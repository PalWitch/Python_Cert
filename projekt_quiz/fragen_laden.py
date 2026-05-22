from typing import List, Dict, Any
import json

Frage = Dict[str, Any]


def lade_fragen_aus_json(pfad: str) -> List[Frage]:
    """
    Lädt Fragen aus einer JSON-Datei und gibt sie als Liste von Dicts zurück.
    """
    with open(pfad, "r", encoding="utf-8") as datei:
        daten = json.load(datei)

    # Optional: einfache Validierung
    if not isinstance(daten, list):
        raise ValueError("Die JSON-Datei muss eine Liste von Fragen enthalten.")

    return daten