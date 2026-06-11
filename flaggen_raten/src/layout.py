import flet as ft

DUNKELGRUEN = "#1b5e20"


def baue_layout(
    flag_image,
    textfeld_punktestand,
    textfeld_versuche,
    textfeld_rundenpunkte,
    textfeld_spielername,
    textfeld_laenge_anzeige,
    eingabefeld_loesung,
    textfeld_ergebnis,
    textfeld_hinweis,
    button_loesung_pruefen,
    button_hinweis,
    button_aufgeben,
    button_naechstes_land,
    button_neues_spiel,
    button_beenden,
    button_highscores,
):
    kopfzeile = ft.Container(
        bgcolor=DUNKELGRUEN,
        padding=10,
        content=ft.Column(
            spacing=6,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Column(
                            spacing=4,
                            controls=[
                                ft.Text("Flaggen raten", size=20, weight="bold", color="white"),
                                textfeld_spielername,
                            ],
                        ),
                        ft.Row(
                            spacing=6,
                            wrap=True,
                            controls=[button_highscores, button_neues_spiel, button_beenden],
                        ),
                    ],
                ),
                ft.Row(
                    spacing=8,
                    wrap=True,
                    controls=[
                        ft.Column(
                            spacing=2,
                            controls=[textfeld_punktestand, textfeld_versuche, textfeld_rundenpunkte],
                        )
                    ],
                ),
            ],
        ),
    )

    spielbereich = ft.Container(
        expand=True,
        padding=12,
        content=ft.Column(
            spacing=8,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    bgcolor="#e8efe9",
                    border_radius=16,
                    padding=10,
                    content=flag_image,
                ),
                textfeld_laenge_anzeige,
                eingabefeld_loesung,
                textfeld_ergebnis,
                textfeld_hinweis,
                ft.Row(
                    spacing=8,
                    wrap=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[button_loesung_pruefen, button_hinweis, button_aufgeben, button_naechstes_land],
                ),
            ],
        ),
    )

    return ft.View(route="/spiel", padding=0, scroll=ft.ScrollMode.AUTO, controls=[kopfzeile, spielbereich])


def baue_highscore_view(highscore_spalte, button_zurueck_start, button_zurueck_spiel):
    return ft.View(
        route="/highscores",
        padding=0,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Container(
                bgcolor=DUNKELGRUEN,
                padding=10,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text("Highscores", size=28, weight="bold", color="white"),
                        ft.Row(spacing=8, wrap=True, controls=[button_zurueck_spiel, button_zurueck_start]),
                    ],
                ),
            ),
            ft.Container(
                padding=12,
                expand=True,
                content=ft.Column(
                    spacing=8,
                    controls=[
                        ft.Text("Die 10 besten Ergebnisse aus deiner CSV-Datei.", size=18),
                        highscore_spalte,
                    ],
                ),
            ),
        ],
    )