import json
import math
import os
import random
import string
import uuid
from pathlib import Path

import bw2data as bd
import flask
import tomli
import whoosh
from bw2analyzer import PageRank
from bw2data.backends import ActivityDataset as AD
from flask_httpauth import HTTPBasicAuth
from peewee import fn
from werkzeug.security import check_password_hash, generate_password_hash

from .comments import Comment, CommentThread
from .utils import (
    MATCH_TYPE_ABBREVIATIONS,
    get_match_types,
    name_close_enough,
    similar_location,
)

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

matchbox_app = flask.Flask(
    "matchbox_app",
    static_folder=BASE_DIR / "assets",
    template_folder=BASE_DIR / "assets" / "templates",
)
matchbox_app.config["SECRET_KEY"] = os.urandom(24)

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    users = matchbox_app.config["mb_users"]
    if username in users and check_password_hash(users.get(username), password):
        return username


def configure_app(filepath, app):
    try:
        config_fp = Path(filepath)
        assert config_fp.exists
        with open(config_fp, "rb") as f:
            config = tomli.load(f)
        assert "users" in config
        assert "configs" in config
        assert "roles" in config
        assert "files" in config
    except:
        # NOTE: If you got this exception, make sure first you don't have
        # windows-style backslahes in your config file for file names (no
        # double `\\`).
        raise ValueError("Invalid or unreadable config file")

    app.config["mb_configs"] = config["configs"]
    app.config["mb_roles"] = config["roles"]
    app.config["mb_users"] = {
        user: generate_password_hash(password)
        for user, password in config["users"].items()
    }
    app.config["mb_output_dir"] = Path(config["files"]["output_dir"])
    if not (
        app.config["mb_output_dir"].is_dir()
        and os.access(app.config["mb_output_dir"], os.W_OK)
    ):
        raise ValueError("`output_dir` is invalid")

    app.config["mb_match_types"] = get_match_types(app.config["mb_output_dir"])

    return app


def return_invalid_config(config):
    # TBD #90
    raise ValueError(f"Invalid configuration: {config}")


def get_role(config):
    for role, lst in config["roles"].items():
        for name in lst:
            if name == config["user"]:
                return role


def get_config():
    config_label = flask.request.cookies.get("config")
    if not config_label:
        return flask.redirect(flask.url_for("select_config"))

    try:
        # TBD #90: Provide good error messages
        config = matchbox_app.config["mb_configs"][config_label]
        config["roles"] = matchbox_app.config["mb_roles"]
        config["config_label"] = config_label
        config["user"] = auth.current_user()
        config["role"] = get_role(config)
        config["output_dir"] = matchbox_app.config["mb_output_dir"]
    except KeyError:
        return flask.redirect(flask.url_for("select_config"))

    if config["project"] not in bd.projects:
        return_invalid_config(config)

    bd.projects.set_current(config["project"])
    return config


def get_match_type_for_source_process(node):
    if hasattr(node, "data"):
        if "match_type" in node.data:
            label = matchbox_app.config["mb_match_types"].get(
                node.data["match_type"], "Unknown"
            )
            return MATCH_TYPE_ABBREVIATIONS.get(label, label)
        elif node.data.get("proxy_id"):
            mt = bd.get_node(id=node.data["proxy_id"]).get("match_type")
            label = matchbox_app.config["mb_match_types"].get(mt, "Unknown")
            return MATCH_TYPE_ABBREVIATIONS.get(label, label)
        else:
            return "Unknown"
    elif "match_type" in node:
        label = matchbox_app.config["mb_match_types"].get(node["match_type"], "Unknown")
        return MATCH_TYPE_ABBREVIATIONS.get(label, label)
    else:
        mt = bd.get_node(id=node["proxy_id"]).get("match_type")
        if not mt or mt == "0":
            return "Unknown"
        else:
            label = matchbox_app.config["mb_match_types"].get(mt, "Unknown")
            return MATCH_TYPE_ABBREVIATIONS.get(label, label)


@matchbox_app.route("/delete-all-comments", methods=["GET"])
@auth.login_required
def delete_all_comments():
    config = get_config()
    if config["role"] != "editors":
        flask.abort(403)

    Comment.delete().execute()
    CommentThread.delete().execute()

    return ""


