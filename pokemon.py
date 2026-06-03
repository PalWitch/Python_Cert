import random

class Angriff:
    def __init__(self, name, schaden):
        self.name = name
        self.schaden = schaden

    def __str__(self):
        return f"{self.name} ({self.schaden} Schaden)"


class Pokemon:
    def __init__(self, name, hp, angriffe):
        self.name = name
        self.hp = hp
        self.angriffe = angriffe

    def ist_besiegt(self):
        return self.hp <= 0

    def greife_an(self, ziel, angriff):
        ziel.hp -= angriff.schaden
        return f"{self.name} benutzt {angriff.name}! {ziel.name} verliert {angriff.schaden} HP."


# Vererbung: konkrete Pokemon-Klassen
class Pikachu(Pokemon):
    def __init__(self):
        super().__init__(
            "Pikachu",
            100,
            [
                Angriff("Donnerschock", 18),
                Angriff("Ruckzuckhieb", 12),
                Angriff("Volt tackle", 22),
                Angriff("Knurren", 8)
            ]
        )


class Glumanda(Pokemon):
    def __init__(self):
        super().__init__(
            "Glumanda",
            95,
            [
                Angriff("Glut", 16),
                Angriff("Kratzer", 10),
                Angriff("Flammenwurf", 24),
                Angriff("Biss", 14)
            ]
        )


class Schiggy(Pokemon):
    def __init__(self):
        super().__init__(
            "Schiggy",
            110,
            [
                Angriff("Aquaknarre", 17),
                Angriff("Tackle", 10),
                Angriff("Blubber", 13),
                Angriff("Kopfnuss", 15)
            ]
        )


class Bisasam(Pokemon):
    def __init__(self):
        super().__init__(
            "Bisasam",
            105,
            [
                Angriff("Rankenhieb", 16),
                Angriff("Tackle", 10),
                Angriff("Rasierblatt", 20),
                Angriff("Samenbomben", 18)
            ]
        )


class GameState:
    def __init__(self, pokemon_pool):
        self.spieler_pkm = random.choice(pokemon_pool)()
        self.gegner_pkm = random.choice(pokemon_pool)()
        self.aktiver_spieler = "spieler"

    def status_anzeigen(self):
        print("\n--- Kampfstatus ---")
        print(f"Spieler: {self.spieler_pkm.name} | HP: {max(0, self.spieler_pkm.hp)}")
        print(f"Gegner:  {self.gegner_pkm.name} | HP: {max(0, self.gegner_pkm.hp)}")
        print("-------------------")

    def spieler_zug(self):
        print(f"\nDu bist dran! Wähle einen Angriff für {self.spieler_pkm.name}:")
        for i, angriff in enumerate(self.spieler_pkm.angriffe, start=1):
            print(f"{i}. {angriff}")

        while True:
            auswahl = input("Deine Wahl (1-4): ")
            if auswahl in ["1", "2", "3", "4"]:
                angriff = self.spieler_pkm.angriffe[int(auswahl) - 1]
                print(self.spieler_pkm.greife_an(self.gegner_pkm, angriff))
                break
            else:
                print("Ungültige Eingabe. Bitte 1 bis 4 eingeben.")

    def computer_zug(self):
        print(f"\nDer Gegner ist dran...")
        angriff = random.choice(self.gegner_pkm.angriffe)
        print(self.gegner_pkm.greife_an(self.spieler_pkm, angriff))

    def spielen(self):
        print("Das Spiel startet!")
        print(f"Spieler-Pokemon: {self.spieler_pkm.name}")
        print(f"Gegner-Pokemon: {self.gegner_pkm.name}")

        while True:
            self.status_anzeigen()

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


pokemon_pool = [Pikachu, Glumanda, Schiggy, Bisasam]

spiel = GameState(pokemon_pool)
spiel.spielen()