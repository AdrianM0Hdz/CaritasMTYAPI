from src.application.read_model.ticket import TicketData

def serialize_ticket_to_json(ticket: TicketData) -> dict:
    return {
        "uuid": ticket.uuid,
        "housingReference": ticket.housing_reference,
        "receiptComments": ticket.receipt_comments,
        "reprogramationComments": ticket.reprogramation_comments,
        "housePhoneNumber": ticket.house_phone_number,
        "cellPhone": ticket.cellphone,
        "managerId": ticket.manager_id,
        "collectorId": ticket.collector_id,
        "state": ticket.state.value,
        "date": str(ticket.date),
        "collectorComments": ticket.collector_comments,
        "donationAmount": ticket.donation_amount,
        "donorName": ticket.donor_name
    }