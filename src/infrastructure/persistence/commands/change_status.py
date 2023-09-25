from src.domain.ticket.ticket_state import TicketState

from src.utils.execute_command import execute_command

def change_status(ticket_uuid: str, new_state: TicketState) -> None:
    """ Changes the status of ticket with uuid "ticket_id" to "new_state" 
    """
    execute_command(f"""
                    UPDATE Ticket
                    SET State = '{new_state.value}'
                    WHERE UUID = {ticket_uuid}
                    """)