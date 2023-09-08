import os
from dotenv import load_dotenv
load_dotenv(override=True)

from uuid import uuid1

from src.domain.ticket import Ticket
from src.domain.ticket.ticket_state import TicketState

from src.infrastructure.persistence.ticket_repo import TicketRepository

ticket_repo = TicketRepository()

t = Ticket(id=str(uuid1()), 
           housing_reference="dummy", 
           receipt_comments="dummy", 
           reprogramation_comments="dummy", 
           house_phone_number="dummy", 
           cellphone="dummy", 
           manager_id="1", 
           collector_id="1", 
           state=TicketState.PENDING, 
           date="2023-01-01", 
           collector_comments="dummty")
print(
ticket_repo.get("250479a4-4e62-11ee-9f3e-04ea56b5cbe1")
)