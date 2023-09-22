from src.application.read_model.collector import CollectorData

from ..ticket import serialize_ticket_to_json

def serialize_collector_to_json(collector: CollectorData) -> dict:
    return {
        "id": collector.id,
        "uuid": collector.uuid,
        "username": collector.username,
        "password": collector.password,
        "fullname": collector.fullname,
        "managerId": collector.manager_id,
        "tickets": list(map(serialize_ticket_to_json, collector.tickets))
    }