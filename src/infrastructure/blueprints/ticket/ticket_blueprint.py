import json

from flask import Blueprint, Response, request, jsonify

from src.utils.logger import logger

from src.application.commands.ticket.create_ticket import create_ticket

from src.domain.ticket.ticket_state import TicketState
from src.infrastructure.persistence.queries.ticket.get_ticket_by_id import get_ticket_by_id
from src.infrastructure.persistence.queries.ticket.get_tickets_by_collector_id import get_tickets_by_collector_id
from src.infrastructure.persistence.queries.ticket.get_tickets_by_manager_id import get_tickets_by_manager_id
from src.infrastructure.blueprints.serializers.ticket import serialize_ticket_to_json
from src.infrastructure.persistence.commands.change_status import change_status
from src.infrastructure.persistence.commands.change_collector_comments import change_collector_comments

ticket_blueprint = Blueprint("ticket_blueprint", __name__)

@ticket_blueprint.route("/<string:id>", methods=["GET"])
def get_ticket_by_id_handler(uuid: str):
    return jsonify()

@ticket_blueprint.route("/collector-tickets/<int:collector_id>", methods=["GET"])
def get_tickets_by_collector_id_handler(collector_id: int):
    try:
        tickets = get_tickets_by_collector_id(collector_id=collector_id)
        ticket_json = list(map(serialize_ticket_to_json, tickets)) 
        respObject = {
            "tickets": ticket_json
        }
        logger.info(f"FETCHED THE TICKETS OF THE COLLECTOR WITH ID: {collector_id} BY {request.remote_addr}")
        return Response(response=json.dumps(respObject), 
                        status=200, 
                        mimetype="application/json")
    except BaseException as inst:
        logger.critical(f"ERROR WHILE FETCHING THE THICKETS OF THE COLLECTOR WITH ID {collector_id} BY {request.remote_addr}", exc_info=True)
        return jsonify(
            msg="ERROR"
        ), 500

@ticket_blueprint.route("/manager-tickets/<int:manager_id>", methods=["GET"])
def get_tickets_by_manager_id_handler(manager_id: int):
    try: 
        tickets = get_tickets_by_manager_id(manager_id=manager_id)
        ticket_json = list(map(serialize_ticket_to_json, tickets)) 
        respObject = {
            "tickets": ticket_json
        }
        logger.info(f"FETCHED TICKETS OF MANAGER WITH ID: {manager_id} BY: {request.remote_addr}")
        return Response(response=json.dumps(respObject), 
                        status=200, 
                        mimetype="application/json")
    except BaseException as inst:
        logger.critical(f"FAILED TO FETCH TICKETS OF MANAGER WITH ID: {manager_id} BY {request.remote_addr}", exc_info=True)
        return jsonify(
            msg="ERROR"
        ), 500


@ticket_blueprint.route("/change_state", methods=["POST"])
def change_state_handler():
    data = request.get_json()
    if not data:
        logger.error(f"NO REQUEST BODY GIVEN BY {request.remote_addr} TO CHANGE THE STATE OF A TICKET")
        return jsonify(
            msg="no request body given"
        ), 400
    
    if ("ticket_id" not in data) or ("new_state" not in data):
        logger.error(f"NO VALID PARAMETERS GIVEN BY {request.remote_addr} TO CHANGE THE STATE OF A TICKET")
        return jsonify(
            msg="ticket_id and new_state must be given"
        ), 400

    try:
        change_status(ticket_id=data["ticket_id"], new_state=TicketState(data["new_state"]))
        logger.info(f"STATE OF THE TICKET WITH ID: {data['ticket_id']} CHANGED TO: {data['new_state']} BY: {request.remote_addr}")
        return jsonify(
            msg="state changed"
        )
    except BaseException as inst:
        logger.critical(f"FAILED TO CHANGE THE TICKET WITH ID: {data['ticket_id']} TO: {data['new_state']} BY: {request.remote_addr}", exc_info=True)
        return jsonify(
            msg=str(inst)
        ), 500

@ticket_blueprint.route("/change_collector_comments", methods=["POST"])
def change_collector_comments_handler():
    data = request.get_json()
    if not data:
        logger.error(f"NO REQUEST BODY GIVEN BY: {request.remote_addr} TO CHANGE THE COLLECTOR COMMENTS OF A TICKET")
        return jsonify(
            msg="no request body given"
        ), 400
    
    if ("ticket_id" not in data) or ("collector_comments" not in data):
        logger.error(f"THE REQUEST PARAMETERS NEEDED TO CHANGE COLLECTOR COMMENTS OF A TICKET WHERE NOT GIVEN BY {request.remote_addr}")
        return jsonify(
            msg="ticket_id and collector_comments must be given"
        ), 400

    try:
        change_collector_comments(ticket_id=data["ticket_id"], collector_comments=data["collector_comments"])
        logger.info(f"CHANGED COLLECTOR COMMENTS OF TICKET WITH ID: {data['ticket_id']} TO: {data['collector_comments']}")
        return jsonify(
            msg="comments changed"
        )
    except BaseException as inst:
        logger.critical(f"FAILED TO CHANGE COLLECTOR COMMENTS OF TICKET WITH ID: {data['ticket_id']} TO: {data['collector_comments']}", exc_info=True)
        return jsonify(
            msg="error"
        ), 500


@ticket_blueprint.route("/create_ticket", methods=["POST"])
def create_ticket_handler():
    data = request.get_json()
    if not data:
        logger.error(f"NO REQUEST BODY GIVEN BY {request.remote_addr} TO CREATE A TICKET")
        return jsonify(
            msg="no request body given"
        ), 400
    try:
        ticket_id = create_ticket(**data)
        logger.info(f"TICKET WITH ID: {ticket_id} CREATED BY {request.remote_addr}")
        return jsonify(
            id=ticket_id
        )
    except BaseException as inst:
        logger.exception(f"FAILED TO CREATE A TICKET BY: {request.remote_addr}", exc_info=True)
        return jsonify(
            msg=str(inst)
        )
