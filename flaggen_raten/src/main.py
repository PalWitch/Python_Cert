import flet as ft
import random
import os
from laender import Laender
from flet import Text, Button, Image
from laender_laden import erstelle_laender_objekte, laender_dateiladen
from layout import baue_layout


#TODO Funktion zum Check, ob die Flagge vorhanden ist, sonst neuladen

def init_game():
    laender_json = laender_dateiladen("laender.json")
    laender_liste = erstelle_laender_objekte(laender_json)
    return laender_liste


def random_land(laender_liste: list[Laender]):
    zufallsland = random.randrange(len(laender_liste))
    return laender_liste.pop(zufallsland)


def main(page: ft.Page):
    page.title = "Flaggen raten"
    page.window.width = 620
    page.window.height = 760
    page.window.min_width = 620
    page.window.min_height = 700
    page.window.resizable = True

    punktestand = 0
    versuche = 5
    laender_geladen = init_game()
    zufallsland = random_land(laender_geladen)
    offene_hinweise = []

    def name_verschluesseln(name):
        name = name.replace("_", "-")
        return "".join(
            buchstabe if buchstabe in [" ", "-"] else "*"
            for buchstabe in name
        )

    def normalisiere_name(name):
        return name.strip().lower().replace("_", "-")

    def bevoelkerung_text(land):
        return f"{land.bevoelkerung:,}".replace(",", ".")

    def hinweise_fuer_land(land):
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
            hinweise.append(f"Grenzen: {land.grenzen}")

        return hinweise

    def naechster_hinweis():
        nonlocal offene_hinweise

        if not offene_hinweise:
            return "Kein weiterer Hinweis verfügbar."

        hinweis = random.choice(offene_hinweise)
        offene_hinweise.remove(hinweis)
        return hinweis

    def runde_beenden(nachricht, loesung_anzeigen=False):
        eingabefeld_loesung.disabled = True
        button_loesung_pruefen.disabled = True
        button_aufgeben.disabled = True
        button_hinweis.disabled = True
        textfeld_ergebnis.value = nachricht

        if loesung_anzeigen:
            textfeld_hinweis.value = f"Richtige Lösung: {zufallsland.name}"
        else:
            textfeld_hinweis.value = ""

    def neues_land_laden():
        nonlocal zufallsland, versuche, offene_hinweise

        if not laender_geladen:
            textfeld_ergebnis.value = "Keine Länder mehr vorhanden."
            textfeld_hinweis.value = ""
            eingabefeld_loesung.disabled = True
            button_loesung_pruefen.disabled = True
            button_aufgeben.disabled = True
            button_hinweis.disabled = True
            button_naechstes_land.disabled = True
            page.update()
            return

        zufallsland = random_land(laender_geladen)
        versuche = 5
        offene_hinweise = hinweise_fuer_land(zufallsland)

        flag_image.src = os.path.join(zufallsland.cca3 + ".png")
        textfeld_laenge_anzeige.value = name_verschluesseln(zufallsland.name)
        textfeld_ergebnis.value = ""
        textfeld_hinweis.value = ""
        textfeld_versuche.value = f"Versuche: {versuche}"
        eingabefeld_loesung.value = ""
        eingabefeld_loesung.disabled = False
        button_loesung_pruefen.disabled = False
        button_aufgeben.disabled = False
        button_hinweis.disabled = False

    flag_image = ft.Image(
        width=260,
        height=260,
        repeat=ft.ImageRepeat.NO_REPEAT,
        src=os.path.join(zufallsland.cca3 + ".png"),
    )

    offene_hinweise = hinweise_fuer_land(zufallsland)

    textfeld_punktestand = ft.Text(value=f"Punkte: {punktestand}", size=25)
    textfeld_versuche = ft.Text(value=f"Versuche: {versuche}", size=25)
    textfeld_laenge_anzeige = ft.Text(value=name_verschluesseln(zufallsland.name), size=25)
    textfeld_hinweis = ft.Text(value="", size=22)
    textfeld_ergebnis = ft.Text(value="", size=25)
    eingabefeld_loesung = ft.TextField(label="Dein Tipp", width=320)

    def start_game(e):
        print("Spiel gestartet")

    def next_land(e):
        neues_land_laden()
        page.update()

    def loesung_pruefen(e):
        nonlocal punktestand, versuche

        eingabe = normalisiere_name(eingabefeld_loesung.value)
        loesung = normalisiere_name(zufallsland.name)

        if not eingabe:
            textfeld_ergebnis.value = "Bitte gib zuerst einen Ländernamen ein."
            page.update()
            return

        if eingabe == loesung:
            punktestand += 1
            textfeld_punktestand.value = f"Punkte: {punktestand}"
            runde_beenden("Richtig!", loesung_anzeigen=False)
        else:
            versuche -= 1
            textfeld_versuche.value = f"Versuche: {versuche}"
            textfeld_ergebnis.value = "Leider falsch!"
            textfeld_hinweis.value = naechster_hinweis()
            eingabefeld_loesung.value = ""

            if versuche == 0:
                runde_beenden("Keine Versuche mehr.", loesung_anzeigen=True)

        page.update()

    def hinweis_anzeigen(e):
        nonlocal versuche

        if versuche > 1:
            versuche -= 1
            textfeld_versuche.value = f"Versuche: {versuche}"
            textfeld_ergebnis.value = "Hier ist dein Hinweis:"
            textfeld_hinweis.value = naechster_hinweis()
        else:
            versuche = 0
            textfeld_versuche.value = f"Versuche: {versuche}"
            runde_beenden("Keine Versuche mehr.", loesung_anzeigen=True)

        page.update()

    def aufgeben(e):
        runde_beenden("Du hast aufgegeben.", loesung_anzeigen=True)
        page.update()

    button_loesung_pruefen = ft.Button("Lösung prüfen", on_click=loesung_pruefen)
    button_hinweis = ft.Button("Hinweis", on_click=hinweis_anzeigen)
    button_aufgeben = ft.Button("Aufgeben", on_click=aufgeben)
    button_naechstes_land = ft.Button("Nächstes Land", on_click=next_land)

    page.views.append(
        baue_layout(
            flag_image,
            textfeld_punktestand,
            textfeld_versuche,
            textfeld_laenge_anzeige,
            eingabefeld_loesung,
            textfeld_ergebnis,
            textfeld_hinweis,
            button_loesung_pruefen,
            button_hinweis,
            button_aufgeben,
            button_naechstes_land,
            start_game,
        )
    )

    page.update()


if __name__ == "__main__":
    ft.run(main)