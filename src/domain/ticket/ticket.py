from uuid import uuid1
from dataclasses import dataclass
import datetime
from typing import List

from .ticket_state import TicketState

@dataclass
class Ticket:
    id: int
    uuid: str
    housing_reference: str
    receipt_comments: str
    reprogramation_comments: str
    house_phone_number: str
    cellphone: str
    manager_id: str
    collector_id: str
    state: TicketState
    date: datetime.date
    collector_comments: str
    donation_amount: int
    donor_name: str

    @classmethod
    def create_new(cls, 
                   uuid: str,
                   housing_reference: str, 
                   street: str,
                   house_number: int,
                   municipality: str,
                   suburb: str,
                   receipt_comments: str, 
                   reprogramation_comments: str, 
                   house_phone_number: str, 
                   cellphone: str, 
                   manager_id: str, 
                   collector_id: str,
                   date: datetime.date, 
                   collector_comments: str,
                   donation_amount: int,
                   donor_name: str): 
        return cls(
            uuid=uuid,
            housing_reference=housing_reference, 
            street=street,
            house_number=house_number,
            municipality=municipality,
            suburb=suburb,
            receipt_comments=receipt_comments, 
            reprogramation_comments=reprogramation_comments,
            house_phone_number=house_phone_number, 
            cellphone=cellphone, 
            manager_id=manager_id, 
            collector_id=collector_id, 
            state=TicketState.PENDING, 
            date=date, 
            collector_comments=collector_comments,
            donation_amount=donation_amount,
            donor_name=donor_name
        )