from models import Ticket, BugTicket, FeatureAnfrage, SupportAnfrage
from exceptions import TicketNichtGefundenFehler


class TicketSystem:
    def __init__(self, speicher=None):
        self.tickets = []
        self.speicher = speicher

    def ticket_erstellen(self, titel, beschreibung, ersteller,
                         ticket_typ="allgemein", zustaendig=None):
        klassen = {
            "allgemein": Ticket,
            "bug": BugTicket,
            "feature": FeatureAnfrage,
            "support": SupportAnfrage
        }

        klasse = klassen.get(ticket_typ, Ticket)
        ticket = klasse(titel, beschreibung, ersteller, zustaendig)
        self.tickets.append(ticket)
        return ticket

    def ticket_nach_id(self, ticket_id):
        for ticket in self.tickets:
            if ticket.id == ticket_id:
                return ticket
        raise TicketNichtGefundenFehler(f"Ticket mit ID {ticket_id} wurde nicht gefunden.")

    def kommentar_hinzufuegen(self, ticket_id, autor, text):
        ticket = self.ticket_nach_id(ticket_id)
        return ticket.kommentar_hinzufuegen(autor, text)

    def status_aendern(self, ticket_id, neuer_status, geaendert_von):
        ticket = self.ticket_nach_id(ticket_id)
        ticket.status_aendern(neuer_status, geaendert_von)
        return ticket

    def tickets_nach_status(self, status):
        return [ticket for ticket in self.tickets if ticket.status == status]

    def tickets_nach_prioritaet(self):
        return sorted(self.tickets)

    def report_erzeugen(self):
        report = {
            "gesamt": len(self.tickets),
            "offen": len(self.tickets_nach_status("open")),
            "in_bearbeitung": len(self.tickets_nach_status("in_progress")),
            "geloest": len(self.tickets_nach_status("resolved")),
            "geschlossen": len(self.tickets_nach_status("closed")),
            "kritisch": len([ticket for ticket in self.tickets if ticket.prioritaet == 1])
        }
        return report

    def speichern(self):
        if self.speicher is not None:
            self.speicher.speichern(self.tickets)

    def laden(self):
        if self.speicher is not None:
            self.tickets = self.speicher.laden()