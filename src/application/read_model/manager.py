from dataclasses import dataclass
from typing import List

from .collector import CollectorData
from .ticket import TicketData


@dataclass(frozen=True)
class ManagerData:
    id: int
    uuid: str
    username: str
    password: str
    fullname: str
    tickets: List[TicketData]
    collectors: List[CollectorData]
