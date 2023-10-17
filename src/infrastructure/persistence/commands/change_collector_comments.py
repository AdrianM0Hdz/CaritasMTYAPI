from src.utils.execute_command import execute_command

def change_collector_comments(ticket_id: int, collector_comments: str) -> None:
    """ Changes the collector comments of ticket with id "ticket_id" to "collector_comments" 
    """
    command = f"""
                UPDATE Ticket
                SET CollectorComments = ?
                WHERE ID = ?
                """
    params = [collector_comments, ticket_id]

    execute_command(command, params)