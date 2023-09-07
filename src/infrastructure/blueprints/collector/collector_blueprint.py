from flask import Blueprint, request, jsonify

from src.application.read_model.collector import CollectorData
from src.infrastructure.persistence.queries.collector.get_collector_by_id import get_collector_by_id
from src.infrastructure.blueprints.serializers.collector import serialize_collector_to_json

ticket_blueprint = Blueprint('ticket_blueprint', __name__)

@ticket_blueprint.route("/<string:id>", methods=["GET"])
def get_collector_by_id_handle(id: str):
    assert isinstance(id, str)
    collector: CollectorData = get_collector_by_id(id=id)
    collector_json: dict = serialize_collector_to_json(collector)
    return jsonify(**collector_json)
