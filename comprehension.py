# ----------------------------------------
# Was ist eine List-Comprehension?
# ----------------------------------------
# Eine kurze Schreibweise, um Listen zu erstellen.
# Statt einer normalen for-Schleife kannst du alles in eine Zeile packen.

# Beispiel 1: Zahlen von 0 bis 9
zahlen = [i for i in range(10)]
print("Zahlen 0-9:", zahlen)


# ----------------------------------------
# Vergleich: normale Schleife vs. Comprehension
# ----------------------------------------

# Normale Variante:
quadrate_alt = []
for i in range(5):
    quadrate_alt.append(i ** 2)

# List-Comprehension:
quadrate_neu = [i ** 2 for i in range(5)]

print("Quadrate (alt):", quadrate_alt)
print("Quadrate (neu):", quadrate_neu)


# ----------------------------------------
# Mit Bedingung (if)
# ----------------------------------------
# Nur gerade Zahlen (also durch 2 teilbar)

gerade = [i for i in range(10) if i % 2 == 0]
print("Gerade Zahlen:", gerade)


# ----------------------------------------
# Mit if/else in der Comprehension
# ----------------------------------------
# Wenn Zahl gerade → "even", sonst "odd"

even_odd = ["even" if i % 2 == 0 else "odd" for i in range(5)]
print("Even/Odd:", even_odd)


# ----------------------------------------
# Strings bearbeiten
# ----------------------------------------
# Alle Buchstaben groß machen

namen = ["anna", "bob", "charlie"]
gross = [name.upper() for name in namen]

print("Groß geschrieben:", gross)


# ----------------------------------------
# Verschachtelte Schleifen
# ----------------------------------------
# Kombinationen von zwei Listen

liste1 = [1, 2, 3]
liste2 = ["a", "b"]

kombi = [(x, y) for x in liste1 for y in liste2]
print("Kombinationen:", kombi)


# ----------------------------------------
# Mini-Merkhilfe:
# ----------------------------------------
# [Ergebnis for Element in Liste if Bedingung]
#
# Beispiel:
# [i*2 for i in range(5) if i > 2]


# Quadrate erstellen
quadrate = [i ** 2 for i in range(1, 11)]
print("Quadrate 1-10:", quadrate)

# Zeichenkettenlängen
wortlaengen = [len(wort) for wort in ["Die", "Sonne", "scheint"]]
print("Längen der Wörter:", wortlaengen)

# Absolute Werte
absolute = [abs(i) for i in [-1, -2, 3, -4, 5]]
print("Absolute Werte:", absolute)

# String in Großbuchstaben
grossbuchstaben = [s.upper() for s in ["Die", "Sonne", "scheint"]]
print("Großbuchstaben:", grossbuchstaben)

# Wurzeln ziehen
wurzeln = [i ** 0.5 for i in [1, 4, 9, 16, 25]]
print("Quadratwurzeln:", wurzeln)

# Tupel erstellen
tupel_liste = [(i, i * i) for i in range(1, 11)]
print("Tupel (Zahl, Quadrat):", tupel_liste)

# Teile von Strings
erste_zeichen = [wort[0] for wort in ["Die", "Sonne", "scheint"]]
print("Erste Zeichen:", erste_zeichen)

# Durchschnittswerte
liste = [1,2,5,5,2,-2]
durchschnitt = [(liste[i] + liste[i + 1]) / 2 for i in range(len(liste) - 1)]  
print("Durchschnittswerte:", durchschnitt)


# Gerade Zahlen
gerade = [i for i in range(1, 21) if not i % 2]
print("Gerade Zahlen 1-20:", gerade)

# Filtern nach Bedingung
teilbar_durch_3 = [i for i in range(1, 21) if i % 3 == 0]
print("Zahlen 1-20, die durch 3 teilbar sind:", teilbar_durch_3)

# Nicht-leere Strings
nicht_leer = [s for s in ["Sonne", "", "scheint", ""] if s]
print("Nicht-leere Strings:", nicht_leer)

# Fizz Buzz
fizz_buzz = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for
             i in range(1, 16)]
print("FizzBuzz 1-15:", fizz_buzz)


# Bedingung fehlt
result = [(i, j) for i in range(1, 11) for j in range(1, 11) if i + j == 10]
print("Zahlenpaare, deren Summe 10 ergibt:", result)

# Liste von Listen abflachen
flache_liste = [element for sublist in [[1, 2], [3, 4], [5, 6]] for element in sublist]
print("Abgeflachte Liste:", flache_liste)

# Verschachtelung
# a = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3)]
a = [(i,j) for i in range(2) for j in range(4)]
print(a)
# b = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6], [0, 3, 6, 9]]
b = [[i*j for i in range(4)] for j in range(4)]
print(b)
# c = [['aA', 'bA', 'cA'], ['aB', 'bB', 'cB'], ['aC', 'bC', 'cC']]
c = [[i+j for i in "abc"] for j in "ABC"]
print(c)


