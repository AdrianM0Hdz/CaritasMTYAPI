from dataclasses import dataclass

from src.domain.ticket.ticket_state import TicketState


@dataclass(frozen=True)
class TicketData:
    id: str
    housing_reference: str
    receipt_comments: str
    reprogramation_comments: str
    house_phone_number: str
    cellphone: str
    manager_id: str
    collector_id: str
    state: TicketState
    date: str
    collector_comments: str
