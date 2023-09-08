import os
from dotenv import load_dotenv
load_dotenv(override=True)

from uuid import uuid1
from datetime import date

from src.domain.ticket import Ticket
from src.domain.ticket.ticket_state import TicketState

from src.application.commands.ticket.create_ticket import create_ticket

from src.infrastructure.persistence.ticket_repo import TicketRepository

ticket_repo = TicketRepository()

tid = create_ticket(
    id=str(uuid1()), 
    housing_reference="dummy", 
    receipt_comments="dummy", 
    reprogramation_comments="dummy", 
    house_phone_number="dummy", 
    cellphone="dummy", 
    manager_id="1", 
    collector_id="1", 
    date="1000-12-12", 
    collector_comments="dummty"
)

print(tid)