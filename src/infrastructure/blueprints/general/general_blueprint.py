from flask import Blueprint, request, jsonify

from src.application.read_model.collector import CollectorData
from src.application.read_model.manager import ManagerData

from src.application.queries.collector import login_collector
from src.application.queries.manager import login_manager



general_blueprint = Blueprint('general_blueprint', __name__)

@general_blueprint.route("/login", methods=["POST"])
def login_handle():
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

        try: 
            collector: CollectorData  = login_collector(username=username, password=password)
        except BaseException as inst:
            print(inst)
            collector = None
        
        try:
            manager: ManagerData  = login_manager(username=username, password=password)
        except BaseException as inst:
            print(inst)
            manager = None

        if collector == None and manager == None:
            raise BaseException("INCORRECT USERNAME OR PASSWORD")
        elif collector == None:
            return jsonify(id=manager.id, role="MANAGER")
        else:
            return jsonify(id=collector.id, role="COLLECTOR")
        
    except BaseException as inst:
        return jsonify(msg=str(inst)), 400
