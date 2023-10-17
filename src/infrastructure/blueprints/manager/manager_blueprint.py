from flask import Blueprint, request, jsonify

from src.utils.logger import logger

from src.application.read_model.manager import ManagerData
from src.application.queries.manager import login_manager

from src.infrastructure.persistence.queries.manager.get_manager_by_id import get_manager_by_id
from src.infrastructure.blueprints.serializers.manager import serialize_manager_to_json

manager_blueprint = Blueprint('manager_blueprint', __name__)

@manager_blueprint.route("/<string:id>", methods=["GET"])
def get_manager_by_id_handle(id: int):
    try: 
        assert isinstance(id, str)
        manager: ManagerData = get_manager_by_id(id=id)
        manager_json: dict = serialize_manager_to_json(manager)
        logger.info(f"MANAGER WITH ID: {id} FETCHED BY {request.remote_addr}")
        return jsonify(**manager_json)
    except BaseException as inst:
        logger.critical(f"FAILED TO FETCH MANAGER WITH ID: {id} BY {request.remote_addr}", exc_info=True)
        return jsonify(msg="ERROR"),400

@manager_blueprint.route("/login", methods=["POST"])
def login_manager_handle():
    data = request.get_json()
    if not data:
        logger.error(f"NO REQUEST BODY GIVEN BY {request.remote_addr} TO LOG IN MANAGER")
        return jsonify(
            msg="just must give username and password"
        ), 400
    username: str
    password: str 
    try:
        username=data["username"]
        password=data["password"]
    except KeyError:
        logger.error(f"NO VAILD PRAMETERS GIVEN IN JSON BODY BY {request.remote_addr}, TO LOG IN MANAGER")
        return jsonify(
            msg="username and password parameters must be given"
        ), 400

    try:
        manager: ManagerData  = login_manager(username=username, password=password)
        manager_json = serialize_manager_to_json(manager)
        logger.info(f"MANAGER WITH USERNAME: {username} LOGGED IN BY {request.remote_addr}")
        return jsonify(id=manager_json["id"])
    except BaseException as inst:
        logger.critical(f"FAILED TO LOG IN MANAGER: {username} BY {request.remote_addr}", exc_info=True)
        return jsonify(msg=str(inst)), 400
