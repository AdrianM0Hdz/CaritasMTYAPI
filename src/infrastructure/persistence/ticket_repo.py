import os

import pyodbc 

from src.utils import execute_command, execute_query

from src.domain.ticket import Ticket
from src.domain.ticket.ticket_state import TicketState

class TicketRepository:

    def insert(self, item: Ticket) -> str:    
        command=f""" INSERT INTO 
                     Ticket (UUID, 
                             ManagerID, 
                             CollectorID, 
                             HousingReference, 
                             Street,
                             HouseNumber,
                             Municipality,
                             Suburb,
                             ReceiptComments, 
                             ReprogrammationComments, 
                             HousePhoneNumber, 
                             Cellphone, 
                             State, 
                             TicketDate, 
                             CollectorComments) 
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        
        params = [item.uuid, item.manager_id, item.collector_id, item.housing_reference, item.street, \
                  item.house_number, item.municipality, item.suburb, item.receipt_comments, \
                  item.reprogramation_comments, item.house_phone_number, item.cellphone, item.state.value, \
                  str(item.date), item.collector_comments]
        execute_command(command, params)
        return item.id

    def get(self, id: int) -> Ticket:
        query = f"SELECT * FROM Ticket WHERE ID=?"
        params = [id]
        raw_data = execute_query(query, params)
        if len(raw_data) > 1:
            raise Exception("more than one item fetched")
        if len(raw_data) == 0:
            raise Exception("no ticket with that id found")
        item_row = raw_data[0]
        return Ticket(
            id=item_row[0],
            uuid=item_row[1],
            manager_id=item_row[2],
            collector_id=item_row[3],
            housing_reference=item_row[4],
            street=item_row[5],
            house_number=item_row[6],
            municipality=item_row[7],
            suburb=item_row[8],
            receipt_comments=item_row[9],
            reprogramation_comments=item_row[10],
            house_phone_number=item_row[11],
            cellphone=item_row[12],
            state=TicketState(item_row[13]),
            date=item_row[14],
            collector_comments=item_row[15],
            donation_amount=item_row[16],
            donor_name=item_row[17]
        )

    def commit(self, item: Ticket):
        command = f"""UPDATE Ticket SET
                      ID=?, 
                      ManagerID=?, 
                      CollectorID=?, 
                      HousingReference=?, 
                      ReceiptComments=?, 
                      ReprogrammationComments=?, 
                      HousePhoneNumber=?, 
                      Cellphone=?, 
                      State=?, 
                      TicketDate=?, 
                      CollectorComments=?
                      WHERE ID=?;"""
        
        params = [item.id, item.manager_id, item.collector_id, item.housing_reference, \
                  item.receipt_comments, item.reprogramation_comments, item.house_phone_number, \
                  item.cellphone, item.state, item.date, item.collector_comments,item.id]
        execute_command(command, params)
