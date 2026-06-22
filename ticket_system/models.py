from datetime import datetime


class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def rolle(self):
        return "Person"

    def to_dict(self):
        return {
            "klasse": self.__class__.__name__,
            "name": self.name,
            "email": self.email
        }

    @staticmethod
    def from_dict(daten):
        klassenname = daten.get("klasse")

        if klassenname == "Kunde":
            return Kunde(daten["name"], daten["email"], daten.get("kundennummer"))
        if klassenname == "SupportMitarbeiter":
            return SupportMitarbeiter(daten["name"], daten["email"], daten.get("team"))
        return Person(daten["name"], daten["email"])

    def __str__(self):
        return f"{self.rolle()}: {self.name} <{self.email}>"


class Kunde(Person):
    def __init__(self, name, email, kundennummer):
        super().__init__(name, email)
        self.kundennummer = kundennummer

    def rolle(self):
        return "Kunde"

    def to_dict(self):
        daten = super().to_dict()
        daten["kundennummer"] = self.kundennummer
        return daten


class SupportMitarbeiter(Person):
    def __init__(self, name, email, team):
        super().__init__(name, email)
        self.team = team

    def rolle(self):
        return "Support"

    def to_dict(self):
        daten = super().to_dict()
        daten["team"] = self.team
        return daten


class Kommentar:
    def __init__(self, autor, text, erstellt_am=None):
        self.autor = autor
        self.text = text
        self.erstellt_am = erstellt_am or datetime.now().isoformat(timespec="seconds")

    def to_dict(self):
        return {
            "autor": self.autor,
            "text": self.text,
            "erstellt_am": self.erstellt_am
        }

    @staticmethod
    def from_dict(daten):
        return Kommentar(
            daten["autor"],
            daten["text"],
            daten.get("erstellt_am")
        )

    def __str__(self):
        return f"[{self.erstellt_am}] {self.autor}: {self.text}"


class StatusAenderung:
    def __init__(self, alter_status, neuer_status, geaendert_von, zeitpunkt=None):
        self.alter_status = alter_status
        self.neuer_status = neuer_status
        self.geaendert_von = geaendert_von
        self.zeitpunkt = zeitpunkt or datetime.now().isoformat(timespec="seconds")

    def to_dict(self):
        return {
            "alter_status": self.alter_status,
            "neuer_status": self.neuer_status,
            "geaendert_von": self.geaendert_von,
            "zeitpunkt": self.zeitpunkt
        }

    @staticmethod
    def from_dict(daten):
        return StatusAenderung(
            daten["alter_status"],
            daten["neuer_status"],
            daten["geaendert_von"],
            daten.get("zeitpunkt")
        )

    def __str__(self):
        return f"{self.alter_status} -> {self.neuer_status} durch {self.geaendert_von} am {self.zeitpunkt}"


class Ticket:
    naechste_nummer = 1000

    erlaubte_statuswechsel = {
        "open": ["in_progress"],
        "in_progress": ["resolved"],
        "resolved": ["closed"],
        "closed": []
    }

    def __init__(self, titel, beschreibung, ersteller, zustaendig=None,
                 ticket_id=None, status="open", prioritaet=None,
                 erstellt_am=None, aktualisiert_am=None,
                 kommentare=None, statushistorie=None):
        if ticket_id is None:
            Ticket.naechste_nummer += 1
            self.id = f"T-{Ticket.naechste_nummer}"
        else:
            self.id = ticket_id

        self.titel = titel
        self.beschreibung = beschreibung
        self.ersteller = ersteller
        self.zustaendig = zustaendig
        self.status = status
        self._prioritaet = prioritaet if prioritaet is not None else self.berechne_prioritaet()
        self.erstellt_am = erstellt_am or datetime.now().isoformat(timespec="seconds")
        self.aktualisiert_am = aktualisiert_am or self.erstellt_am
        self.kommentare = kommentare or []
        self.statushistorie = statushistorie or []

    @property
    def prioritaet(self):
        return self._prioritaet

    def berechne_prioritaet(self):
        return 2

    def typ(self):
        return "allgemein"

    def kommentar_hinzufuegen(self, autor, text):
        kommentar = Kommentar(autor, text)
        self.kommentare.append(kommentar)
        self.aktualisiert_am = datetime.now().isoformat(timespec="seconds")
        return kommentar

    def status_aendern(self, neuer_status, geaendert_von):
        erlaubte_ziele = self.erlaubte_statuswechsel.get(self.status, [])
        if neuer_status not in erlaubte_ziele:
            from exceptions import UngueltigerStatuswechselFehler
            raise UngueltigerStatuswechselFehler(
                f"Statuswechsel von '{self.status}' zu '{neuer_status}' ist nicht erlaubt."
            )

        eintrag = StatusAenderung(self.status, neuer_status, geaendert_von)
        self.statushistorie.append(eintrag)
        self.status = neuer_status
        self.aktualisiert_am = datetime.now().isoformat(timespec="seconds")

    def zusammenfassung(self):
        return f"{self.id} | {self.typ()} | {self.status} | Priorität {self.prioritaet} | {self.titel}"

    def to_dict(self):
        return {
            "klasse": self.__class__.__name__,
            "id": self.id,
            "titel": self.titel,
            "beschreibung": self.beschreibung,
            "status": self.status,
            "prioritaet": self.prioritaet,
            "typ": self.typ(),
            "ersteller": self.ersteller.to_dict() if self.ersteller else None,
            "zustaendig": self.zustaendig.to_dict() if self.zustaendig else None,
            "erstellt_am": self.erstellt_am,
            "aktualisiert_am": self.aktualisiert_am,
            "kommentare": [kommentar.to_dict() for kommentar in self.kommentare],
            "statushistorie": [eintrag.to_dict() for eintrag in self.statushistorie]
        }

    @staticmethod
    def from_dict(daten):
        klassenname = daten.get("klasse", "Ticket")

        klassen = {
            "Ticket": Ticket,
            "BugTicket": BugTicket,
            "FeatureAnfrage": FeatureAnfrage,
            "SupportAnfrage": SupportAnfrage
        }

        klasse = klassen.get(klassenname, Ticket)

        ticket = klasse(
            titel=daten["titel"],
            beschreibung=daten["beschreibung"],
            ersteller=Person.from_dict(daten["ersteller"]) if daten.get("ersteller") else None,
            zustaendig=Person.from_dict(daten["zustaendig"]) if daten.get("zustaendig") else None,
            ticket_id=daten["id"],
            status=daten["status"],
            prioritaet=daten["prioritaet"],
            erstellt_am=daten.get("erstellt_am"),
            aktualisiert_am=daten.get("aktualisiert_am"),
            kommentare=[Kommentar.from_dict(k) for k in daten.get("kommentare", [])],
            statushistorie=[StatusAenderung.from_dict(s) for s in daten.get("statushistorie", [])]
        )
        return ticket

    def __str__(self):
        return self.zusammenfassung()

    def __len__(self):
        return len(self.kommentare)

    def __lt__(self, anderes_ticket):
        return self.prioritaet < anderes_ticket.prioritaet


class BugTicket(Ticket):
    def typ(self):
        return "bug"

    def berechne_prioritaet(self):
        return 1


class FeatureAnfrage(Ticket):
    def typ(self):
        return "feature"

    def berechne_prioritaet(self):
        return 3

    def zusammenfassung(self):
        return f"{self.id} | FEATURE | {self.status} | Wunsch: {self.titel}"


class SupportAnfrage(Ticket):
    def typ(self):
        return "support"

    def berechne_prioritaet(self):
        return 2