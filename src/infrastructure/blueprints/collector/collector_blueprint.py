from flask import Blueprint, request, jsonify

from src.utils.logger import logger

from src.application.read_model.collector import CollectorData
from src.application.queries.collector import login_collector

from src.infrastructure.persistence.queries.collector.get_collector_by_id import get_collector_by_id
from src.infrastructure.persistence.queries.collector.get_collectors_by_manager_id import get_collectors_by_manager_id
from src.infrastructure.blueprints.serializers.collector import serialize_collector_to_json

collector_blueprint = Blueprint('collector_blueprint', __name__)

@collector_blueprint.route("/<int:id>", methods=["GET"])
def get_collector_by_id_handle(id: int):
    try: 
        assert isinstance(id, int)
        collector: CollectorData = get_collector_by_id(id=id)
        collector_json: dict = serialize_collector_to_json(collector)
        logger.info(f"COLLECTOR WITH ID {id} FETCHED BY {request.remote_addr}")
        return jsonify(**collector_json)
    except BaseException as inst:
        logger.critical(f"FAILED TO FETCH COLLECTOR WITH ID {id} BY {request.remote_addr}", exc_info=True)
        return jsonify(msg="error"), 500

@collector_blueprint.route("/get_by_manager_id/<int:manager_id>", methods=["GET"]) 
def get_collectors_by_manager_id_handle(manager_id: int):
    try:
        collectors: tuple[CollectorData] = get_collectors_by_manager_id(manager_id=manager_id)
        collectors_json: list[dict] = list(map(serialize_collector_to_json, collectors))
        logger.info(f"COLLECTOR FETCHED BY MANAGER ID: {manager_id} BY: {request.remote_addr}")
        return jsonify(collectors=collectors_json)
    except BaseException as inst:
        logger.critical(f"FAILED TO FECTH COLLECTOR BY MANAGER ID: {manager_id} BY {request.remote_addr}", exc_info=True)
        return jsonify(msg="error"), 500

@collector_blueprint.route("/login", methods=["POST"])
def login_collector_handle():
    data = request.get_json()
    if not data:
        logger.error(f"NO REQUEST BODY GIVEN BY {request.remote_addr} TO LOGIN COLLECTOR")
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
        logger.error(f"INVALID LOGIN COLLECTOR PARAMETERS GIVEN BY {request.remote_addr}")
        return jsonify(
            msg="username and password parameters must be given"
        ), 400

    try:
        collector: CollectorData  = login_collector(username=username, password=password)
        collector_json = serialize_collector_to_json(collector)
        logger.info(f"CORRECTLY LOGGED COLLECTOR {username} BY {request.remote_addr}")
        return jsonify(id=collector_json["id"])
    except BaseException as inst:
        return jsonify(msg=str(inst)), 500
