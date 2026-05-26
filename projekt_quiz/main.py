from typing import List, Dict, Any
from fragen_laden import lade_fragen_aus_json, Frage
import quiz_engine

print("Herzlich Willkommen zum PCEP/PCAP-Quiz!  by AnnK")

def hauptmenue() -> None:
    """
    Zeigt das Hauptmenü an.
    """
    print("\n=== PCEP Quiz ===")
    print("1. Quiz starten (ohne Filter)")
    print("2. Quiz nach Kategorie")
    print("3. Quiz nach Schwierigkeit")
    print("4. Meine Ergebnisse anzeigen")
    print("5. Beenden")


def programm_starten() -> None:
    """
    Hauptfunktion mit Menü-Schleife.
    """
    alle_ergebnisse: List[Dict[str, Any]] = []
    alle_fragen    : List[Frage] = lade_fragen_aus_json("fragen.json")

    while True:
        hauptmenue()
        auswahl = input("Bitte wähle eine Option (1-5): ")

        if auswahl == "1":
            ergebnis = quiz_engine.run_quiz(alle_fragen)
            alle_ergebnisse.append(ergebnis)
            quiz_engine.zeige_ergebnis(ergebnis)

        elif auswahl == "2":
            # Quiz nach Kategorie
            quiz_engine.quiz_nach_kategorie(alle_fragen, alle_ergebnisse)

        elif auswahl == "3":
            quiz_engine.quiz_nach_schwierigkeit(alle_fragen, alle_ergebnisse)
        
        elif auswahl == "4":
            if not alle_ergebnisse:
                print("Es wurden noch keine Quiz-Ergebnisse gespeichert.")
            else:
                print(f"\nDu hast bisher {len(alle_ergebnisse)} Quiz(s) gespielt.")
                letztes_ergebnis = alle_ergebnisse[-1]
                print("\nLetztes Ergebnis:")
                quiz_engine.zeige_ergebnis(letztes_ergebnis)

        elif auswahl == "5":
            print("Programm wird beendet. Auf Wiedersehen!")
            break

        else:
            print("Ungültige Auswahl. Bitte 1, 2, 3, 4 oder 5 eingeben.")


if __name__ == "__main__":
    programm_starten()