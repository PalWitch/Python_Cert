from models import Kunde, SupportMitarbeiter
from service import TicketSystem
from storage import JsonSpeicher
from exceptions import TicketFehler


def introspektion_anzeigen():
    from models import Ticket, BugTicket

    print("Introspection-Demo")
    print("Klassenname:", Ticket.__name__)
    print("Basisklassen von BugTicket:", BugTicket.__bases__)
    print("Attribute von Ticket:", list(Ticket.__dict__.keys())[:10])


def demo():
    speicher = JsonSpeicher("data/tickets.json")
    system = TicketSystem(speicher)

    kunde = Kunde("Hannah", "mueller@beispiel.de", "K-100")
    support = SupportMitarbeiter("Ada", "ada@example.de", "First Level")

    ticket1 = system.ticket_erstellen(
        "Login kaputt",
        "User kann sich nicht einloggen",
        ersteller=kunde,
        ticket_typ="bug",
        zustaendig=support
    )

    ticket2 = system.ticket_erstellen(
        "Dark Mode",
        "Bitte dunkles Design ergänzen",
        ersteller=kunde,
        ticket_typ="feature"
    )

    system.kommentar_hinzufuegen(ticket1.id, "Ada", "Ich prüfe das Problem.")
    system.status_aendern(ticket1.id, "in_progress", "Ada")
    system.status_aendern(ticket1.id, "resolved", "Ada")

    print(ticket1)
    print("Anzahl Kommentare:", len(ticket1))

    print("\nNach Priorität sortiert:")
    for ticket in system.tickets_nach_prioritaet():
        print(ticket)

    print("\nReport:")
    print(system.report_erzeugen())

    print("\nObjekt-Dictionary:")
    print(ticket1.__dict__)

    system.speichern()

    neues_system = TicketSystem(speicher)
    neues_system.laden()

    print("\nGeladene Tickets:")
    for ticket in neues_system.tickets:
        print(ticket)


if __name__ == "__main__":
    introspektion_anzeigen()

    try:
        demo()
    except TicketFehler as fehler:
        print("Fehler:", fehler)