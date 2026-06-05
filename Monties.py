import random
import sys
import time

AP_REGEN_PRO_RUNDE = 3
SAMMELN_AP = 6
BALKEN_BREITE = 20


class Angriff:
    def __init__(self, name, schaden, kosten):
        self.name = name
        self.schaden = schaden
        self.kosten = kosten

    def __str__(self):
        return f"{self.name} ({self.schaden} Schaden, {self.kosten} AP)"


class Monties:
    def __init__(self, name, kp, ap, angriffe):
        self.name = name
        self.max_kp = kp
        self.kp = kp
        self.max_ap = ap
        self.ap = ap
        self.angriffe = angriffe

    def ist_besiegt(self):
        return self.kp <= 0

    def hat_noch_angriff(self):
        return any(angriff.kosten <= self.ap for angriff in self.angriffe)

    def regeneriere_ap(self, menge=AP_REGEN_PRO_RUNDE):
        alt = self.ap
        self.ap = min(self.max_ap, self.ap + menge)
        return self.ap - alt

    def sammeln(self, menge=SAMMELN_AP):
        alt = self.ap
        self.ap = min(self.max_ap, self.ap + menge)
        return self.ap - alt

    def greife_an(self, ziel, angriff):
        if self.ap < angriff.kosten:
            return f"{self.name} hat nicht genug AP für {angriff.name} und verliert seinen Zug!"

        ziel.kp -= angriff.schaden
        self.ap -= angriff.kosten

        if ziel.kp < 0:
            ziel.kp = 0

        return (
            f"{self.name} benutzt {angriff.name}! "
            f"{ziel.name} verliert {angriff.schaden} KP. "
            f"{self.name} verbraucht {angriff.kosten} AP."
        )


class Matchu(Monties):
    def __init__(self):
        super().__init__(
            "Matchu",
            115,
            40,
            [
                Angriff("Knurren", 7, 3),
                Angriff("Hieb", 10, 5),
                Angriff("Donner", 17, 8),
                Angriff("Voltschlag", 22, 11),
            ],
        )


class Feurina(Monties):
    def __init__(self):
        super().__init__(
            "Feurina",
            100,
            42,
            [
                Angriff("Kratzer", 9, 4),
                Angriff("Biss", 13, 6),
                Angriff("Glut", 16, 8),
                Angriff("Flammenwurf", 21, 11),
            ],
        )


class Aprilia(Monties):
    def __init__(self):
        super().__init__(
            "Aprilia",
            110,
            44,
            [
                Angriff("Rempler", 9, 4),
                Angriff("Blubstrahl", 13, 6),
                Angriff("Kopfnuss", 15, 8),
                Angriff("Wassercolt", 18, 9),
            ],
        )


class Florus(Monties):
    def __init__(self):
        super().__init__(
            "Florus",
            108,
            41,
            [
                Angriff("Rempler", 8, 4),
                Angriff("Wurzelschlag", 14, 7),
                Angriff("Saat", 17, 9),
                Angriff("Schneidblatt", 20, 11),
            ],
        )


def langsam_schreiben(text, delay=0.02):
    for zeichen in text:
        print(zeichen, end="", flush=True)
        time.sleep(delay)
    print()


def punkte_animation(text, punkte=3, delay=0.3):
    print(text, end="", flush=True)
    for _ in range(punkte):
        time.sleep(delay)
        print(".", end="", flush=True)
    print()


def frame_animation(frames, delay=0.35):
    for frame in frames:
        print("\r" + frame + " " * 12, end="", flush=True)
        time.sleep(delay)
    print("\n")


def sieg_animation():
    frame_animation(
        [
            "🏆 SIEG!",
            "✨ 🏆 SIEG! ✨",
            "🎉 ✨ 🏆 SIEG! ✨ 🎉",
        ],
        delay=0.4,
    )


def niederlage_animation():
    frame_animation(
        [
            "☠️ Niederlage...",
            "💀 Niederlage...",
            "⚰️ Niederlage...",
        ],
        delay=0.45,
    )


def unentschieden_animation():
    frame_animation(
        [
            "🤝 Unentschieden!",
            "⚖️  Unentschieden!",
            "🤝 Kampf ohne Sieger!",
        ],
        delay=0.4,
    )


def balken(wert, maximum, breite=BALKEN_BREITE, voll="█", leer="░"):
    maximum = max(1, maximum)
    gefuellt = int((wert / maximum) * breite)
    return voll * gefuellt + leer * (breite - gefuellt)


