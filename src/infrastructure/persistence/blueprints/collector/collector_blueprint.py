from flask import Blueprint, Response, request, jsonify

from src.application.read_model.collector import CollectorData
from src.infrastructure.persistence.queries.collector.get_collector_by_id import get_collector_by_id

ticket_blueprint = Blueprint('ticket_blueprint', __name__)

@ticket_blueprint.route("/<string:id>", methods=["GET"])
def get_collector_by_id_handle(id: str):
    assert isinstance(id, str)
    collector: CollectorData = get_collector_by_id(id=id)
    return jsonify()