@matchbox_app.route("/generate-fake-comments", methods=["GET"])
@auth.login_required
def generate_fake_comments():
    config = get_config()
    if config["role"] != "editors":
        flask.abort(403)

    from faker import Faker

    fake = Faker(["it_IT", "en_US", "ja_JP", "ru_RU"])
    import random

    names = [fake.name() for _ in range(8)]
    processes = [ds.id for ds, _ in zip(bd.Database(config["proxy"]), range(20))]

    for process in processes:
        num_comments = abs(int(2 * random.normalvariate(mu=0, sigma=5)))
        if not num_comments:
            continue

        thread = CommentThread.create(
            name=fake.text()[:20], process_id=process, resolved=random.random() < 0.2
        )

        for index in range(num_comments):
            Comment.create(
                thread=thread, content=fake.text(), user=random.choice(names)
            )

    return ""


def format_process(obj_id):
    node = bd.get_node(id=obj_id)
    return {
        "id": node.id,
        "database": node["database"],
        "name": node["name"],
        "unit": node["unit"],
        "location": node["location"],
        "product": node["reference product"],
        "url": flask.url_for("process_detail", id=node.id),
    }


@matchbox_app.route("/comments-api", methods=["GET"])
@auth.login_required
def comments_api():
    """
    API to populate dynamic comments display.

    Optional GET parameters.

    * `user`: str. Username to filter by
    * `process`: int. Proxy process ID
    * `resolved`: str, either "0" or "1". Whether comment thread is resolved or not
    * `thread`: int. Comment thread id

    JSON Return format, sorted by ascending comment thread and then comment position.

        {
            "total_threads": int,
            "total_comments": int,
            "data": [
                {
                    "thread_id": int, 1-indexed (from db),
                    "thread_name": str,
                    "resolved": bool,
                    "process": {
                        "id": int, 1-indexed (from db),
                        "database": str,
                        "name": str,
                        "unit": str,
                        "location": str,
                        "product": str,
                        "url": str, relative URL,
                    },
                    "content": str,
                    "position": int, 0-indexed,
                    "user": str,
                }
                for obj in qs.dicts()
            ],
        }

    """
    get_config()

    qs = (
        Comment.select(
            Comment.position,
            Comment.content,
            Comment.user,
            Comment.id,
            CommentThread.id.alias("thread_id"),
            CommentThread.name,
            CommentThread.resolved,
            CommentThread.process_id,
        )
        .join(CommentThread)
        .order_by(CommentThread.id.asc(), Comment.position.asc())
    )

    user = flask.request.args.get("user")
    process = flask.request.args.get("process")
    resolved = flask.request.args.get("resolved")
    thread = flask.request.args.get("thread")

    if user:
        qs = qs.where(Comment.user == user)
    if process:
        qs = qs.where(CommentThread.process_id == int(process))
    if resolved and resolved in "01":
        qs = qs.where(CommentThread.resolved == (True if resolved == "1" else False))
    if thread:
        qs = qs.where(CommentThread.id == int(thread))

    payload = {
        "total_threads": CommentThread.select().count(),
        "total_comments": Comment.select().count(),
        "data": [
            {
                "thread_id": obj["thread_id"],
                "thread_name": obj["name"],
                "resolved": obj["resolved"],
                "process": format_process(obj["process_id"]),
                "content": obj["content"],
                "position": obj["position"],
                "user": obj["user"],
            }
            for obj in qs.dicts()
        ],
    }
    return flask.jsonify(payload)


@matchbox_app.route("/page-rank", methods=["GET"])
@auth.login_required
def build_page_rank_cache():
    config = get_config()
    if config["role"] != "editors":
        flask.abort(403)

    pr = PageRank(bd.Database(config["source"])).calculate()
    with open(config["output_dir"] / "page-rank.json", "w") as f:
        json.dump({"scores": pr}, f, indent=2)
    return ""


def get_page_rank_cache():
    fp = Path(matchbox_app.config["mb_output_dir"]) / "page-rank.json"
    if fp.is_file():
        return json.load(open(fp))["scores"]
    else:
        return []


