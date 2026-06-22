class TicketFehler(Exception):
    """Basisklasse für alle Ticket-System-Fehler."""
    pass


class TicketNichtGefundenFehler(TicketFehler):
    """Wird geworfen, wenn ein Ticket nicht gefunden wurde."""
    pass


class UngueltigerStatuswechselFehler(TicketFehler):
    """Wird geworfen, wenn ein Statuswechsel nicht erlaubt ist."""
    pass