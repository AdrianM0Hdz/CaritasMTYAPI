from pyodbc import Row 

from src.application.read_model.ticket import TicketData, TicketState

def deserialize_ticket(ticket_raw_data) -> TicketData:   
    return TicketData(
        id=ticket_raw_data[0],
        manager_id=ticket_raw_data[1],
        collector_id=ticket_raw_data[2],
        housing_reference=ticket_raw_data[3],
        receipt_comments=ticket_raw_data[4],
        reprogramation_comments=ticket_raw_data[5],
        house_phone_number=ticket_raw_data[6],
        cellphone=ticket_raw_data[7],
        state=TicketState(ticket_raw_data[8]),
        date=ticket_raw_data[9],
        collector_comments=ticket_raw_data[10]
    )