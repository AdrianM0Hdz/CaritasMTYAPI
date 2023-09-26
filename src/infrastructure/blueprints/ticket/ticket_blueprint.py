import json

from flask import Blueprint, Response, request, jsonify

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
    tickets = get_tickets_by_collector_id(collector_id=collector_id)
    ticket_json = list(map(serialize_ticket_to_json, tickets)) 
    respObject = {
        "tickets": ticket_json
    }
    return Response(response=json.dumps(respObject), 
                    status=200, 
                    mimetype="application/json")

@ticket_blueprint.route("/manager-tickets/<int:manager_id>", methods=["GET"])
def get_tickets_by_manager_id_handler(manager_id: int):
    tickets = get_tickets_by_manager_id(manager_id=manager_id)
    ticket_json = list(map(serialize_ticket_to_json, tickets)) 
    respObject = {
        "tickets": ticket_json
    }
    return Response(response=json.dumps(respObject), 
                    status=200, 
                    mimetype="application/json")


@ticket_blueprint.route("/change_state/<int:ticket_id>", methods=["POST"])
def change_state_handler(ticket_id: int):
    data = request.get_json()
    if not data:
        return jsonify(
            msg="no request body given"
        ), 400
    
    try:
        change_status(ticket_id=ticket_id, new_state=TicketState(data["new_state"]))
        return jsonify(
            msg="state changed"
        )
    except BaseException as inst:
        return jsonify(
            msg=str(inst)
        )

@ticket_blueprint.route("/change_collector_comments/<int:ticket_id>", methods=["POST"])
def change_collector_comments_handler(ticket_id: int):
    data = request.get_json()
    if not data:
        return jsonify(
            msg="no request body given"
        ), 400
    
    try:
        change_collector_comments(ticket_id=ticket_id, collector_comments=data["collector_comments"])
        return jsonify(
            msg="comments changed"
        )
    except BaseException as inst:
        return jsonify(
            msg=str(inst)
        )


@ticket_blueprint.route("/create_ticket", methods=["POST"])
def create_ticket_handler():
    data = request.get_json()
    if not data:
        return jsonify(
            msg="no request body given"
        ), 400
    try:
        ticket_id = create_ticket(**data)
        return jsonify(
            id=ticket_id
        )
    except BaseException as inst:
        return jsonify(
            msg=str(inst)
        )
