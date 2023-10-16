from typing import List

from pyodbc import Row 


from src.application.read_model.collector import CollectorData
from src.application.read_model.ticket import TicketData, TicketState

def deserialize_collector(collector_raw_data, tickets: List[TicketData]) -> CollectorData:
    return CollectorData(
        id=collector_raw_data[0],
        uuid=collector_raw_data[1],
        username=collector_raw_data[2],
        password=collector_raw_data[3],
        manager_id=collector_raw_data[4],
        fullname=collector_raw_data[5],
        zone=collector_raw_data[6],
        tickets=tickets
    )