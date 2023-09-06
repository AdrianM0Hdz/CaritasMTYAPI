from enum import Enum


class TicketState(Enum):
    PENDING = "PENDING"
    COLLECTED = "COLLECTED"
    CONFLICT = "CONFLICT"
    FINALIZED = "FINALIZED"