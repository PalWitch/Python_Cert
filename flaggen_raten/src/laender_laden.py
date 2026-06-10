import json
from laender import Laender

def laender_dateiladen(laender_datei:str):
    with open(laender_datei, encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def erstelle_laender_objekte(laender_dict: dict):
    laender_liste = []

    for land in laender_dict:
        cca3 = land["cca3"]
        name = land["translations"]["deu"]["official"]
        hauptstadt = ", ".join(land.get("capital", [])) or "Keine Angabe"
        grenzen = ", ".join(land.get("borders", [])) or "keine"
        sprache = ", ".join(land.get("languages", {}).values()) or "Keine Angabe"
        bevoelkerung = land.get("population", 0)
        kontinent = ", ".join(land.get("continents", [])) or "Keine Angabe"

        laender_liste.append(
            Laender(cca3, name, hauptstadt, grenzen, sprache, bevoelkerung, kontinent)
        )

    return laender_liste

