# Ein einfaches Mixin

class JsonMixin:
    def to_dict(self):
        """Konvertiert die Attribute des Objekts in ein Dictionary."""
        return self.__dict__

class Book(JsonMixin):
    def __init__(self, title, author):
        self.title = title
        self.author = author


        # Test des Codes
book = Book("Python", "Ada")
print(book.to_dict())


# Fehlmodellierung korrigieren

class Logger:
    def log(self, message):
        print(f"LOG: {message}")


class Order:
    def __init__(self, number, logger: Logger):
        self.number = number
        self.logger = logger  # Komposition statt Vererbung

    def confirm(self):
        self.logger.log(f"Bestellung {self.number} bestätigt")

logger = Logger()
order = Order(42, logger)
order.confirm()

# Austauschbares Verhalten mit Komposition

from typing import Protocol


        # 1. Definition des Interfaces (Protokolls)
class Sender(Protocol):
    def send(self, text: str) -> None:
        ...


        # 2. Implementierung der konkreten Sender
class EmailSender:
    def send(self, text: str) -> None:
        print(f"E-Mail gesendet: {text}")


class ConsoleSender:
    def send(self, text: str) -> None:
        print(f"Konsole: {text}")


        # 3. NotificationService mit Dependency Injection
class NotificationService:
    def __init__(self, sender: Sender):
        self.sender = sender  # Initialer Sender

    def notify(self, text: str) -> None:
        self.sender.send(text)  # Delegation an den Sender


        # --- Demonstration der Laufzeit-Änderung ---

        # Start mit dem ConsoleSender
service = NotificationService(ConsoleSender())
service.notify("System gestartet")

        # 4. Tausch des Senders zur Laufzeit
service.sender = EmailSender()
service.notify("Kritischer Fehler aufgetreten")

# Mixin für kurze Objektinfos
class InfoMixin:
    """Ein Mixin, das Klassen eine standardisierte info()-Methode bereitstellt."""
    
    def info(self) -> str:
        # self.__class__.__name__ holt dynamisch den Namen der aktuellen Klasse
        # self.__dict__ liefert alle Attribute des Objekts als Dictionary
        return f"Klasse: {self.__class__.__name__} | Daten: {self.__dict__}"


        # Anwendung in der ersten Klasse
class Book(InfoMixin):
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = price


        # Anwendung in der zweiten Klasse (mit völlig anderen Attributen)
class Product(InfoMixin):
    def __init__(self, product_id: int, name: str, stock: int):
        self.product_id = product_id
        self.name = name
        self.stock = stock


        # --- Test der Klassen ---
if __name__ == "__main__":
        # Instanziierung der Objekte
    book = Book("Der alte Mann und das Meer", "Ernest Hemingway", 9.99)
    product = Product(4201, "Wireless Mouse", 150)

    