# ------------------------------------------------------------
# IMPORTE
# ------------------------------------------------------------
# tkinter ist die Standardbibliothek für einfache GUIs in Python.
# Wir importieren tkinter als "tk", damit die Schreibweise kürzer ist.
import tkinter as tk

# ttk enthält "themed widgets", also modernere Varianten einiger Tkinter-Elemente.
# Für ein erstes Projekt ist ttk sehr praktisch.
from tkinter import ttk, messagebox

import random

# Typ-Hinweise: machen den Code verständlicher.
from typing import List, Dict, Any

# Wir nutzen den vorhandenen Loader weiter.
from fragen_laden import lade_fragen_aus_json, Frage

# ------------------------------------------------------------
# KONSTANTEN
# ------------------------------------------------------------
# Wie in der Konsolen-Engine begrenzen wir das Quiz auf maximal 10 Fragen.
MAX_FRAGEN = 10


# ------------------------------------------------------------
# KLASSE DER ANWENDUNG
# ------------------------------------------------------------
# Warum eine Klasse?
# Eine GUI besteht aus vielen Teilen, die gemeinsamen Zustand teilen:
# - alle Fragen
# - aktuelle Frage
# - Punktestand
# - ausgewählte Antwort
# - bereits beantwortet oder nicht
#
# Mit einer Klasse können wir diese Daten sauber in self.* speichern.
class QuizGUI:
    def __init__(self, root: tk.Tk) -> None:
        """
        Konstruktor der Anwendung.
        Diese Methode wird genau einmal beim Start aufgerufen.

        root ist das Hauptfenster der App.
        """
        self.root = root

        # Fenstertitel setzen
        self.root.title("PCEP / PCAP Quiz")

        # Startgröße des Fensters
        self.root.geometry("900x650")

        # Mindestgröße, damit die GUI nicht zu klein gezogen wird
        self.root.minsize(800, 550)

        # Speichert falsch beantwortete Fragen für eine Wiederholungsrunde
        # am Ende des Quiz.
        self.falsche_fragen: List[Frage] = []
        self.ist_wiederholungsrunde: bool = False

        # --------------------------------------------------------
        # DATEN LADEN
        # --------------------------------------------------------
        # Wir versuchen, die Fragen aus der JSON-Datei zu laden.
        # Falls das fehlschlägt, zeigen wir eine Fehlermeldung an.
        try:
            self.alle_fragen: List[Frage] = lade_fragen_aus_json("fragen.json")
        except Exception as e:
            messagebox.showerror(
                "Fehler beim Laden",
                f"Die Fragen konnten nicht geladen werden:\n{e}"
            )
            self.root.destroy()
            return

        # --------------------------------------------------------
        # ZUSTANDSVARIABLEN DER APP
        # --------------------------------------------------------
        # Diese Variablen beschreiben den aktuellen Stand des Quiz.
        self.quiz_fragen: List[Frage] = []          # die Fragen des aktuellen Durchlaufs
        self.aktuelle_frage_index: int = 0          # welche Frage gerade angezeigt wird
        self.punktestand: int = 0                   # wie viele Antworten richtig waren
        self.beantwortet: bool = False              # ob die aktuelle Frage schon geprüft wurde

        # Ergebnisdetails ähnlich wie in deiner Engine.
        self.details: List[Dict[str, Any]] = []

        # Die vom Benutzer ausgewählte Antwort speichern wir in einer IntVar.
        # Tkinter-Widgets wie Radiobuttons arbeiten oft mit solchen Variablenobjekten.
        # Wichtiger Startwert: -1 = noch nichts ausgewählt.
        self.ausgewaehlte_antwort = tk.IntVar(value=-1)

        # Für Filter im Startbildschirm.
        self.kategorie_var = tk.StringVar(value="Alle")
        self.schwierigkeit_var = tk.StringVar(value="Alle")

        # --------------------------------------------------------
        # HAUPT-CONTAINER
        # --------------------------------------------------------
        # Ein Frame ist ein Behälter für andere Widgets.
        # Darin organisieren wir die komplette App.
        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.pack(fill="both", expand=True)

        # Startansicht anzeigen.
        self.zeige_startseite()

    # ------------------------------------------------------------
    # HILFSMETHODE: ALLE WIDGETS IM HAUPTFRAME LÖSCHEN
    # ------------------------------------------------------------
    def leere_ansicht(self) -> None:
        """
        Entfernt alle Widgets aus dem Hauptbereich.

        Das ist ein einfacher Trick, um zwischen Seiten zu wechseln:
        Statt echte mehrere Fenster zu bauen, räumen wir denselben Bereich leer
        und setzen neue Widgets hinein.
        """
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # ------------------------------------------------------------
    # STARTSEITE
    # ------------------------------------------------------------
    def zeige_startseite(self) -> None:
        """
        Baut den Startbildschirm auf.
        Hier kann der Benutzer das Quiz starten und optional filtern.
        """
        self.leere_ansicht()

        # Zurück auf den allgemeinen Modus.
        self.ist_wiederholungsrunde = False

        titel = ttk.Label(
            self.main_frame,
            text="PCEP / PCAP Quiz",
            font=("Arial", 22, "bold")
        )
        titel.pack(pady=(10, 20))

        info = ttk.Label(
            self.main_frame,
            text=(
                "Willkommen zum Quiz.\n"
                "Wähle optional eine Kategorie oder Schwierigkeit und starte dann das Quiz."
            ),
            font=("Arial", 12),
            justify="center"
        )
        info.pack(pady=(0, 20))

        # -----------------------------
        # Filterbereich
        # -----------------------------
        filter_frame = ttk.LabelFrame(self.main_frame, text="Filter", padding=15)
        filter_frame.pack(fill="x", pady=10)

        # Verfügbare Kategorien dynamisch aus den Fragen erzeugen.
        kategorien = sorted({frage["kategorie"] for frage in self.alle_fragen})
        kategorien_werte = ["Alle"] + kategorien

        ttk.Label(filter_frame, text="Kategorie:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        kategorie_box = ttk.Combobox(
            filter_frame,
            textvariable=self.kategorie_var,
            values=kategorien_werte,
            state="readonly",
            width=35
        )
        kategorie_box.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(filter_frame, text="Schwierigkeit:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        schwierigkeit_box = ttk.Combobox(
            filter_frame,
            textvariable=self.schwierigkeit_var,
            values=["Alle", "1", "2", "3"],
            state="readonly",
            width=35
        )
        schwierigkeit_box.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        # -----------------------------
        # Buttons
        # -----------------------------
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=20)

        start_button = ttk.Button(
            button_frame,
            text="Quiz starten",
            command=self.quiz_starten
        )
        start_button.grid(row=0, column=0, padx=10)

        beenden_button = ttk.Button(
            button_frame,
            text="Beenden",
            command=self.root.destroy
        )
        beenden_button.grid(row=0, column=1, padx=10)

        # Kleine Statusinfo.
        status = ttk.Label(
            self.main_frame,
            text=f"Insgesamt geladene Fragen: {len(self.alle_fragen)}",
            font=("Arial", 10)
        )
        status.pack(pady=(15, 0))

    # ------------------------------------------------------------
    # QUIZ STARTEN
    # ------------------------------------------------------------
    def quiz_starten(self) -> None:
        """
        Filtert die Fragen entsprechend der Auswahl,
        mischt sie und startet den Durchlauf.
        """
        gefilterte_fragen = self.alle_fragen.copy()

        # Bei einem komplett neuen Quiz löschen wir alte Fehlfragen
        # und markieren, dass wir wieder in einer normalen Runde sind.
        self.falsche_fragen = []
        self.ist_wiederholungsrunde = False

        # Kategorie-Filter
        gewaehlte_kategorie = self.kategorie_var.get()
        if gewaehlte_kategorie != "Alle":
            gefilterte_fragen = [
                frage for frage in gefilterte_fragen
                if frage["kategorie"] == gewaehlte_kategorie
            ]

        # Schwierigkeits-Filter
        gewaehlte_schwierigkeit = self.schwierigkeit_var.get()
        if gewaehlte_schwierigkeit != "Alle":
            level = int(gewaehlte_schwierigkeit)
            gefilterte_fragen = [
                frage for frage in gefilterte_fragen
                if frage["schwierigkeit"] == level
            ]

        # Wenn nach dem Filtern keine Fragen übrig bleiben.
        if not gefilterte_fragen:
            messagebox.showinfo(
                "Keine Fragen gefunden",
                "Für diese Filterkombination wurden keine Fragen gefunden."
            )
            return

        # Fragen mischen.
        random.shuffle(gefilterte_fragen)

        # Auf MAX_FRAGEN begrenzen.
        self.quiz_fragen = gefilterte_fragen[:MAX_FRAGEN]

        # Quiz-Zustand zurücksetzen.
        self.aktuelle_frage_index = 0
        self.punktestand = 0
        self.details = []
        self.beantwortet = False

        # Erste Frage anzeigen.
        self.zeige_aktuelle_frage()

    # ------------------------------------------------------------
    # AKTUELLE FRAGE ANZEIGEN
    # ------------------------------------------------------------
    def zeige_aktuelle_frage(self) -> None:
        """
        Zeigt die aktuelle Frage im GUI an.
        """
        self.leere_ansicht()

        # Falls wir schon durch sind, Ergebnis anzeigen.
        if self.aktuelle_frage_index >= len(self.quiz_fragen):
            self.zeige_ergebnis()
            return

        self.beantwortet = False
        self.ausgewaehlte_antwort.set(-1)

        frage = self.quiz_fragen[self.aktuelle_frage_index]

        # Kopfbereich mit Fortschritt und Score.
        kopf_frame = ttk.Frame(self.main_frame)
        kopf_frame.pack(fill="x", pady=(0, 15))

        # Sichtbarer Hinweis, ob wir in einer normalen Runde oder
        # in der Wiederholung sind.
        modus_text = "Wiederholung" if self.ist_wiederholungsrunde else "Quiz"

        fortschritt = ttk.Label(
            kopf_frame,
            text=f"{modus_text} – Frage {self.aktuelle_frage_index + 1} von {len(self.quiz_fragen)}",
            font=("Arial", 11, "bold")
        )
        fortschritt.pack(side="left")

        score = ttk.Label(
            kopf_frame,
            text=f"Punkte: {self.punktestand}",
            font=("Arial", 11)
        )
        score.pack(side="right")

        # Frage selbst.
        frage_label = ttk.Label(
            self.main_frame,
            text=frage["frage"],
            font=("Arial", 16, "bold"),
            wraplength=760,
            justify="left"
        )
        frage_label.pack(anchor="w", pady=(10, 20))

        # Zusatzinfo.
        meta_label = ttk.Label(
            self.main_frame,
            text=f"Kategorie: {frage['kategorie']} | Schwierigkeit: {frage['schwierigkeit']}",
            font=("Arial", 10)
        )
        meta_label.pack(anchor="w", pady=(0, 15))

        # Antwortbereich.
        antwort_frame = ttk.LabelFrame(self.main_frame, text="Antwortmöglichkeiten", padding=15)
        antwort_frame.pack(fill="x", pady=10)

        # Radiobuttons erzeugen.
        for index, antwort_text in enumerate(frage["antworten"]):
            rb = ttk.Radiobutton(
                antwort_frame,
                text=antwort_text,
                variable=self.ausgewaehlte_antwort,
                value=index
            )
            rb.pack(anchor="w", pady=6)

        # Feedback-Bereich.
        self.feedback_label = ttk.Label(
            self.main_frame,
            text="",
            font=("Arial", 11),
            wraplength=760,
            justify="left"
        )
        self.feedback_label.pack(anchor="w", pady=(20, 10))

        # Buttonbereich.
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(fill="x", pady=15)

        links_frame = ttk.Frame(button_frame)
        links_frame.pack(side="left")

        rechts_frame = ttk.Frame(button_frame)
        rechts_frame.pack(side="right")

        self.pruefen_button = ttk.Button(
            links_frame,
            text="Antwort prüfen",
            command=self.antwort_pruefen
        )
        self.pruefen_button.pack(side="left", padx=(0, 10))

        # Prüfen, ob dies die letzte Frage der Runde ist
        ist_letzte_frage = (self.aktuelle_frage_index == len(self.quiz_fragen) - 1)

        weiter_text = "Ergebnis anzeigen" if ist_letzte_frage else "Nächste Frage"

        self.weiter_button = ttk.Button(
            links_frame,
            text=weiter_text,
            command=self.naechste_frage,
            state="disabled"
        )
        self.weiter_button.pack(side="left")

        abbrechen_button = ttk.Button(
            rechts_frame,
            text="Quiz abbrechen",
            command=self.quiz_abbrechen
        )
        abbrechen_button.pack(side="right")

    # ------------------------------------------------------------
    # ANTWORT PRÜFEN
    # ------------------------------------------------------------
    def antwort_pruefen(self) -> None:
        """
        Prüft die aktuell ausgewählte Antwort.
        """
        if self.beantwortet:
            # Falls bereits geprüft wurde, tun wir nichts.
            return

        ausgewaehlt = self.ausgewaehlte_antwort.get()

        # -1 bedeutet: Es wurde noch nichts markiert.
        if ausgewaehlt == -1:
            messagebox.showwarning(
                "Keine Auswahl",
                "Bitte wähle zuerst eine Antwort aus."
            )
            return

        frage = self.quiz_fragen[self.aktuelle_frage_index]
        richtiger_index = frage["antworten_richtig"]
        ist_richtig = ausgewaehlt == richtiger_index

        if ist_richtig:
            self.punktestand += 1
            feedback_text = (
                "Richtig! ✓\n\n"
                f"Erklärung: {frage['erklaerung']}"
            )
        else:
            # Falsch beantwortete Frage für spätere Wiederholung merken.
            self.falsche_fragen.append(frage)
            richtige_antwort = frage["antworten"][richtiger_index]
            feedback_text = (
                "Falsch. ✗\n\n"
                f"Richtige Antwort: {richtiger_index + 1}) {richtige_antwort}\n\n"
                f"Erklärung: {frage['erklaerung']}"
            )

        self.feedback_label.config(text=feedback_text)

        # Detaildaten für spätere Statistik speichern.
        self.details.append({
            "frage_text": frage["frage"],
            "kategorie": frage["kategorie"],
            "schwierigkeit": frage["schwierigkeit"],
            "ist_richtig": ist_richtig,
        })

        self.beantwortet = True

        # Nach dem Prüfen:
        # - Prüfen-Button deaktivieren
        # - Weiter-Button aktivieren
        self.pruefen_button.config(state="disabled")
        self.weiter_button.config(state="normal")

    # ------------------------------------------------------------
    # NÄCHSTE FRAGE
    # ------------------------------------------------------------
    def naechste_frage(self) -> None:
        """
        Springt zur nächsten Frage.
        """
        self.aktuelle_frage_index += 1
        self.zeige_aktuelle_frage()

    # ------------------------------------------------------------
    # QUIZ ABBRECHEN
    # ------------------------------------------------------------
    def quiz_abbrechen(self) -> None:
        """
        Bricht das laufende Quiz nach Nachfrage ab.
        """
        wirklich = messagebox.askyesno(
            "Quiz abbrechen",
            "Möchtest du das aktuelle Quiz wirklich abbrechen?"
        )
        if wirklich:
            self.zeige_startseite()

    # ------------------------------------------------------------
    # ERGEBNISSEITE
    # ------------------------------------------------------------
    def zeige_ergebnis(self) -> None:
        """
        Zeigt das Endergebnis des Quiz an.
        """
        self.leere_ansicht()

        anzahl = len(self.quiz_fragen)
        prozent = (self.punktestand / anzahl * 100) if anzahl > 0 else 0

        titel = ttk.Label(
            self.main_frame,
            text="Quiz beendet",
            font=("Arial", 22, "bold")
        )
        titel.pack(pady=(10, 20))

        ergebnis_label = ttk.Label(
            self.main_frame,
            text=(
                f"Du hast {self.punktestand} von {anzahl} Fragen richtig beantwortet.\n"
                f"Trefferquote: {prozent:.2f}%"
            ),
            font=("Arial", 14),
            justify="center"
        )
        ergebnis_label.pack(pady=(0, 20))

        # Kleine Statistik nach Kategorien.
        statistik = self.kategorien_statistik_bauen()

        statistik_frame = ttk.LabelFrame(self.main_frame, text="Statistik nach Kategorien", padding=15)
        statistik_frame.pack(fill="x", pady=10)

        if not statistik:
            ttk.Label(statistik_frame, text="Keine Statistik verfügbar.").pack(anchor="w")
        else:
            for kategorie, daten in statistik.items():
                gesamt = daten["gesamt"]
                richtig = daten["richtig"]
                quote = (richtig / gesamt * 100) if gesamt else 0
                text = f"{kategorie}: {richtig}/{gesamt} richtig ({quote:.2f}%)"
                ttk.Label(statistik_frame, text=text).pack(anchor="w", pady=2)

        # Die Buttons werden zuerst erzeugt und DANACH befüllt.
        # So vermeiden wir den Fehler, dass button_frame benutzt wird,
        # bevor es überhaupt existiert.
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=20)

        erneut_button = ttk.Button(
            button_frame,
            text="Nochmal spielen",
            command=self.quiz_starten
        )
        erneut_button.grid(row=0, column=0, padx=10)

        startseite_button = ttk.Button(
            button_frame,
            text="Zur Startseite",
            command=self.zeige_startseite
        )
        startseite_button.grid(row=0, column=1, padx=10)

        # Nur in der normalen Runde und nur dann, wenn es falsche Fragen gibt,
        # zeigen wir den Wiederholen-Button an.
        if self.falsche_fragen and not self.ist_wiederholungsrunde:
            wiederholen_button = ttk.Button(
                button_frame,
                text="Falsche Fragen wiederholen",
                command=self.falsche_fragen_wiederholen
            )
            wiederholen_button.grid(row=0, column=2, padx=10)

    # ------------------------------------------------------------
    # KATEGORIE-STATISTIK
    # ------------------------------------------------------------
    def kategorien_statistik_bauen(self) -> Dict[str, Dict[str, int]]:
        """
        Baut eine kleine Statistik auf Basis der gespeicherten Details.

        Rückgabe-Beispiel:
        {
            "Datentypen": {"gesamt": 3, "richtig": 2},
            "Strings": {"gesamt": 2, "richtig": 1}
        }
        """
        statistik: Dict[str, Dict[str, int]] = {}

        for eintrag in self.details:
            kategorie = eintrag["kategorie"]

            # Falls die Kategorie noch nicht im Dict ist, legen wir sie an.
            if kategorie not in statistik:
                statistik[kategorie] = {"gesamt": 0, "richtig": 0}

            statistik[kategorie]["gesamt"] += 1

            if eintrag["ist_richtig"]:
                statistik[kategorie]["richtig"] += 1

        return statistik

    def falsche_fragen_wiederholen(self) -> None:
        """
        Startet eine neue Runde nur mit den zuvor falsch beantworteten Fragen.
        """
        if not self.falsche_fragen:
            messagebox.showinfo(
                "Keine falschen Fragen",
                "Es gibt keine falschen Fragen zum Wiederholen."
            )
            return

        # Neue Quizliste nur aus den falschen Fragen erzeugen.
        self.quiz_fragen = self.falsche_fragen.copy()
        random.shuffle(self.quiz_fragen)

        # Zustand für die Wiederholungsrunde zurücksetzen.
        self.aktuelle_frage_index = 0
        self.punktestand = 0
        self.details = []
        self.ist_wiederholungsrunde = True

        # Liste leeren, damit die Wiederholungsrunde einen frischen Start hat.
        # Wenn in der Wiederholungsrunde wieder Fehler passieren, werden nur diese
        # neuen Fehler erneut gesammelt.
        self.falsche_fragen = []

        self.zeige_aktuelle_frage()


# ------------------------------------------------------------
# PROGRAMMSTART
# ------------------------------------------------------------
# Dieser Teil wird nur ausgeführt, wenn die Datei direkt gestartet wird.
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGUI(root)
    root.mainloop()