@matchbox_app.route("/select-config", methods=["POST", "GET"])
@auth.login_required
def select_config():
    if flask.request.method == "POST":
        config_name = flask.request.form["config"]
        resp = flask.make_response(flask.redirect(flask.url_for("index")))
        resp.set_cookie("config", config_name)
        return resp
    else:
        resp = flask.make_response(
            flask.render_template(
                "select_config.html",
                config_labels=matchbox_app.config["mb_configs"],
                config={"user": auth.current_user()},
            )
        )
        resp.delete_cookie("config")
        return resp


@matchbox_app.route("/", methods=["GET"])
@auth.login_required
def index():
    config = get_config()
    if isinstance(config, flask.Response):
        return config

    return flask.render_template(
        "index.html",
        title="Matchbox Index",
        unmatched_link=True,
        config=config,
        table_data=[],
        query_string="",
    )


def apply_filter_to_qs(qs, filter_arg):
    if not filter_arg:
        return qs
    elif filter_arg == "unmatched":
        return [node for node in qs if not node.data.get("matched")]
    else:
        return [node for node in qs if node.data.get(filter_arg)]


def apply_limit_offset(qs, limit, offset):
    if offset:
        qs = qs[offset:]
    if limit:
        qs = qs[:limit]
    return qs


def maybe_int(value):
    if value in (None, ""):
        return None
    else:
        return int(value)


def get_proxy_url(ds):
    if isinstance(ds, AD) and "proxy_id" in ds.data:
        return flask.url_for("process_detail", id=ds.data["proxy_id"])
    elif not isinstance(ds, AD) and "proxy_id" in ds:
        return flask.url_for("process_detail", id=ds["proxy_id"])
    else:
        return None


@matchbox_app.route("/processes", methods=["GET"])
@auth.login_required
def processes():
    """API Endpoint to get process data for dynamic table population.

    GET args:

    * database (str): Name of database to draw processes from. Defaults to source
                    database (stored in cookie) if not given.
    * limit (int): Number of results to return
    * order_by (str, optional): Parameter to sort by. Random if not provided.
                    Valid parameters:
        * name (will be used 99% of the time)
        * location
        * product (short name for reference product)
    * offset (int, optional): Offset from beginning of sorted values. Zero-indexed.
                    Only used if sorting.
    * filter (string, optional): Optional attribute filter. Should be one of
                    `matched`, `unmatched`, or `waitlist`.
    * search (string, optional): Optional parameter to pass to search index.
                    Note that this overrides `order_by`.

    Response data format (JSON):

    ```
        [
            {
                'details_url': 'URL for `process_detail` page for this activity',
                'match_url': 'URL for `match` page for this activity',
                'matched': 'Boolean. Whether or not process is already matched.',
                'waitlist': 'Boolean. Whether or not process has attribute `waitlist`.',
                'id': 'Integer process ID',
                'name': 'Process name',
                'location': 'Process location',
                'unit': 'Unit of reference product',
            }
        ]
    ```
    """
    config = get_config()

    database_label = flask.request.args.get("database") or config["source"]
    limit = maybe_int(flask.request.args.get("limit"))
    offset = maybe_int(flask.request.args.get("offset"))
    filter_arg = flask.request.args.get("filter")
    order_by = flask.request.args.get("order_by")

    pr = get_page_rank_cache()

    search_query = flask.request.args.get("search")
    if search_query:
        # Override default too small search limit
        qs = [
            x._document
            for x in bd.Database(database_label).search(search_query, limit=1000)
        ]
        if filter_arg:
            qs = apply_filter_to_qs(qs, filter_arg)
        total_records = len(qs)
        qs = apply_limit_offset(qs, limit, offset)
    elif order_by == "importance":
        limit = limit or 250
        offset = offset or 0
        qs = [bd.get_node(id=id_)._document for _, id_ in pr[offset : offset + limit]]
        qs = apply_filter_to_qs(qs, filter_arg)
        total_records = len(bd.Database(config["source"]))
    else:
        qs = AD.select().where(AD.database == database_label)

        if order_by and order_by in ("name", "location", "product"):
            qs = qs.order_by(getattr(AD, order_by))
        else:
            qs = qs.order_by(fn.Random())

        if not filter_arg:
            total_records = qs.count()

            if offset:
                qs = qs.offset(offset)
            if limit:
                qs = qs.limit(limit)
        else:
            qs = apply_filter_to_qs(qs, filter_arg)
            total_records = len(qs)
            qs = apply_limit_offset(qs, limit, offset)

    payload = {
        "total_records": total_records,
        "data": [
            {
                "details_url": flask.url_for("process_detail", id=obj.id),
                "match_url": flask.url_for("match", source=obj.id),
                "proxy_url": get_proxy_url(obj),
                "matched": bool(obj.data.get("matched")),
                "match_type": get_match_type_for_source_process(obj),
                "waitlist": bool(obj.data.get("waitlist")),
                "id": obj.id,
                "name": obj.name,
                "location": obj.location,
                "product": obj.product,
                "unit": obj.data["unit"],
            }
            for obj in qs
        ],
    }
    return flask.jsonify(payload)


