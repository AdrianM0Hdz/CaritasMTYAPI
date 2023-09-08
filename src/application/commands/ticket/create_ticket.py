import datetime

from src.domain.ticket import Ticket
from src.infrastructure.persistence.ticket_repo import TicketRepository

def create_ticket(
        id: str,
        housing_reference: str, 
        receipt_comments: str, 
        reprogramation_comments: str, 
        house_phone_number: str, 
        cellphone: str, 
        manager_id: str, 
        collector_id: str,
        date: str, 
        collector_comments: str 
) -> str:
    """ Creates a ticket in the database and returns the id of the created ticket
    """
    raw_date = date.split("-")
    date_obj = datetime.date(
        year=int(raw_date[0]), 
        month=int(raw_date[1]), 
        day=int(raw_date[2])
    )
    
    ticket = Ticket.create_new(
        id=id,
        housing_reference=housing_reference, 
        receipt_comments=receipt_comments, 
        reprogramation_comments=reprogramation_comments, 
        house_phone_number=house_phone_number, 
        cellphone=cellphone, 
        manager_id=manager_id, 
        collector_id=collector_id,
        date=date_obj, 
        collector_comments=collector_comments
    )
    
    ticket_repo = TicketRepository() 
    ticket_id = ticket_repo.insert(ticket)
    return ticket_id
