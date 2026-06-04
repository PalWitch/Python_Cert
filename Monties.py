import random


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
        self.kp = kp
        self.ap = ap
        self.angriffe = angriffe

    def ist_besiegt(self):
        return self.kp <= 0

    def hat_noch_angriff(self):
        return any(angriff.kosten <= self.ap for angriff in self.angriffe)

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
            110,
            45,
            [
                Angriff("Donner", 18, 9),
                Angriff("Hieb", 12, 6),
                Angriff("Voltschlag", 20, 10),
                Angriff("Knurren", 8, 4)
            ]
        )


class Feurina(Monties):
    def __init__(self):
        super().__init__(
            "Feurina",
            100,
            45,
            [
                Angriff("Glut", 16, 8),
                Angriff("Kratzer", 8, 5),
                Angriff("Flammenwurf", 20, 10),
                Angriff("Biss", 14, 7)
            ]
        )


class Aprilia(Monties):
    def __init__(self):
        super().__init__(
            "Aprilia",
            110,
            45,
            [
                Angriff("Wassercolt", 17, 9),
                Angriff("Rempler", 10, 5),
                Angriff("Blubstrahl", 13, 7),
                Angriff("Kopfnuss", 15, 8)
            ]
        )


class Florus(Monties):
    def __init__(self):
        super().__init__(
            "Florus",
            105,
            45,
            [
                Angriff("Wurzelschlag", 16, 6),
                Angriff("Rempler", 10, 3),
                Angriff("Schneidblatt", 20, 8),
                Angriff("Saat", 18, 7)
            ]
        )


class GameState:
    def __init__(self, monties_pool):
        self.spieler_pkm = random.choice(monties_pool)()
        self.gegner_pkm = random.choice(monties_pool)()
        self.aktiver_spieler = "spieler"

    def status_anzeigen(self):
        print("\n--- Kampfstatus ---")
        print(
            f"Spieler: {self.spieler_pkm.name} | "
            f"KP: {self.spieler_pkm.kp} | AP: {self.spieler_pkm.ap}"
        )
        print(
            f"Gegner: {self.gegner_pkm.name} | "
            f"KP: {self.gegner_pkm.kp} | AP: {self.gegner_pkm.ap}"
        )
        print("-------------------")

    def spieler_zug(self):
        if not self.spieler_pkm.hat_noch_angriff():
            print(f"\n{self.spieler_pkm.name} hat keine AP mehr für einen Angriff und verliert seinen Zug!")
            return

        print(f"\nDu bist dran! Wähle einen Angriff für {self.spieler_pkm.name}:")

        gueltige_wahlen = []

        for i, angriff in enumerate(self.spieler_pkm.angriffe, start=1):
            if angriff.kosten > self.spieler_pkm.ap:
                print(f"{i}. ({angriff}) [zu teuer]")
            else:
                print(f"{i}. {angriff}")
                gueltige_wahlen.append(str(i))

        while True:
            auswahl = input("Deine Wahl: ")

            if auswahl in gueltige_wahlen:
                angriff = self.spieler_pkm.angriffe[int(auswahl) - 1]
                print(self.spieler_pkm.greife_an(self.gegner_pkm, angriff))
                break
            elif auswahl in ["1", "2", "3", "4"]:
                print("Diesen Angriff kannst du dir gerade nicht leisten.")
            else:
                print("Ungültige Eingabe. Bitte wähle eine verfügbare Zahl.")

    def computer_zug(self):
        print("\nDer Gegner ist dran...")

        moegliche_angriffe = [
            angriff for angriff in self.gegner_pkm.angriffe
            if angriff.kosten <= self.gegner_pkm.ap
        ]

        if not moegliche_angriffe:
            print(f"{self.gegner_pkm.name} hat keine AP mehr für einen Angriff und verliert seinen Zug!")
            return

        angriff = random.choice(moegliche_angriffe)
        print(self.gegner_pkm.greife_an(self.spieler_pkm, angriff))

    def pruefe_ap_sackgasse(self):
        return (
            not self.spieler_pkm.hat_noch_angriff()
            and not self.gegner_pkm.hat_noch_angriff()
        )

    def ende_bei_ap_sackgasse(self):
        print("\nBeide Monties haben keine AP mehr für Angriffe!")

        if self.spieler_pkm.kp > self.gegner_pkm.kp:
            print("Du gewinnst nach verbleibenden KP!")
        elif self.spieler_pkm.kp < self.gegner_pkm.kp:
            print("Der Computer gewinnt nach verbleibenden KP!")
        else:
            print("Der Kampf endet unentschieden!")

    def spielen(self):
        print("Das Spiel startet!")
        print(f"Spieler-Montie: {self.spieler_pkm.name}")
        print(f"Gegner-Montie: {self.gegner_pkm.name}")

        while True:
            self.status_anzeigen()

            if self.pruefe_ap_sackgasse():
                self.ende_bei_ap_sackgasse()
                break

            if self.aktiver_spieler == "spieler":
                self.spieler_zug()
                if self.gegner_pkm.ist_besiegt():
                    self.status_anzeigen()
                    print(f"\n{self.gegner_pkm.name} wurde besiegt. Du gewinnst!")
                    break
                self.aktiver_spieler = "gegner"

            else:
                self.computer_zug()
                if self.spieler_pkm.ist_besiegt():
                    self.status_anzeigen()
                    print(f"\n{self.spieler_pkm.name} wurde besiegt. Der Computer gewinnt!")
                    break
                self.aktiver_spieler = "spieler"


monties_pool = [Matchu, Feurina, Aprilia, Florus]

spiel = GameState(monties_pool)
spiel.spielen()