from src.utils.execute_command import execute_command

def change_collector_comments(ticket_id: int, collector_comments: str) -> None:
    """ Changes the collector comments of ticket with id "ticket_id" to "collector_comments" 
    """
    execute_command(f"""
                    UPDATE Ticket
                    SET CollectorComments = '{collector_comments}'
                    WHERE ID = {ticket_id}
                    """)