class GameState:
    def __init__(self, monties_pool):
        self.spieler_pkm = random.choice(monties_pool)()
        self.gegner_pkm = random.choice(monties_pool)()
        while self.gegner_pkm.name == self.spieler_pkm.name:
            self.gegner_pkm = random.choice(monties_pool)()
        self.aktiver_spieler = "spieler"

    def status_anzeigen(self):
        print("\n" + "=" * 48)
        print(f"⚔️  {self.spieler_pkm.name} vs. {self.gegner_pkm.name}")
        print("=" * 48)
        print(f"🧑 Spieler: {self.spieler_pkm.name}")
        print(
            f"KP [{balken(self.spieler_pkm.kp, self.spieler_pkm.max_kp)}] "
            f"{self.spieler_pkm.kp}/{self.spieler_pkm.max_kp}"
        )
        print(
            f"AP [{balken(self.spieler_pkm.ap, self.spieler_pkm.max_ap)}] "
            f"{self.spieler_pkm.ap}/{self.spieler_pkm.max_ap}"
        )
        print("-" * 48)
        print(f"🤖 Gegner:  {self.gegner_pkm.name}")
        print(
            f"KP [{balken(self.gegner_pkm.kp, self.gegner_pkm.max_kp)}] "
            f"{self.gegner_pkm.kp}/{self.gegner_pkm.max_kp}"
        )
        print(
            f"AP [{balken(self.gegner_pkm.ap, self.gegner_pkm.max_ap)}] "
            f"{self.gegner_pkm.ap}/{self.gegner_pkm.max_ap}"
        )
        print("=" * 48)

    def zug_ende(self, montie):
        gewonnen = montie.regeneriere_ap()
        if gewonnen > 0:
            print(f"🔋 {montie.name} regeneriert {gewonnen} AP.")

    def angriffs_animation(self, name, angriff_name):
        punkte_animation(f"\n{name} setzt {angriff_name} ein", delay=0.25)

    def spieler_zug(self):
        print(f"\nDu bist dran! Wähle einen Angriff für {self.spieler_pkm.name}:")
        print("0. Sammeln (+6 AP, kein Schaden)")

        gueltige_wahlen = ["0"]

        for i, angriff in enumerate(self.spieler_pkm.angriffe, start=1):
            if angriff.kosten > self.spieler_pkm.ap:
                print(f"{i}. ({angriff}) [zu teuer]")
            else:
                print(f"{i}. {angriff}")
                gueltige_wahlen.append(str(i))

        while True:
            auswahl = input("Deine Wahl: ").strip()

            if auswahl == "0":
                gewonnen = self.spieler_pkm.sammeln()
                print(f"\n🌀 {self.spieler_pkm.name} sammelt Energie und erhält {gewonnen} AP!")
                break
            if auswahl in gueltige_wahlen:
                angriff = self.spieler_pkm.angriffe[int(auswahl) - 1]
                self.angriffs_animation(self.spieler_pkm.name, angriff.name)
                langsam_schreiben(self.spieler_pkm.greife_an(self.gegner_pkm, angriff), delay=0.018)
                break
            if auswahl in ["1", "2", "3", "4"]:
                print("Diesen Angriff kannst du dir gerade nicht leisten.")
            else:
                print("Ungültige Eingabe. Bitte wähle eine verfügbare Zahl.")

        self.zug_ende(self.spieler_pkm)

    def computer_zug(self):
        print("\nDer Gegner ist dran...")

        moegliche_angriffe = [
            angriff for angriff in self.gegner_pkm.angriffe if angriff.kosten <= self.gegner_pkm.ap
        ]

        if not moegliche_angriffe or (self.gegner_pkm.ap <= 6 and random.random() < 0.4):
            gewonnen = self.gegner_pkm.sammeln()
            print(f"🌀 {self.gegner_pkm.name} sammelt Energie und erhält {gewonnen} AP!")
            self.zug_ende(self.gegner_pkm)
            return

        angriff = random.choice(moegliche_angriffe)
        self.angriffs_animation(self.gegner_pkm.name, angriff.name)
        langsam_schreiben(self.gegner_pkm.greife_an(self.spieler_pkm, angriff), delay=0.018)
        self.zug_ende(self.gegner_pkm)

    def ende_bei_sackgasse(self):
        print("\nBeide Monties können gerade nichts Entscheidendes ausrichten.")
        if self.spieler_pkm.kp > self.gegner_pkm.kp:
            langsam_schreiben("Du gewinnst nach verbleibenden KP!", delay=0.03)
            sieg_animation()
        elif self.spieler_pkm.kp < self.gegner_pkm.kp:
            langsam_schreiben("Der Computer gewinnt nach verbleibenden KP!", delay=0.03)
            niederlage_animation()
        else:
            langsam_schreiben("Der Kampf endet unentschieden!", delay=0.03)
            unentschieden_animation()

    def spielen(self):
        langsam_schreiben("Das Spiel startet!", delay=0.03)
        print(f"Spieler-Montie: {self.spieler_pkm.name}")
        print(f"Gegner-Montie: {self.gegner_pkm.name}")

        runden_zaehler = 1

        while True:
            print(f"\n🧭 Runde {runden_zaehler}")
            self.status_anzeigen()

            if runden_zaehler >= 30:
                self.ende_bei_sackgasse()
                break

            if self.aktiver_spieler == "spieler":
                self.spieler_zug()
                if self.gegner_pkm.ist_besiegt():
                    self.status_anzeigen()
                    langsam_schreiben(f"\n{self.gegner_pkm.name} wurde besiegt. Du gewinnst!", delay=0.03)
                    sieg_animation()
                    break
                self.aktiver_spieler = "gegner"
            else:
                self.computer_zug()
                if self.spieler_pkm.ist_besiegt():
                    self.status_anzeigen()
                    langsam_schreiben(
                        f"\n{self.spieler_pkm.name} wurde besiegt. Der Computer gewinnt!",
                        delay=0.03,
                    )
                    niederlage_animation()
                    break
                self.aktiver_spieler = "spieler"
                runden_zaehler += 1


def main():
    monties_pool = [Matchu, Feurina, Aprilia, Florus]
    spiel = GameState(monties_pool)
    spiel.spielen()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSpiel beendet.")
        sys.exit(0)