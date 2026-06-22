# Ticket-System Backend

Dieses Projekt ist ein kleines Ticket-System-Backends in Python.
Der Fokus liegt auf sauberer Objektorientierung, klarer Trennung der Verantwortlichkeiten und einer Struktur, die später leicht durch eine CLI oder eine Streamlit-Oberfläche erweitert werden kann.

## Projektidee

Das System verwaltet Tickets für verschiedene Zwecke:

- Fehler (`BugTicket`)
- Feature-Wünsche (`FeatureAnfrage`)
- Support-Anfragen (`SupportAnfrage`)

Zu jedem Ticket können Kommentare und Statusänderungen gespeichert werden.
Zusätzlich können Tickets gefiltert, sortiert, gespeichert, geladen und in einem einfachen Report zusammengefasst werden.

## Architektur

Das Projekt ist bewusst in mehrere Dateien aufgeteilt:

```text
ticket_system/
├── main.py          # Demo-Ablauf / Einstiegspunkt
├── models.py        # Datenmodelle und Objektverhalten
├── service.py       # Geschäftslogik
├── storage.py       # JSON-Speicherung
├── exceptions.py    # Eigene Exception-Klassen
└── data/
    └── tickets.json
```

Diese Trennung ist wichtig, damit die Fachlogik unabhängig von einer Oberfläche bleibt.
Eine spätere CLI oder Streamlit-App soll nur Methoden des Backends aufrufen.

## OOP-Anforderungen

Die Lösung erfüllt die typischen Anforderungen der Aufgabe:

- mindestens 7 eigene Klassen
- Konstruktoren mit `__init__`
- Vererbung durch Personen- und Ticket-Hierarchien
- Overriding durch überschriebenes Verhalten in Unterklassen
- Polymorphismus über gemeinsame Methoden verschiedener Ticketarten
- Komposition durch Kommentare und Statushistorie in Tickets
- Klassenattribut mit `naechste_nummer`
- Kapselung mit `_prioritaet`
- Magic Methods: `__str__`, `__len__`, `__lt__`
- Introspection mit `__dict__`, `__name__`, `__bases__`
- eigene Exceptions
- Datei-I/O mit JSON

## Klassenüberblick

### Personen

- `Person`: Basisklasse für Personen im System
- `Kunde`: Spezialisierung für Kunden
- `SupportMitarbeiter`: Spezialisierung für Support-Personal

### Ticketdaten

- `Kommentar`: Einzelner Kommentar mit Autor, Text und Zeitpunkt
- `StatusAenderung`: Historieneintrag für Statuswechsel

### Tickets

- `Ticket`: Allgemeine Basisklasse
- `BugTicket`: Hohe Priorität
- `FeatureAnfrage`: Niedrigere Priorität, eigene Zusammenfassung
- `SupportAnfrage`: Standard-Priorität

### Verwaltung und Persistenz

- `TicketSystem`: zentrale Geschäftslogik
- `JsonSpeicher`: Speichern und Laden über JSON-Dateien

### Fehlerklassen

- `TicketFehler`: allgemeine Basisklasse für fachliche Fehler
- `TicketNichtGefundenFehler`: Ticket-ID nicht gefunden
- `UngueltigerStatuswechselFehler`: nicht erlaubter Statuswechsel

## Startanleitung

1. In den Projektordner wechseln.
2. Das Programm ausführen:

```bash
python main.py
```

## Beispielablauf

Der Demo-Ablauf in `main.py` zeigt folgende Schritte:

1. Introspection mit `__name__`, `__bases__` und `__dict__`
2. Erstellen von Personenobjekten
3. Erstellen mehrerer Ticketarten
4. Hinzufügen von Kommentaren
5. Ändern von Statuswerten
6. Filtern nach Status
7. Sortieren nach Priorität
8. Erzeugen eines Reports
9. Speichern in JSON
10. Laden aus JSON

## Speicherformat

Die Tickets werden als Liste von Dictionaries gespeichert.
Jedes Ticket enthält unter anderem:

- `id`
- `titel`
- `beschreibung`
- `status`
- `prioritaet`
- `ersteller`
- `zustaendig`
- `kommentare`
- `statushistorie`

Die Umwandlung erfolgt über `to_dict()` und `from_dict()`.

## Frontendfähigkeit

Die Architektur ist backend-first aufgebaut:

- keine direkte Nutzung von `input()` in den Fachklassen
- keine Abhängigkeit zu Streamlit
- Methoden geben Werte zurück
- Speicherlogik ist ausgelagert

Dadurch eignet sich das Projekt gut als Grundlage für eine spätere Benutzeroberfläche.

## Hinweis zur Ausgabe

Diese Version enthält bewusst viele deutsche Kommentare und Docstrings,
weil sie nicht nur funktionieren, sondern auch als gut lesbare Lehrgrundlage dienen soll.