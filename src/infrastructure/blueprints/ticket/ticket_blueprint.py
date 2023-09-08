import json

from flask import Blueprint, Response, request, jsonify

from src.infrastructure.persistence.queries.ticket.get_ticket_by_id import get_ticket_by_id
from src.infrastructure.persistence.queries.ticket.get_tickets_by_collector_id import get_tickets_by_collector_id
from src.infrastructure.blueprints.serializers.ticket import serialize_ticket_to_json

ticket_blueprint = Blueprint("ticket_blueprint", __name__)

@ticket_blueprint.route("/<string:id>", methods=["GET"])
def get_ticket_by_id_handler(id: str):
    return jsonify()

@ticket_blueprint.route("/collector-tickets/<string:collector_id>", methods=["GET"])
def get_tickets_by_collector_id_handler(collector_id: str):
    tickets = get_tickets_by_collector_id(collector_id=collector_id)
    ticket_json = list(map(serialize_ticket_to_json, tickets)) 
    return Response(response=json.dumps(ticket_json), 
                    status=200, 
                    mimetype="application/json")
