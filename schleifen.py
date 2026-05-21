###################
# Schlüsselwörter #
###################

# break #
''' wird verwendet, um die Schleifen an einer definierten Stelle zu unterbrechen
    for i in range(0, 10):
    print(i)
    if i == 5:
        break
    print("Ende")
'''

# continue #
''' wird verwendet, um einen bestimmten Durchlauf zu skippen
    for i in range(0, 10):
    if 3 <= i <= 5:
        continue
    print(i)
'''

###################
# while-Schleifen #
# #################
''' Die while-Schleife wird so lange ausgeführt, wie eine angegebene 
    Bedingung wahr ist. Sie wird verwendet, wenn die Anzahl der 
    Schleifendurchläufe im Voraus nicht bekannt ist.
'''

# Summe von 1 bis 100
summe = 0
zahl = 1
while zahl <= 100:
    summe += zahl
    zahl += 1
print(summe)

# Input erfragen
antwort = ""
while antwort != "stop":
    antwort = input("Bitte etwas eingeben (stop zum Beenden): ")
    print("Du hast eingegeben:", antwort)

# Fakultät
zahl = 5
fakultaet = 1
zaehler = 1
while zaehler <= zahl:
    fakultaet *= zaehler
    zaehler += 1
print(f"Die Fakultät von {zahl} ist {fakultaet}")

# Fast endlose Schleife
zaehler = 1
while True:
    print(zaehler)
    zaehler += 1
    if zaehler > 10:
        break

# Fibonacci
anzahl = 10
a = 0
b = 1
zaehler = 0
while zaehler < anzahl:
    print(a)
    naechste_zahl = a + b
    a = b
    b = naechste_zahl
    zaehler += 1

#################
# for-Schleifen #
#################
'''Die for-Schleife wird verwendet, um über eine Sequenz 
   (z. B. eine Liste, ein Tupel oder eine Zeichenkette) zu 
   iterieren und den Codeblock für jedes Element in der Sequenz auszuführen.
'''

# Zählen
for zahl in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(zahl)

# Städtetrip
staedte = ["Berlin", "Paris", "London", "New York"]
for stadt in staedte:
    print(stadt)

# Summierung
summe = 0
for zahl in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    summe += zahl
print(summe)

# Längster Name
namen = ["Anna", "Maximilian", "Tom", "Julia"]
laengster_name = ""
for name in namen:
    if len(name) > len(laengster_name):
        laengster_name = name
print(laengster_name)

# Quadratzahlen
for zahl in [1, 2, 3, 4, 5]:
    print(zahl ** 2)

# Verdreht
wort = "Python"
verdreht = ""
for buchstabe in wort:
    verdreht = buchstabe + verdreht
print(verdreht)

# Fakultät
zahl = 5
fakultaet = 1
for i in [1, 2, 3, 4, 5]:
    fakultaet *= i
print(fakultaet)

# Thermometer für Amerikaner
celsius_werte = [0, 20, 30, 100]
for celsius in celsius_werte:
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius}°C = {fahrenheit}°F")

# Vokale
wort = "Programmierung"
vokale = "aeiouAEIOU"
anzahl = 0
for buchstabe in wort:
    if buchstabe in vokale:
        anzahl += 1
print(anzahl)

# Häufigkeit
zahlen = [1, 2, 2, 3, 2, 4, 2, 5]
suche = 2
haeufigkeit = 0
for zahl in zahlen:
    if zahl == suche:
        haeufigkeit += 1
print(haeufigkeit)