@matchbox_app.route("/search/", methods=["GET"])
@auth.login_required
def search():
    config = get_config()
    if isinstance(config, flask.Response):
        return config

    q = flask.request.args.get("q")
    embed = flask.request.args.get("e")
    json = flask.request.args.get("json")  # Return the data as json
    search_db = flask.request.args.get("database")

    table_data = bd.Database(search_db or config["target"]).search(q, limit=100)

    if json:
        MAPPING = {"reference product": "referenceProduct"}
        FIELDS = {"name", "id", "location", "unit", "reference product"}

        payload = [
            {MAPPING.get(key, key): ds.get(key) for key in FIELDS} for ds in table_data
        ]
        return flask.jsonify(payload)
    elif embed:
        source = bd.get_activity(id=int(flask.request.args.get("source")))
        return flask.render_template(
            "search-embedded.html",
            source=source,
            table_data=table_data,  # bd.Database(search_db or t).search(q, limit=100),
        )
    else:
        return flask.render_template(
            "index.html",
            config=config,
            title="bw_matchbox Search Result",
            table_data=table_data,  # =bd.Database(search_db).search(q, limit=100),
            query_string=q,
        )


@matchbox_app.route("/add-attribute/<id>", methods=["GET"])
@auth.login_required
def add_attribute(id):
    config = get_config()
    if isinstance(config, flask.Response):
        return config

    if config["role"] != "editors":
        flask.abort(403)

    node = bd.get_node(id=id)

    attr = flask.request.args.get("attr")
    value = flask.request.args.get("value")

    if attr is None or value is None:
        flask.abort(400)
    if attr in ("waitlist", "matched"):
        if value not in ("0", "1"):
            flask.abort(400)
        value = {"0": False, "1": True}[value]

    node[attr] = value

    try:
        node.save()
    except whoosh.index.LockError:
        # MAIN_WRITELOCK not being released. Can ignore as we don't
        # change anything that is in the index anyway.
        pass
    return ""


def get_authors(authors):
    if not authors:
        return "Unknown"
    elif isinstance(authors, list):
        return ", ".join({obj.get("name", "Unknown") for obj in authors})
    else:
        return ", ".join({obj.get("name", "Unknown") for obj in authors.values()})


@matchbox_app.route("/remove-match/<id>", methods=["GET"])
@auth.login_required
def remove_match(id):
    """Remove match information.

    If the referenced process is in the proxy database, it will be deleted, and the
    source process matching attributes will be removed.

    If the reference process is in the source database, its matching attributes will
    be removed, and it's proxy process (if any) will be deleted.

    If the reference process is from any other database, no action is taken.

    Returns a redirect to the source dataset process details view."""
    config = get_config()
    if isinstance(config, flask.Response):
        return config

    if config["role"] != "editors":
        flask.abort(403)

    node = bd.get_node(id=id)
    if node["database"] == config["proxy"]:
        if node.get("original_id"):
            reference = bd.get_node(id=node["original_id"])
            for field in ("proxy_id", "matched", "match_type"):
                if field in reference:
                    del reference[field]
            reference.save()
        else:
            reference = None

        node.delete()

        return_url = (
            flask.url_for("process_detail", id=reference.id)
            if reference
            else flask.url_for("index")
        )
    elif node["database"] == config["source"]:
        if "proxy_id" in node:
            bd.get_node(id=node["proxy_id"]).delete()
        for field in ("proxy_id", "matched", "match_type"):
            if field in node:
                del node[field]
        node.save()
        return_url = flask.url_for("process_detail", id=node.id)
    else:
        return_url = flask.url_for("process_detail", id=reference.id)

    return flask.redirect(return_url)


