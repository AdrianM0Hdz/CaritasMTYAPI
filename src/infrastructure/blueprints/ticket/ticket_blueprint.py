import json

from flask import Blueprint, Response, request, jsonify

from src.application.commands.ticket.create_ticket import create_ticket

from src.infrastructure.persistence.queries.ticket.get_ticket_by_id import get_ticket_by_id
from src.infrastructure.persistence.queries.ticket.get_tickets_by_collector_id import get_tickets_by_collector_id
from src.infrastructure.persistence.queries.ticket.get_tickets_by_manager_id import get_tickets_by_manager_id
from src.infrastructure.blueprints.serializers.ticket import serialize_ticket_to_json

ticket_blueprint = Blueprint("ticket_blueprint", __name__)

@ticket_blueprint.route("/<string:id>", methods=["GET"])
def get_ticket_by_id_handler(uuid: str):
    return jsonify()

@ticket_blueprint.route("/collector-tickets/<int:collector_id>", methods=["GET"])
def get_tickets_by_collector_id_handler(collector_id: int):
    tickets = get_tickets_by_collector_id(collector_id=collector_id)
    ticket_json = list(map(serialize_ticket_to_json, tickets)) 
    return Response(response=json.dumps(ticket_json), 
                    status=200, 
                    mimetype="application/json")

@ticket_blueprint.route("/manager-tickets/<int:manager_id>", methods=["GET"])
def get_tickets_by_manager_id_handler(manager_id: int):
    tickets = get_tickets_by_manager_id(manager_id=manager_id)
    ticket_json = list(map(serialize_ticket_to_json, tickets)) 
    return Response(response=json.dumps(ticket_json), 
                    status=200, 
                    mimetype="application/json")


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
