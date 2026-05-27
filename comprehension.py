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