@matchbox_app.route("/process/<id>", methods=["GET"])
@auth.login_required
def process_detail(id):
    config = get_config()
    if isinstance(config, flask.Response):
        return config

    try:
        node = bd.get_node(id=id)
    except bd.errors.UnknownObject:
        return flask.redirect(flask.url_for("index"))

    proxy_node = bd.get_node(id=node["proxy_id"]) if node.get("proxy_id") else None
    reference_node = (
        bd.get_node(id=node["original_id"]) if node.get("original_id") else None
    )

    same_name = AD.select().where(
        AD.name == node["name"], AD.database == node["database"], AD.id != node.id
    )
    same_name_count = same_name.count()
    technosphere = sorted(node.technosphere(), key=lambda x: x.input["name"])
    biosphere = sorted(node.biosphere(), key=lambda x: x.input["name"])
    is_proxy = node["database"] == config["proxy"]

    return flask.render_template(
        "process_detail.html",
        title="bw_matchbox Detail Page",
        ds=node,
        config=config,
        authors=get_authors(node.get("authors")),
        proxy_node=proxy_node,
        reference_node=reference_node,
        source=config["source"],
        same_name_count=same_name_count,
        same_name=same_name,
        technosphere=technosphere,
        biosphere=biosphere,
        match_type=matchbox_app.config["mb_match_types"].get(node.get("match_type")),
        total_consumers=len(node.upstream()),
        consumers=list(node.upstream())[:50],
        is_proxy=is_proxy,
    )


@matchbox_app.route("/multi-match/<id>", methods=["GET"])
@auth.login_required
def multi_match(id):
    config = get_config()
    if isinstance(config, flask.Response):
        return config

    if config["role"] != "editors":
        flask.abort(403)

    node = bd.get_node(id=id)
    node["matched"] = True
    node["match_type"] = "1"
    node["waitlist"] = False
    node.save()

    for ds in AD.select().where(
        AD.name == node["name"], AD.database == node["database"], AD.id != node.id
    ):
        if not ds.data.get("matched"):
            ds.data["matched"] = True
            ds.data["match_type"] = "1"
            ds.data["waitlist"] = False
            ds.save()
    return ""


@matchbox_app.route("/match/<source>", methods=["GET"])
@auth.login_required
def match(source):
    config = get_config()
    if isinstance(config, flask.Response):
        return config

    if config["role"] != "editors":
        flask.abort(403)

    node = bd.get_node(id=source)

    if node['matched']:
        return flask.redirect(flask.url_for("process_detail", id=node.id))

    matches = bd.Database(config["target"]).search(
        node["name"] + " " + node.get("location", "")
    )

    MAPPING = {"reference product": "referenceProduct"}
    FIELDS = {"name", "id", "location", "unit", "reference product"}
    matches_payload = [
        {MAPPING.get(key, key): ds.get(key) for key in FIELDS} for ds in matches
    ]

    return flask.render_template(
        "match.html",
        title="Database Matching Page",
        config=config,
        ds=node,
        query_string=node["name"] + " " + node.get("location", ""),
        matches=matches,
        matches_json=json.dumps(matches_payload),
    )


def check_similar(node, candidates):
    for index, candidate in enumerate(candidates):
        if node.get("collapsed") or candidate.get("collapsed"):
            continue
        if (
            name_close_enough(node["name"], candidate["name"])
            and similar_location(node["location"], candidate["location"])
            and node["unit"] == candidate["unit"]
            and math.isclose(
                node["amount"], candidate["amount"], rel_tol=0.025, abs_tol=1e-6
            )
        ):
            node["collapsed"] = candidate["collapsed"] = True
            node["collapsed-group"] = candidate[
                "collapsed-group"
            ] = "Collapsed-{}-{}".format(
                index, "".join(random.choices(string.ascii_letters, k=6))
            )


