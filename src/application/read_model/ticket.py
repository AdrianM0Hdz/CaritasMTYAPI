from dataclasses import dataclass

from src.domain.ticket.ticket_state import TicketState


@dataclass(frozen=True)
class TicketData:
    id: int
    uuid: str
    housing_reference: str
    street: str
    house_number: int
    municipality: str
    suburb: str
    receipt_comments: str
    reprogramation_comments: str
    house_phone_number: str
    cellphone: str
    manager_id: str
    collector_id: str
    state: TicketState
    date: str
    collector_comments: str
    donation_amount: int
    donor_name: str
