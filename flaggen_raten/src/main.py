import flet as ft
import random
import os
from laender import Laender
from flet import View, Text, Row, View, Page, AppBar, Button, IconButton, Image
from laender_laden import erstelle_laender_objekte, laender_dateiladen

#TODO Funktion zum Check, ob die Flagge vorhanden ist, sonst neuladen

def init_game():
    laender_json = laender_dateiladen("laender.json")
    laender_liste = erstelle_laender_objekte(laender_json)  
    return laender_liste

def random_land(laender_liste: list[Laender]):
    zufallsland = random.randrange(len(laender_liste)-1)
    return laender_liste.pop(zufallsland)


def main(page: ft.Page):
    zaehler = ft.Text("0", size=30, data=0)
    laender_geladen = init_game()
    zufallsland = random_land(laender_geladen)

    flag_image = ft.Image(
    width=300,
    height=300,
    repeat=ft.ImageRepeat.NO_REPEAT,
    src=os.path.join(zufallsland.cca3 + ".png")
    )
    bevoelkerung_formatiert = f"{zufallsland.bevoelkerung:,}".replace(",", ".") 

    textfeld_name = Text(value=f"Name: {zufallsland.name}", size=25)
    textfeld_hauptstadt = Text(value=f"Hauptstadt: {zufallsland.hauptstadt}", size=25)
    textfeld_bevoelkerung = Text(value=f"Bevölkerung: {bevoelkerung_formatiert}", size=25)
    textfeld_kontinent = Text(value=f"Kontinent: {zufallsland.kontinent}", size=25)
    textfeld_sprache = Text(value=f"Sprache: {zufallsland.sprache}", size=25)
    textfeld_grenzen = Text(value=f"Grenzen: {zufallsland.grenzen}", size=25)

    def start_game(e):
        print("Spiel gestartet")
      
    def next_land(e):
        next_land_ = random_land(laender_geladen)
        flag_image.src = next_land_.cca3 + '.png'
        textfeld_name.value = next_land_.name
        textfeld_hauptstadt.value = next_land_.hauptstadt
        textfeld_bevoelkerung.value = next_land_.bevoelkerung
        textfeld_kontinent.value = next_land_.kontinent
        textfeld_sprache.value = next_land_.sprache
        textfeld_grenzen.value = next_land_.grenzen

    page.update()
        
    
    page.views.append(View(route="/", controls=[

        flag_image,

        textfeld_name,
        textfeld_hauptstadt,
        textfeld_bevoelkerung,
        textfeld_kontinent,
        textfeld_sprache,
        textfeld_grenzen,
        
        Button("Nächstes Land", on_click=next_land),
        Button("Flaggen Raten", on_click=start_game)
    ]))

    page.update()
if __name__ == "__main__":
    ft.run(main)
 