# Dictionary Comprehensions
# a = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
a = {i: i * i for i in range(1, 11)}
# b = {'Hase': ['H', 'a', 's', 'e'], 'Hund': ['H', 'u', 'n', 'd']}
words = ['Hase', 'Hund']
b = {word: [letter for letter in word] for word in words}
# Tausche die Keys und Values in folgendem Dicitonary
# swapped_my_dict = {1: 'A', 2: 'B', 3: 'C'}
my_dict = {'A': 1, 'B': 2, 'C': 3}
gedreht_my_dict = {v: k for k, v in my_dict.items()}


# List Comprehension – Grundform
'''
Erstelle mit einer List Comprehension eine Liste, die die ersten 10 Vielfachen von 7 enthält (also [7, 14, 21, ..., 70]).
'''
vielfache = [7 * i for i in range(1, 11)]
print(vielfache)  # [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]


# List Comprehension – mit Filter
'''
Gegeben ist eine Liste von Namen:

namen = ["Anna", "Bo", "Christina", "Ed", "Friedrich", "Gia"]

Erstelle mit einer List Comprehension eine neue Liste, die nur die Namen enthält, die mehr als 3 Zeichen haben.
'''
namen = ["Anna", "Bo", "Christina", "Ed", "Friedrich", "Gia"]

lange_namen = [name for name in namen if len(name) > 3]
print(lange_namen)  # ['Anna', 'Christina', 'Friedrich']


# Set Comprehension – Grundform
'''
Gegeben ist eine Liste von Wörtern:

woerter = ["Python", "programmieren", "Pasta", "lernen", "Praxis"]

Erstelle mit einer Set Comprehension ein Set, das alle Anfangsbuchstaben (in Kleinbuchstaben) enthält.
'''
woerter = ["Python", "programmieren", "Pasta", "lernen", "Praxis"]

anfang = {w[0].lower() for w in woerter}
print(anfang)  # {'p', 'l'}
'''
Da ein Set keine Duplikate enthält, kommt 'p' nur einmal vor, obwohl drei Wörter mit P beginnen.
'''

# Set Comprehension – mit Filter
'''
Gegeben ist eine Liste von Zahlen (mit Duplikaten):

zahlen = [3, -1, 4, -1, 5, 9, -2, 6, 5, 3, -5]

Erstelle mit einer Set Comprehension ein Set, das nur die positiven Zahlen enthält (ohne Duplikate).
'''
zahlen = [3, -1, 4, -1, 5, 9, -2, 6, 5, 3, -5]

positiv = {x for x in zahlen if x > 0}
print(positiv)  # {3, 4, 5, 6, 9}


# Dict Comprehension – Grundform
'''
Gegeben ist eine Liste von Städten:

staedte = ["Berlin", "Hamburg", "München", "Köln"]

Erstelle mit einer Dict Comprehension ein Dictionary, das jede Stadt als Key und die Länge des Namens als Value enthält.
'''
staedte = ["Berlin", "Hamburg", "München", "Köln"]

laengen = {stadt: len(stadt) for stadt in staedte}
print(laengen)  # {'Berlin': 6, 'Hamburg': 7, 'München': 7, 'Köln': 4}


# Dict Comprehension – mit Filter
'''
Gegeben ist ein Dictionary mit Produktpreisen:

preise = {"Laptop": 999, "Maus": 25, "Monitor": 349, "Kabel": 8, "Tastatur": 65}

Erstelle mit einer Dict Comprehension ein neues Dictionary, das nur Produkte enthält, die mehr als 50 Euro kosten.
'''
preise = {"Laptop": 999, "Maus": 25, "Monitor": 349, "Kabel": 8, "Tastatur": 65}

teuer = {produkt: preis for produkt, preis in preise.items() if preis > 50}
print(teuer)  # {'Laptop': 999, 'Monitor': 349, 'Tastatur': 65}


# Nested Comprehension – Lesen & Verstehen
'''
Lies den folgenden Code und beantworte die Fragen ohne ihn auszuführen:

farben = ["rot", "blau"]
groessen = ["S", "M", "L"]

kombinationen = [f"{f}-{g}" for f in farben for g in groessen]
print(kombinationen)

    Was gibt print(kombinationen) aus?
    Wie viele Elemente hat die Liste?
    Schreibe den Code als verschachtelte for-Schleife um.

Tipp

Lies die Comprehension von links nach rechts:

    f"{f}-{g}" → was wird pro Element erzeugt?
    for f in farben → äußere Schleife
    for g in groessen → innere Schleife
'''

# 1. Ausgabe:

['rot-S', 'rot-M', 'rot-L', 'blau-S', 'blau-M', 'blau-L']

# 2. Anzahl: 6 Elemente (2 Farben × 3 Größen)

# 3. Als verschachtelte Schleife:

farben = ["rot", "blau"]
groessen = ["S", "M", "L"]

kombinationen = []
for f in farben:
    for g in groessen:
        kombinationen.append(f"{f}-{g}")

print(kombinationen)
'''
Die Reihenfolge der for-Klauseln in der Comprehension entspricht der Verschachtelung der Schleifen: 
Die äußere Schleife (for f in farben) steht zuerst, die innere (for g in groessen) danach.
'''