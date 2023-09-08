from flask import Blueprint, request, jsonify

from src.application.read_model.collector import CollectorData
from src.application.queries.collector import login_collector

from src.infrastructure.persistence.queries.collector.get_collector_by_id import get_collector_by_id
from src.infrastructure.blueprints.serializers.collector import serialize_collector_to_json

collector_blueprint = Blueprint('collector_blueprint', __name__)

@collector_blueprint.route("/<string:id>", methods=["GET"])
def get_collector_by_id_handle(id: str):
    assert isinstance(id, str)
    collector: CollectorData = get_collector_by_id(id=id)
    collector_json: dict = serialize_collector_to_json(collector)
    return jsonify(**collector_json)

@collector_blueprint.route("/login", methods=["POST"])
def login_collector_handle():
    data = request.get_json()
    if not data:
        print("no json body")
        return jsonify(
            msg="just must give username and password"
        ), 400
    
    username: str
    password: str 
    try:
        username=data["username"]
        password=data["password"]
    except KeyError:
        return jsonify(
            msg="username and password parameters must be given"
        ), 400
    print("passed check")
    try:
        collector: CollectorData  = login_collector(username=username, password=password)
        collector_json = serialize_collector_to_json(collector)
        return jsonify(id=collector_json["id"])
    except BaseException as inst:
        return jsonify(msg=str(inst)), 400
