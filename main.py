import os
from dotenv import load_dotenv
load_dotenv(override=True)

from uuid import uuid1
from datetime import date

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
           date=date(year=1000, month=12, day=12), 
           collector_comments="dummty")

ticket_repo.insert(t)