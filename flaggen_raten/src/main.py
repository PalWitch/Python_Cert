import csv
from difflib import SequenceMatcher
import os
import random
from datetime import datetime

import flet as ft
from unidecode import unidecode

from laender_laden import erstelle_laender_objekte, laender_dateiladen
from layout import baue_layout, baue_highscore_view

DATEI_HIGHSCORES = "highscores.csv"
MAX_HIGHSCORES = 10
PUNKTE_PRO_RUNDE = 5
MINDESTPUNKTE_PRO_RUNDE = 1

#TODO Funktion, die Länder ohne Flagge exkludiert
#TODO Hinweise-Hierarchie: Kontinent, Grenzen, Hauptstadt, Sprachen, Bevölkerung
#TODO App-Schließen-Button

def erstelle_cca3_namen_map_aus_json(laender_json):
    cca3_namen_map = {}
    for land in laender_json:
        cca3 = land.get("cca3", "").strip()
        deutscher_name = land.get("translations", {}).get("deu", {}).get("common")
        if not deutscher_name:
            deutscher_name = land.get("name", {}).get("common", cca3)
        cca3_namen_map[cca3] = deutscher_name
    return cca3_namen_map


def uebersetze_grenzen(grenzen, cca3_namen_map):
    if not grenzen:
        return "Keine Landgrenzen"
    if isinstance(grenzen, str):
        grenzen_text = grenzen.strip()
        if not grenzen_text or grenzen_text.lower() == "keine":
            return "Keine Landgrenzen"
        grenzen_text = grenzen_text.replace("[", "").replace("]", "").replace("'", "").replace('"', "")
        grenzen = [code.strip() for code in grenzen_text.split(",") if code.strip()]
    if not grenzen:
        return "Keine Landgrenzen"
    uebersetzte_grenzen = [cca3_namen_map.get(code.strip(), code.strip()) for code in grenzen]
    return ", ".join(uebersetzte_grenzen)


def init_game():
    laender_json = laender_dateiladen("laender.json")
    cca3_namen_map = erstelle_cca3_namen_map_aus_json(laender_json)
    laender_liste = erstelle_laender_objekte(laender_json)
    return laender_liste, cca3_namen_map


def random_land(laender_liste):
    zufallsindex = random.randrange(len(laender_liste))
    return laender_liste.pop(zufallsindex)


def highscore_speichern(name, punkte):
    datei_existiert = os.path.exists(DATEI_HIGHSCORES)
    with open(DATEI_HIGHSCORES, "a", newline="", encoding="utf-8") as datei:
        writer = csv.writer(datei)
        if not datei_existiert:
            writer.writerow(["name", "punkte", "datum"])
        writer.writerow([name, punkte, datetime.now().strftime("%d.%m.%Y %H:%M")])


def highscores_laden():
    if not os.path.exists(DATEI_HIGHSCORES):
        return []
    with open(DATEI_HIGHSCORES, "r", newline="", encoding="utf-8") as datei:
        reader = csv.DictReader(datei)
        daten = list(reader)
    daten.sort(key=lambda eintrag: int(eintrag["punkte"]), reverse=True)
    return daten[:MAX_HIGHSCORES]


