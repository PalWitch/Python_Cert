import json
import os

from models import Ticket


class JsonSpeicher:
    def __init__(self, dateipfad):
        self.dateipfad = dateipfad

    def speichern(self, tickets):
        os.makedirs(os.path.dirname(self.dateipfad), exist_ok=True)

        daten = [ticket.to_dict() for ticket in tickets]

        with open(self.dateipfad, "w", encoding="utf-8") as datei:
            json.dump(daten, datei, ensure_ascii=False, indent=4)

    def laden(self):
        if not os.path.exists(self.dateipfad):
            return []

        with open(self.dateipfad, "r", encoding="utf-8") as datei:
            daten = json.load(datei)

        return [Ticket.from_dict(eintrag) for eintrag in daten]