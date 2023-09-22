from flask import Blueprint, request, jsonify

from src.application.read_model.manager import ManagerData
from src.application.queries.manager import login_manager

from src.infrastructure.persistence.queries.manager.get_manager_by_id import get_manager_by_id
from src.infrastructure.blueprints.serializers.manager import serialize_manager_to_json

manager_blueprint = Blueprint('manager_blueprint', __name__)

@manager_blueprint.route("/<string:id>", methods=["GET"])
def get_manager_by_id_handle(id: int):
    assert isinstance(id, str)
    manager: ManagerData = get_manager_by_id(id=id)
    manager_json: dict = serialize_manager_to_json(manager)
    return jsonify(**manager_json)

@manager_blueprint.route("/login", methods=["POST"])
def login_manager_handle():
    data = request.get_json()
    if not data:
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

    try:
        manager: ManagerData  = login_manager(username=username, password=password)
        manager_json = serialize_manager_to_json(manager)
        return jsonify(id=manager_json["id"])
    except BaseException as inst:
        return jsonify(msg=str(inst)), 400
        