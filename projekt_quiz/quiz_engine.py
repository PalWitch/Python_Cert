from typing import List, Dict, Any
import random

Frage = Dict[str, Any]
Ergebnis = Dict[str, Any]

FARBE_GRUEN = "\033[92m"
FARBE_ROT = "\033[91m"
FARBE_GELB = "\033[93m"
FARBE_ZURUECK = "\033[0m"


def gruener_text(text: str) -> str:
    return f"{FARBE_GRUEN}{text}{FARBE_ZURUECK}"


def roter_text(text: str) -> str:
    return f"{FARBE_ROT}{text}{FARBE_ZURUECK}"


def gelber_text(text: str) -> str:
    return f"{FARBE_GELB}{text}{FARBE_ZURUECK}"


def verfuegbare_kategorien(fragen_liste: List[Frage]) -> List[str]:
    """
    Gibt eine Liste einzigartiger Kategorien zurück.
    """
    kategorien: List[str] = []
    for frage in fragen_liste:
        kat = frage["kategorie"]
        if kat not in kategorien:
            kategorien.append(kat)
    return kategorien

def quiz_nach_kategorie(
    alle_fragen: List[Frage], alle_ergebnisse: List[Ergebnis]
) -> None:
    """
    Lässt den Benutzer eine Kategorie wählen und startet dann ein Quiz
    nur mit Fragen aus dieser Kategorie.
    """
    kategorien = verfuegbare_kategorien(alle_fragen)

    if not kategorien:
        print("Es sind keine Kategorien vorhanden.")
        return

    print("\nVerfügbare Kategorien:")
    for index, kat in enumerate(kategorien, start=1):
        print(f"{index}) {kat}")

    while True:
        eingabe = input("Bitte wähle eine Kategorie (Nummer): ")

        try:
            nummer = int(eingabe)
        except ValueError:
            print("Bitte gib eine Zahl ein.")
            continue

        if nummer < 1 or nummer > len(kategorien):
            print("Diese Kategorie gibt es nicht.")
            continue

        ausgewaehlte_kategorie = kategorien[nummer - 1]
        break

    # Fragen filtern
    gefilterte_fragen = [
        frage for frage in alle_fragen if frage["kategorie"] == ausgewaehlte_kategorie
    ]

    if not gefilterte_fragen:
        print("Für diese Kategorie gibt es keine Fragen.")
        return

    print(f"\nStarte Quiz für Kategorie: {ausgewaehlte_kategorie}")
    ergebnis = run_quiz(gefilterte_fragen)
    alle_ergebnisse.append(ergebnis)
    zeige_ergebnis(ergebnis)


def quiz_nach_schwierigkeit(
    alle_fragen: List[Frage], alle_ergebnisse: List[Ergebnis]
) -> None:
    """
    Lässt den Benutzer eine Schwierigkeitsstufe wählen und startet dann
    ein Quiz nur mit Fragen dieser Schwierigkeit (oder darüber).
    """
    print("\nSchwierigkeitsstufen:")
    print("1) Nur einfache Fragen (Schwierigkeit = 1)")
    print("2) Mittel und schwer (Schwierigkeit >= 2)")

    while True:
        eingabe = input("Bitte wähle eine Option (1-2): ")

        if eingabe == "1":
            min_schwierigkeit = 1
            max_schwierigkeit = 1
            break
        elif eingabe == "2":
            min_schwierigkeit = 2
            max_schwierigkeit = 999  # praktisch „alle höheren“
            break
        else:
            print("Ungültige Eingabe. Bitte 1 oder 2 wählen.")

    gefilterte_fragen: List[Frage] = []
    for frage in alle_fragen:
        level = frage["schwierigkeit"]
        if min_schwierigkeit <= level <= max_schwierigkeit:
            gefilterte_fragen.append(frage)

    if not gefilterte_fragen:
        print("Für diese Schwierigkeitsstufe gibt es keine Fragen.")
        return

    print("\nStarte Quiz mit gefilterten Fragen nach Schwierigkeit.")
    ergebnis = run_quiz(gefilterte_fragen)  # Tippfehler selbst korrigieren :)
    alle_ergebnisse.append(ergebnis)
    zeige_ergebnis(ergebnis)

def zeige_frage(frage: Frage, nummer: int, gesamt_anzahl: int) -> None:
    """
    Zeigt eine einzelne Frage mit Nummer und Antwortoptionen an.
    """
    print("\n" + "-" * 40)
    print(f"Frage {nummer} von {gesamt_anzahl}")
    print(frage["frage"])

    # Antwortoptionen anzeigen, nummeriert ab 1
    for index, antwort_text in enumerate(frage["antworten"], start=1):
        print(f"{index}) {antwort_text}")