@matchbox_app.route("/compare/<source>/<target>", methods=["GET"])
@auth.login_required
def compare(source, target):
    config = get_config()
    if isinstance(config, flask.Response):
        return config

    source = bd.get_node(id=int(source))
    target = bd.get_node(id=int(target))

    source_technosphere = [
        {
            "amount": exc["amount"],
            "amount_display": "{:0.2g}".format(exc["amount"]),
            "name": exc.input["name"],
            "unit": exc.input["unit"],
            "location": exc.input["location"],
            "input_id": exc.input.id,
            "url": flask.url_for("process_detail", id=exc.input.id),
            # Issue #59: Name cell with check icon for 'matched' rows
            "matched": bool(exc.input.get("matched")),
        }
        for exc in source.technosphere()
    ]
    target_itself = {
        "amount": 1,
        "amount_display": "1.0",
        "name": target["name"],
        "unit": target["unit"],
        "location": target.get("location", ""),
        "input_id": target.id,
        "url": flask.url_for("process_detail", id=target.id),
    }
    target_technosphere = [
        {
            "amount": exc["amount"],
            "amount_display": "{:0.2g}".format(exc["amount"]),
            "name": exc.input["name"],
            "unit": exc.input["unit"],
            "location": exc.input["location"],
            "input_id": exc.input.id,
            "url": flask.url_for("process_detail", id=exc.input.id),
        }
        for exc in target.technosphere()
    ]

    for obj in target_technosphere:
        # Modifies in place
        check_similar(obj, source_technosphere)

    base_url = flask.request.base_url.replace(flask.request.path, "")

    return flask.render_template(
        "compare.html",
        config=config,
        title="Database Comparison Page",
        proxy=config["proxy"],
        target_json=json.dumps(target_itself),
        source_node=source,
        source_data_json=json.dumps(source_technosphere),
        source_biosphere_number=len(source.biosphere()),
        target_node=target,
        target_data_json=json.dumps(target_technosphere),
        target_biosphere_number=len(target.biosphere()),
        match_types=matchbox_app.config["mb_match_types"],
        base_url=base_url,
    )


@matchbox_app.route("/expand/<id>/<scale>/", methods=["GET"])
@auth.login_required
def expand(id, scale):
    config = get_config()
    if isinstance(config, flask.Response):
        return config

    node = bd.get_activity(id=int(id))
    scale = float(scale)

    exchanges = list(node.technosphere())
    for exc in exchanges:
        exc["amount"] *= scale

    payload = [
        {
            "amount": exc["amount"],
            "amount_display": "{:0.2g}".format(exc["amount"]),
            "name": exc.input["name"],
            "unit": exc.input["unit"],
            "location": exc.input["location"],
            "input_id": exc.input.id,
            "url": flask.url_for("process_detail", id=exc.input.id),
        }
        for exc in exchanges
    ]
    return flask.jsonify(payload)


@matchbox_app.route("/create-proxy/", methods=["POST"])
@auth.login_required
def create_proxy():
    config = get_config()
    if isinstance(config, flask.Response):
        return config

    if config["role"] != "editors":
        flask.abort(403)

    content = flask.request.get_json()

    source = bd.get_activity(id=content["source"])
    process = bd.Database(config["proxy"]).new_activity(
        name=content["name"],
        code=uuid.uuid4().hex,
        comment=content["comment"],
        unit=source["unit"],
        location=source["location"],
        original_name=source["name"],
        original_id=source.id,
        match_type=content.get("match_type", "0"),
        **{"reference product": source.get("reference product")},
    )
    process.save()

    source_rp = source.rp_exchange()
    process.new_edge(
        input=process, amount=source_rp["amount"], type="production"
    ).save()
    for exc in content["exchanges"]:
        process.new_edge(
            type="technosphere",
            input=bd.get_activity(id=exc["input_id"]),
            amount=exc["amount"],
        ).save()

    source["matched"] = True
    source["waitlist"] = False
    source["proxy_id"] = process.id
    source.save()

    return flask.redirect(flask.url_for("process_detail", id=process.id))
