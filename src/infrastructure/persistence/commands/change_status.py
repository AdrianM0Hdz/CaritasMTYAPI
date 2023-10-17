from src.domain.ticket.ticket_state import TicketState

from src.utils.execute_command import execute_command

def change_status(ticket_id: int, new_state: TicketState) -> None:
    """ Changes the status of ticket with uuid "ticket_id" to "new_state" 
    """

    command = f"""
                UPDATE Ticket
                SET State = ?
                WHERE ID = ?;
                """
    
    params = [new_state.value, ticket_id]

    execute_command(command, params)