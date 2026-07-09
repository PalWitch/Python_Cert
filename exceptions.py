######################
# Exception Handling #
######################
'''NIEMALS BaseExceptions fangen!'''

# ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Fehler: {e}")  # Fehler: division by zero

# IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as e:
    print(f"Fehler: {e}")  # Fehler: list index out of range

# KeyError
try:
    my_dict = {"a": 1, "b": 2}
    print(my_dict["c"])
except KeyError as e:
    print(f"Fehler: {e}")  # Fehler: 'c'

# ValueError
try:
    num = int("abc")
except ValueError as e:
    print(f"Fehler: {e}")  # Fehler: invalid literal for int() with base 10: 'abc'

# TypeError
try:
    result = "5" + 3
except TypeError as e:
    print(f"Fehler: {e}")  # Fehler: can only concatenate str (not "int") to str

# FileNotFoundError
try:
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"Fehler: {e}")  # Fehler: [Errno 2] No such file or directory: 'non_existent_file.txt'

# Eigene Exception definieren
class AlterUngueltigError(Exception):
    pass

def pruefe_alter(alter):
    if alter < 0 or alter > 150:
        raise AlterUngueltigError(f"Ungültiges Alter: {alter}")
    print("Alter gültig")

for alter in [25, -3, 200]:
    try:
        pruefe_alter(alter)
    except AlterUngueltigError as e:
        print(e)
'''
Ausgabe:

Alter gültig
Ungültiges Alter: -3
Ungültiges Alter: 200

Eigene Exceptions erben von Exception (oder einer spezifischeren Klasse). 
Die Fehlermeldung wird als Argument an den Konstruktor übergeben und ist über str(e) abrufbar.
'''

# raise zur Eingabevalidierung
def berechne_durchschnitt(noten):
    if not noten:
        raise ValueError("Notenliste darf nicht leer sein")
    for note in noten:
        if note < 1 or note > 6:
            raise ValueError(f"Ungültige Note: {note}")
    return sum(noten) / len(noten)

testfaelle = [[1, 2, 3], [], [1, 7, 3]]

for noten in testfaelle:
    try:
        ergebnis = berechne_durchschnitt(noten)
        print(f"{noten} → Durchschnitt: {ergebnis}")
    except ValueError as e:
        print(f"{noten} → Fehler: {e}")

'''
Ausgabe:

[1, 2, 3] → Durchschnitt: 2.0
[] → Fehler: Notenliste darf nicht leer sein
[1, 7, 3] → Fehler: Ungültige Note: 7

Mit raise kann man Fehler aktiv auslösen, um ungültige Eingaben frühzeitig abzufangen.
'''

# Exceptions – Alles kombiniert
class BestellFehler(Exception):
    pass

def bestelle(produkt, menge):
    if not isinstance(produkt, str):
        raise TypeError(f"Produkt muss ein String sein, nicht {type(produkt).__name__}")
    if not isinstance(menge, int):
        raise TypeError(f"Menge muss ein int sein, nicht {type(menge).__name__}")
    if menge <= 0:
        raise BestellFehler("Menge muss positiv sein")
    return f"Bestellung: {menge}x {produkt}"

testfaelle = [("Apfel", 3), ("Apfel", -1), (123, 3), ("Apfel", "zwei")]

for produkt, menge in testfaelle:
    try:
        ergebnis = bestelle(produkt, menge)
        print(ergebnis)
    except BestellFehler as e:
        print(f"BestellFehler: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")

'''
Ausgabe:

Bestellung: 3x Apfel
BestellFehler: Menge muss positiv sein
TypeError: Produkt muss ein String sein, nicht int
TypeError: Menge muss ein int sein, nicht str

Hier kommen alle Konzepte zusammen:

    Eigene Exception (BestellFehler) für fachliche Fehler
    raise zur Validierung der Eingaben
    Mehrere except-Blöcke für verschiedene Fehlertypen
    Eingebaute Exceptions (TypeError) für Typprüfungen
'''


# Score prüfen
class InvalidScoreError(Exception):
    pass

def add_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError("Score muss zwischen 0 und 100 liegen")
    return "ok"


# Gezielt abfangen
try:
    add_score(120)
except InvalidScoreError as error:
    print("Ungültiger Score:", error)
except Exception as error:
    print("Anderer Fehler:", error)


# Exception mit Nachricht
class InvalidAgeError(Exception):
    pass

def register(age):
    if age < 18:
        raise InvalidAgeError("Alter muss mindestens 18 sein")
    return "registriert"


# Eigene Exception nutzen
class NotPositiveError(Exception):
    pass

def parse_positive_int(text):
    zahl = int(text)
    if zahl <= 0:
        raise NotPositiveError("Zahl muss positiv sein")
    return zahl