def antwort_spieler(frage: Frage) -> int:
    """
    Liest eine Antwort vom Benutzer ein und validiert die Eingabe.

    Nur Zahlen im gültigen Bereich sind erlaubt.
    Zusätzlich: Eingabe 'q' bricht das Quiz ab.
    """
    anzahl_optionen = len(frage["antworten"])

    while True:
        benutzer_eingabe = input(
            "Bitte gib die Nummer deiner Antwort ein (oder 'q' für Abbruch): "
        )
        # Möglichkeit zum Abbrechen
        if benutzer_eingabe.strip().lower() == "q":
            # Wir benutzen -1 als Signal für 'Abbruch'
            return -1

        try:
            antwort_nummer = int(benutzer_eingabe)
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine Zahl ein (z.B. 1, 2, 3, 4).")
            continue

        if antwort_nummer < 1 or antwort_nummer > anzahl_optionen:
            print("Diese Nummer gibt es nicht. Bitte versuche es erneut.")
            continue

        ausgewaehlter_index = antwort_nummer - 1
        return ausgewaehlter_index


def antwort_check(gegebene_antwort: int, frage: Frage) -> bool:
    """
    Prüft, ob der gegebene Antwort-Index mit antworten_richtig übereinstimmt.
    """
    richtige_antwort = frage["antworten_richtig"]
    ist_richtig = gegebene_antwort == richtige_antwort
    return ist_richtig


def run_quiz(fragen_liste: List[Frage]) -> Ergebnis:
    """
    Führt ein komplettes Quiz mit den gegebenen Fragen durch.
    """
    fragen_kopie = fragen_liste.copy()
    random.shuffle(fragen_kopie)

    gesamt_anzahl_fragen = len(fragen_kopie)
    punktestand = 0

    # Liste für Details jeder Frage (für Statistik)
    detail_liste: List[Dict[str, Any]] = []

    for laufende_nummer, frage in enumerate(fragen_kopie, start=1):
        zeige_frage(frage, laufende_nummer, gesamt_anzahl_fragen)

        gegebener_index = antwort_spieler(frage)

        # Prüfen, ob der Benutzer abbrechen möchte
        if gegebener_index == -1:
            print("\nQuiz wurde von dir abgebrochen.")
            break

        ist_richtig = antwort_check(gegebener_index, frage)

        if ist_richtig:
            print(gruener_text("Richtig! ✓"))
            punktestand += 1
        else:
            print(roter_text("Falsch. ✗"))
            richtige_index = frage["antworten_richtig"]
            richtige_antwort = frage["antworten"][richtige_index]
            print(
                gruener_text(
                    f"Richtige Antwort: {richtige_index + 1}) {richtige_antwort}"
                )
            )
            print(gelber_text(f"Erklärung: {frage['erklaerung']}"))

        detail_liste.append(
            {
                "frage_text": frage["frage"],
                "kategorie": frage["kategorie"],
                "schwierigkeit": frage["schwierigkeit"],
                "ist_richtig": ist_richtig,
            }
        )

    ergebnis: Ergebnis = {
        "anzahl_fragen": gesamt_anzahl_fragen,
        "punkte": punktestand,
        "details": detail_liste,
    }

    return ergebnis


def zeige_ergebnis(results: Ergebnis) -> None:
    """
    Zeigt die Ergebnisse des Quiz an, inkl. bester/schlechtester Kategorie.
    """
    anzahl_fragen = results["anzahl_fragen"]
    punktestand = results["punkte"]
    details: List[Dict[str, Any]] = results["details"]

    print("\n" + "=" * 40)
    print("Ergebnis:")
    print(f"Du hast {punktestand} von {anzahl_fragen} Fragen richtig beantwortet.")

    if anzahl_fragen > 0:
        prozent = (punktestand / anzahl_fragen) * 100
    else:
        prozent = 0.0
    print(f"Trefferquote: {prozent:.2f}%")

    # Kategorien-Statistik
    kategorien_statistik: Dict[str, Dict[str, int]] = {}

    for eintrag in details:
        kategorie = eintrag["kategorie"]
        if kategorie not in kategorien_statistik:
            kategorien_statistik[kategorie] = {"gesamt": 0, "richtig": 0}

        kategorien_statistik[kategorie]["gesamt"] += 1
        if eintrag["ist_richtig"]:
            kategorien_statistik[kategorie]["richtig"] += 1

    if kategorien_statistik:
        print("\nStatistik nach Kategorien:")
        beste_kategorie = None
        bester_wert = -1.0
        schlechteste_kategorie = None
        schlechtester_wert = 2.0

        for kategorie, werte in kategorien_statistik.items():
            gesamt = werte["gesamt"]
            richtig = werte["richtig"]
            anteil = richtig / gesamt
            print(f"- {kategorie}: {richtig}/{gesamt} ({anteil * 100:.2f}%)")

            if anteil > bester_wert:
                bester_wert = anteil
                beste_kategorie = kategorie

            if anteil < schlechtester_wert:
                schlechtester_wert = anteil
                schlechteste_kategorie = kategorie

        print("\nBeste Kategorie:", beste_kategorie)
        print("Schlechteste Kategorie:", schlechteste_kategorie)