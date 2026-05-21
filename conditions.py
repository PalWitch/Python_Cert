# Einfache if-Abfrage
zahl = 7
if zahl > 5:
    print("Die Zahl ist größer als 5")

# if-else
punktzahl = 35
if punktzahl >= 50:
    print("Bestanden")
else:
    print("Nicht bestanden")

# Negativ oder Positiv
zahl = -3
if zahl >= 0:
    print("Die Zahl ist positiv oder null")
else:
    print("Die Zahl ist negativ")

# Größer oder kleiner
erste_zahl = 10
zweite_zahl = 20
if erste_zahl > zweite_zahl:
    print("Die erste Zahl ist größer")
else:
    print("Die erste Zahl ist kleiner oder gleich")

# Alter überprüfen
alter = 16
if alter >= 18:
    print("Volljährig")
else:
    print("Minderjährig")

# Passwortüberprüfung
richtiger_benutzername = "nicky"
richtiger_passworttext = "geheim"

eingabe_benutzername = "nicky"
eingabe_passworttext = "falsch"

if eingabe_benutzername == richtiger_benutzername and eingabe_passworttext == richtiger_passworttext:
    print("Zugang erlaubt")
else:
    print("Zugang verweigert")

# Maximalwert
zahl_a = 12
zahl_b = 8
if zahl_a > zahl_b:
    maximalwert = zahl_a
else:
    maximalwert = zahl_b
print("Maximalwert:", maximalwert)

# Bewertung
punktzahl = 73
if punktzahl >= 90:
    note = "sehr gut"
elif punktzahl >= 75:
    note = "gut"
elif punktzahl >= 60:
    note = "befriedigend"
else:
    note = "ausreichend oder schlechter"
print("Note:", note)

# Temperaturen
temperatur = 5
if temperatur <= 0:
    print("Es friert")
elif temperatur < 20:
    print("Es ist kühl")
else:
    print("Es ist warm")

# Einfache Rechnung
zahl_x = 10
zahl_y = 5
ergebnis = zahl_x - zahl_y
if ergebnis < 0:
    print("Ergebnis ist negativ")
else:
    print("Ergebnis ist null oder positiv")

# Jahreszeiten
monat = 4
if monat in (3, 4, 5):
    print("Frühling")
elif monat in (6, 7, 8):
    print("Sommer")
elif monat in (9, 10, 11):
    print("Herbst")
else:
    print("Winter")

# Teilbarkeit
zahl = 15
if zahl % 2 == 0:
    print("Die Zahl ist durch 2 teilbar")
elif zahl % 3 == 0:
    print("Die Zahl ist durch 3 teilbar")
else:
    print("Die Zahl ist nicht durch 2 oder 3 teilbar")

# Einkaufsliste
anzahl_aepfel = 0
if anzahl_aepfel == 0:
    print("Äpfel kaufen")
else:
    print("Genug Äpfel vorhanden")

# Größte von drei Zahlen
zahl1 = 3
zahl2 = 9
zahl3 = 5

groesste_zahl = zahl1
if zahl2 > groesste_zahl:
    groesste_zahl = zahl2
if zahl3 > groesste_zahl:
    groesste_zahl = zahl3

print("Die größte Zahl ist:", groesste_zahl)

# Rabattaktion
einkaufswert = 75
if einkaufswert >= 100:
    rabatt_prozent = 20
elif einkaufswert >= 50:
    rabatt_prozent = 10
else:
    rabatt_prozent = 0
print("Rabatt in Prozent:", rabatt_prozent)

# Lichtschalter
licht_ist_an = False
if licht_ist_an:   # if prüft bei Boolschen Werten immer True
    print("Licht ausschalten")
else:              # else prüft bei Boolschen Werten immer False
    print("Licht einschalten")

# Fahrzeugklasse
geschwindigkeit = 130
if geschwindigkeit <= 50:
    print("Stadtverkehr")
elif geschwindigkeit <= 100:
    print("Landstraße")
else:
    print("Autobahn")

# Kinotag
wochentag = "Dienstag"
if wochentag == "Dienstag":
    ticket_preis = 6
else:
    ticket_preis = 10
print("Ticketpreis:", ticket_preis, "Euro")

# Schaltjahr
jahr = 2024
if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
    print(jahr, "ist ein Schaltjahr")
else:
    print(jahr, "ist kein Schaltjahr")