def main(page: ft.Page):
    page.title = "Flaggen raten"
    try:
        page.window_width = 430
        page.window_height = 900
        page.window_min_width = 380
        page.window_min_height = 760
    except Exception:
        pass

    punktestand = 0
    versuche = 5
    punkte_diese_runde = PUNKTE_PRO_RUNDE
    spielername = ""
    score_gespeichert = False
    laender_geladen = []
    zufallsland = None
    offene_hinweise = []
    cca3_namen_map = {}

    def name_verschluesseln(name):
        name = name.replace("_", "-")
        return "".join(buchstabe if buchstabe in [" ", "-"] else "*" for buchstabe in name)

    def normalisiere_name(name):
        text = unidecode((name or "").strip()).casefold()
        return " ".join(text.replace("_", "-").split())

    def bevoelkerung_text(land):
        return f"{land.bevoelkerung:,}".replace(",", ".")

    def ist_aehnlich_genug(eingabe, loesung, grenze=0.9):
        if not eingabe or not loesung:
            return False
        if abs(len(eingabe) - len(loesung)) > 2:
            return False
        return SequenceMatcher(None, eingabe, loesung).ratio() >= grenze

    def hinweise_fuer_land(land, namen_map):
        hinweise = []
        if land.hauptstadt:
            hinweise.append(f"Hauptstadt: {land.hauptstadt}")
        if land.kontinent:
            hinweise.append(f"Kontinent: {land.kontinent}")
        if land.sprache:
            hinweise.append(f"Sprache: {land.sprache}")
        if land.bevoelkerung:
            hinweise.append(f"Bevölkerung: {bevoelkerung_text(land)}")
        if land.grenzen:
            hinweise.append(f"Grenzen: {uebersetze_grenzen(land.grenzen, namen_map)}")
        random.shuffle(hinweise)
        return hinweise

    def naechster_hinweis():
        nonlocal offene_hinweise
        if not offene_hinweise:
            return "Kein weiterer Hinweis verfügbar."
        return offene_hinweise.pop(0)

    def score_einmal_speichern():
        nonlocal score_gespeichert
        if spielername and not score_gespeichert:
            highscore_speichern(spielername, punktestand)
            score_gespeichert = True

    def setze_spielstatus_aktiv(aktiv):
        eingabefeld_loesung.disabled = not aktiv
        button_loesung_pruefen.disabled = not aktiv
        button_hinweis.disabled = not aktiv
        button_aufgeben.disabled = not aktiv
        button_naechstes_land.disabled = aktiv
        button_beenden.disabled = False
        button_highscores.disabled = False
        button_neues_spiel.disabled = False

    def aktualisiere_highscore_liste():
        daten = highscores_laden()
        if not daten:
            highscore_spalte.controls = [ft.Container(content=ft.Text("Noch keine Highscores vorhanden.", size=18), padding=10)]
            page.update()
            return
        eintraege = []
        for index, eintrag in enumerate(daten, start=1):
            eintraege.append(
                ft.Container(
                    bgcolor="#e8efe9",
                    border_radius=10,
                    padding=10,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(f"{index}. {eintrag['name']}", size=18, weight="bold", color="#123524"),
                            ft.Text(f"{eintrag['punkte']} Punkte", size=18, color="#123524"),
                            ft.Text(eintrag["datum"], size=14, color="#365a46"),
                        ],
                    ),
                )
            )
        highscore_spalte.controls = eintraege
        page.update()

    def aktualisiere_anzeige():
        if zufallsland is None:
            return
        flag_image.src = os.path.join(zufallsland.cca3 + ".png")
        textfeld_punktestand.value = f"Punkte gesamt: {punktestand}"
        textfeld_versuche.value = f"Versuche: {versuche}"
        textfeld_rundenpunkte.value = f"Frage: {punkte_diese_runde} Punkte"
        textfeld_laenge_anzeige.value = f"Länge: {name_verschluesseln(zufallsland.name)}"
        textfeld_spielername.value = f"Spieler: {spielername}"

    def neues_land_laden():
        nonlocal zufallsland, versuche, offene_hinweise, punkte_diese_runde
        if not laender_geladen:
            score_einmal_speichern()
            textfeld_ergebnis.value = "Keine Länder mehr vorhanden. Spiel beendet."
            textfeld_hinweis.value = ""
            setze_spielstatus_aktiv(False)
            button_naechstes_land.disabled = True
            aktualisiere_highscore_liste()
            page.update()
            return
        zufallsland = random_land(laender_geladen)
        versuche = 5
        punkte_diese_runde = PUNKTE_PRO_RUNDE
        offene_hinweise = hinweise_fuer_land(zufallsland, cca3_namen_map)
        eingabefeld_loesung.value = ""
        textfeld_ergebnis.value = ""
        textfeld_hinweis.value = ""
        setze_spielstatus_aktiv(True)
        aktualisiere_anzeige()
        page.update()

    def zeige_view(view):
        page.views.clear()
        page.views.append(view)
        page.update()

    def starte_spiel(e):
        nonlocal spielername, punktestand, score_gespeichert, laender_geladen, cca3_namen_map, punkte_diese_runde
        eingegebener_name = (eingabefeld_spieler.value or "").strip()
        if not eingegebener_name:
            textfeld_startinfo.value = "Bitte gib zuerst deinen Namen ein."
            page.update()
            return
        spielername = eingegebener_name
        punktestand = 0
        punkte_diese_runde = PUNKTE_PRO_RUNDE
        score_gespeichert = False
        laender_geladen, cca3_namen_map = init_game()
        textfeld_startinfo.value = ""
        neues_land_laden()
        zeige_view(spiel_view)

    def neues_spiel(e, score_vorher_speichern=True):
        nonlocal punktestand, score_gespeichert, spielername, punkte_diese_runde, laender_geladen, cca3_namen_map, zufallsland, offene_hinweise
        if score_vorher_speichern:
            score_einmal_speichern()
        punktestand = 0
        punkte_diese_runde = PUNKTE_PRO_RUNDE
        score_gespeichert = False
        spielername = ""
        laender_geladen = []
        cca3_namen_map = {}
        zufallsland = None
        offene_hinweise = []
        eingabefeld_spieler.value = ""
        eingabefeld_loesung.value = ""
        textfeld_ergebnis.value = ""
        textfeld_hinweis.value = ""
        textfeld_punktestand.value = "Punkte gesamt: 0"
        textfeld_versuche.value = "Versuche: 5"
        textfeld_rundenpunkte.value = f"Frage: {PUNKTE_PRO_RUNDE} Punkte"
        textfeld_spielername.value = "Spieler: -"
        textfeld_startinfo.value = ""
        aktualisiere_highscore_liste()
        zeige_view(start_view)

    def spiel_beenden(e):
        nonlocal punktestand, punkte_diese_runde
        if zufallsland is not None and not button_loesung_pruefen.disabled:
            punktestand += punkte_diese_runde
        score_einmal_speichern()
        aktualisiere_highscore_liste()
        neues_spiel(e, score_vorher_speichern=False)
        textfeld_startinfo.value = "Spiel beendet. Dein Punktestand wurde gespeichert."
        page.update()

    def next_land(e):
        neues_land_laden()

    def loesung_pruefen(e):
        nonlocal punktestand, versuche, punkte_diese_runde
        if zufallsland is None:
            return
        eingabe = normalisiere_name(eingabefeld_loesung.value)
        loesung = normalisiere_name(zufallsland.name)
        if not eingabe:
            textfeld_ergebnis.value = "Bitte gib zuerst einen Ländernamen ein."
            page.update()
            return
        if eingabe == loesung or ist_aehnlich_genug(eingabe, loesung):
            punktestand += punkte_diese_runde
            textfeld_punktestand.value = f"Punkte gesamt: {punktestand}"
            textfeld_laenge_anzeige.value = f"Lösung: {zufallsland.name}"
            textfeld_laenge_anzeige.update()
            textfeld_ergebnis.value = f"Richtig! Du bekommst {punkte_diese_runde} Punkte."
            textfeld_hinweis.value = "Sehr gut, lade jetzt das nächste Land."
            setze_spielstatus_aktiv(False)
        else:
            versuche -= 1
            if punkte_diese_runde > MINDESTPUNKTE_PRO_RUNDE:
                punkte_diese_runde -= 1
            textfeld_versuche.value = f"Versuche: {versuche}"
            textfeld_rundenpunkte.value = f"Frage: {punkte_diese_runde} Punkte"
            textfeld_ergebnis.value = "Leider falsch! 1 Punkt wurde abgezogen."
            textfeld_hinweis.value = naechster_hinweis()
            eingabefeld_loesung.value = ""
            if versuche == 0:
                score_einmal_speichern()
                textfeld_ergebnis.value = "Keine Versuche mehr."
                textfeld_laenge_anzeige.value = f"Lösung: {zufallsland.name}"
                textfeld_laenge_anzeige.update()
                textfeld_hinweis.value = f"Richtige Lösung: {zufallsland.name}"
                setze_spielstatus_aktiv(False)
                aktualisiere_highscore_liste()
        page.update()

    def hinweis_anzeigen(e):
        nonlocal versuche, punkte_diese_runde
        if zufallsland is None:
            return
        if versuche > 1:
            versuche -= 1
            if punkte_diese_runde > MINDESTPUNKTE_PRO_RUNDE:
                punkte_diese_runde -= 1
            textfeld_versuche.value = f"Versuche: {versuche}"
            textfeld_rundenpunkte.value = f"Frage: {punkte_diese_runde} Punkte"
            textfeld_ergebnis.value = "Hier ist dein Hinweis:"
            textfeld_hinweis.value = naechster_hinweis()
        else:
            versuche = 0
            if punkte_diese_runde > MINDESTPUNKTE_PRO_RUNDE:
                punkte_diese_runde -= 1
            textfeld_versuche.value = f"Versuche: {versuche}"
            textfeld_rundenpunkte.value = f"Frage: {punkte_diese_runde} Punkte"
            score_einmal_speichern()
            textfeld_ergebnis.value = "Keine Versuche mehr."
            textfeld_laenge_anzeige.value = f"Lösung: {zufallsland.name}"
            textfeld_laenge_anzeige.update()
            textfeld_hinweis.value = f"Richtige Lösung: {zufallsland.name}"
            setze_spielstatus_aktiv(False)
            aktualisiere_highscore_liste()
        page.update()

    def aufgeben(e):
        if zufallsland is None:
            return
        score_einmal_speichern()
        textfeld_ergebnis.value = "Du hast aufgegeben."
        textfeld_laenge_anzeige.value = f"Lösung: {zufallsland.name}"
        textfeld_hinweis.value = f"Richtige Lösung: {zufallsland.name}"
        setze_spielstatus_aktiv(False)
        aktualisiere_highscore_liste()
        page.update()

    def zeige_highscores(e):
        aktualisiere_highscore_liste()
        zeige_view(highscore_view)

    def zurueck_zum_start(e):
        zeige_view(start_view)

    def zurueck_zum_spiel(e):
        zeige_view(spiel_view)

    flag_image = ft.Image(width=170, height=170, src="", repeat=ft.ImageRepeat.NO_REPEAT)

    textfeld_punktestand = ft.Text(value="Punkte gesamt: 0", size=16, weight="bold", color="white")
    textfeld_versuche = ft.Text(value="Versuche: 5", size=15, color="white")
    textfeld_rundenpunkte = ft.Text(value=f"Frage: {PUNKTE_PRO_RUNDE} Punkte", size=15, color="white")
    textfeld_spielername = ft.Text(value="Spieler: -", size=15, color="white")
    textfeld_laenge_anzeige = ft.Text(value="Länge: -", size=18, weight="bold")
    textfeld_hinweis = ft.Text(value="", size=16)
    textfeld_ergebnis = ft.Text(value="", size=17, weight="bold")

    eingabefeld_loesung = ft.TextField(label="Dein Tipp", width=280, on_submit=loesung_pruefen)
    eingabefeld_spieler = ft.TextField(label="Dein Name", width=260, on_submit=starte_spiel)
    textfeld_startinfo = ft.Text(value="", size=18)

    button_loesung_pruefen = ft.Button("Lösung prüfen", on_click=loesung_pruefen)
    button_hinweis = ft.Button("Hinweis", on_click=hinweis_anzeigen)
    button_aufgeben = ft.Button("Aufgeben", on_click=aufgeben)
    button_naechstes_land = ft.Button("Nächstes Land", on_click=next_land)
    button_neues_spiel = ft.Button("Neues Spiel", on_click=neues_spiel)
    button_beenden = ft.Button("Beenden", on_click=spiel_beenden)
    button_highscores = ft.Button("Highscores", on_click=zeige_highscores)
    button_spiel_starten = ft.Button("Spiel starten", on_click=starte_spiel)
    button_zurueck_start = ft.Button("Startseite", on_click=zurueck_zum_start)
    button_zurueck_spiel = ft.Button("Zum Spiel", on_click=zurueck_zum_spiel)

    highscore_spalte = ft.Column(spacing=10)

    start_view = ft.View(
        route="/",
        padding=18,
        controls=[
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=14,
                controls=[
                    ft.Text("Flaggen raten", size=26, weight="bold"),
                    ft.Text("Gib deinen Namen ein und starte eine neue Runde.", size=16),
                    eingabefeld_spieler,
                    ft.Row(alignment=ft.MainAxisAlignment.CENTER, wrap=True, spacing=10, controls=[button_spiel_starten, button_highscores]),
                    textfeld_startinfo,
                ],
            )
        ],
    )

    spiel_view = baue_layout(
        flag_image=flag_image,
        textfeld_punktestand=textfeld_punktestand,
        textfeld_versuche=textfeld_versuche,
        textfeld_rundenpunkte=textfeld_rundenpunkte,
        textfeld_spielername=textfeld_spielername,
        textfeld_laenge_anzeige=textfeld_laenge_anzeige,
        eingabefeld_loesung=eingabefeld_loesung,
        textfeld_ergebnis=textfeld_ergebnis,
        textfeld_hinweis=textfeld_hinweis,
        button_loesung_pruefen=button_loesung_pruefen,
        button_hinweis=button_hinweis,
        button_aufgeben=button_aufgeben,
        button_naechstes_land=button_naechstes_land,
        button_neues_spiel=button_neues_spiel,
        button_beenden=button_beenden,
        button_highscores=button_highscores,
    )

    highscore_view = baue_highscore_view(highscore_spalte=highscore_spalte, button_zurueck_start=button_zurueck_start, button_zurueck_spiel=button_zurueck_spiel)

    page.views.append(start_view)
    page.update()


if __name__ == "__main__":
    ft.run(main)