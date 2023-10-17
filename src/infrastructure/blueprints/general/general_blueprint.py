from flask import Blueprint, request, jsonify

from src.utils.logger import logger

from src.application.read_model.collector import CollectorData
from src.application.read_model.manager import ManagerData

from src.application.queries.collector import login_collector
from src.application.queries.manager import login_manager


general_blueprint = Blueprint('general_blueprint', __name__)

@general_blueprint.route("/login", methods=["POST"])
def login_handle():
    data = request.get_json()
    if not data:
        logger.error(f"NO REQUEST BODY GIVEN FOR GENERAL LOGIN BY :  {request.remote_addr}")
        return jsonify(
            msg="just must give username and password"
        ), 400
    
    username: str
    password: str 
    try:
        username=data["username"]
        password=data["password"]
    except KeyError:
        logger.error(f"NO VAID PARAMETERS ARE GIVEN FOR GENERAL LOGIN BY: {request.remote_addr}")
        return jsonify(
            msg="username and password parameters must be given"
        ), 400

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
            logger.info(f"MANAGER WITH ID: {manager.id} WAS LOGGED IN BY {request.remote_addr}")
            return jsonify(id=manager.id, role="MANAGER")
        else:
            logger.info(f"COLLECTOR WITH ID: {manager.id} WAS LOGGED IN BY {request.remote_addr}")
            return jsonify(id=collector.id, role="COLLECTOR")
        
    except BaseException as inst:
        logger.critical(f"ERROR WHILE LOGGING IN COLLECTOR OR MANAGER ID BY {request.remote_addr}", exc_info=True)
        return jsonify(msg=str(inst)), 400
