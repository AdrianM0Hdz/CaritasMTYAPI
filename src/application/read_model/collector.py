from dataclasses import dataclass
from typing import List

from .ticket import TicketData


@dataclass(frozen=True)
class CollectorData:
    id: str
    username: str
    password: str
    fullname: str
    manager_id: str
    tickets: List[TicketData]
