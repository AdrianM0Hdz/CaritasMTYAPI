from uuid import uuid1
from dataclasses import dataclass
import datetime
from typing import List

from .ticket_state import TicketState

@dataclass
class Ticket:
    id: str
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

    @classmethod
    def create_new(cls, 
                   id: str,
                   housing_reference: str, 
                   receipt_comments: str, 
                   reprogramation_comments: str, 
                   house_phone_number: str, 
                   cellphone: str, 
                   manager_id: str, 
                   collector_id: str,
                   date: datetime.date, 
                   collector_comments: str): 
        return cls(
            id=id,
            housing_reference=housing_reference, 
            receipt_comments=receipt_comments, 
            reprogramation_comments=reprogramation_comments,
            house_phone_number=house_phone_number, 
            cellphone=cellphone, 
            manager_id=manager_id, 
            collector_id=collector_id, 
            state=TicketState.PENDING, 
            date=date, 
            collector_comments=collector_comments
        )