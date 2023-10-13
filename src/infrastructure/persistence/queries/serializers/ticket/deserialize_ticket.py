from pyodbc import Row 

from src.application.read_model.ticket import TicketData, TicketState

def deserialize_ticket(ticket_raw_data) -> TicketData:   
    return TicketData(
        id=ticket_raw_data[0],
        uuid=ticket_raw_data[1],
        manager_id=ticket_raw_data[2],
        collector_id=ticket_raw_data[3],
        housing_reference=ticket_raw_data[4],
        street=ticket_raw_data[5],
        house_number=ticket_raw_data[6],
        municipality=ticket_raw_data[7],
        suburb=ticket_raw_data[8],
        receipt_comments=ticket_raw_data[9],
        reprogramation_comments=ticket_raw_data[10],
        house_phone_number=ticket_raw_data[11],
        cellphone=ticket_raw_data[12],
        state=TicketState(ticket_raw_data[13]),
        date=ticket_raw_data[14],
        collector_comments=ticket_raw_data[15],
        donation_amount=ticket_raw_data[16],
        donor_name=ticket_raw_data[17]
    )