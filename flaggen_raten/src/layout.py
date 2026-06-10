import flet as ft

def baue_layout(
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
    start_game=None,
):
    status_spalte = ft.Column(
        controls=[
            textfeld_punktestand,
            textfeld_versuche,
        ],
        spacing=8,
        alignment=ft.MainAxisAlignment.START,
    )

    kopfbereich = ft.Row(
        controls=[
            flag_image,
            status_spalte,
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.START,
    )

    button_reihe_1 = ft.Row(
        controls=[
            button_loesung_pruefen,
            button_hinweis,
        ],
        spacing=10,
        wrap=True,
    )

    button_reihe_2 = ft.Row(
        controls=[
            button_aufgeben,
            button_naechstes_land,
        ],
        spacing=10,
        wrap=True,
    )

    return ft.View(
        route="/",
        scroll=ft.ScrollMode.AUTO,
        padding=20,
        controls=[
            ft.Column(
                spacing=8,
                controls=[
                    kopfbereich,
                    textfeld_laenge_anzeige,
                    ft.Container(
                        content=eingabefeld_loesung,
                        margin=ft.Margin.only(top=0, bottom=2),
                    ),
                    textfeld_ergebnis,
                    textfeld_hinweis,
                    button_reihe_1,
                    button_reihe_2,

                    #Button("Flaggen Raten", on_click=start_game)
                ],
            )
        ],
    )
