from flask import Blueprint, request, jsonify

from src.application.read_model.collector import CollectorData
from src.application.queries.collector import login_collector

from src.infrastructure.persistence.queries.collector.get_collector_by_id import get_collector_by_id
from src.infrastructure.persistence.queries.collector.get_collectors_by_manager_id import get_collectors_by_manager_id
from src.infrastructure.blueprints.serializers.collector import serialize_collector_to_json

collector_blueprint = Blueprint('collector_blueprint', __name__)

@collector_blueprint.route("/<int:id>", methods=["GET"])
def get_collector_by_id_handle(id: int):
    assert isinstance(id, int)
    collector: CollectorData = get_collector_by_id(id=id)
    collector_json: dict = serialize_collector_to_json(collector)
    return jsonify(**collector_json)

@collector_blueprint.route("/get_by_manager_id/<int:manager_id>", methods=["GET"]) 
def get_collectors_by_manager_id_handle(manager_id: int):
    collectors: list[CollectorData] = get_collectors_by_manager_id(manager_id=manager_id)
    collectors_json: list[dict] = list(map(serialize_collector_to_json, collectors))
    return jsonify(collectors=collectors_json)

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
