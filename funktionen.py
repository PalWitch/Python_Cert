##############
# Funktionen #
##############
'''In Python ist eine Funktion eine selbstständige, wiederverwendbare Codeeinheit, 
   die dazu dient, eine bestimmte Aufgabe zu erledigen. Funktionen können Parameter 
   akzeptieren, Operationen durchführen und einen Rückgabewert liefern.
'''

''' Parameter sind quasi Variablen bei Definition einer Funktion
    Beim Aufruf der Funktion sind es dann die konkreten Werte und heißen dann Argumente
'''
''' Parameter können optional sein und mit default gefüllt werden
    requiered arguments müssen dann vorangestellt werden, damit die Syntax funktioniert.
    Argumente sind positional, also an die Reihenfolge gebunden
    named-arguments (name=Gustav) dürfen auch in anderer Reihenfolge stehen
    *args    = positional arguments      <- Tupel
    **kwargs = keyword/named arguments   <- Dictionary
'''

# Einfache Begrüßungsfunktion
def begruesse():
    print("Hallo Welt!")

begruesse()
print()

# Quadratzahlen
def quadrat(zahl):
    ergebnis = zahl * zahl
    return ergebnis

print("Quadrat von 6:", quadrat(6))
print()

# Maximum von zwei Zahlen
def maximum_von_zwei_zahlen(erste_zahl, zweite_zahl):
    if erste_zahl > zweite_zahl:
        return erste_zahl
    return zweite_zahl

print("Größere Zahl:", maximum_von_zwei_zahlen(8, 13))
print()

# Summierung
def summiere(erste_zahl, zweite_zahl, dritte_zahl):
    summe = erste_zahl + zweite_zahl + dritte_zahl
    return summe

print("Summe:", summiere(4, 7, 9))
print()

# String-Wiederholung
def wiederhole_text(text, anzahl):
    wiederholter_text = text * anzahl
    return wiederholter_text

print(wiederhole_text("Hi ", 3))
print()

# Fahrenheit in Celsius
def fahreinheit_in_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

print("20 Grad Fahrenheit sind", round(fahreinheit_in_celsius(20), 2), "Grad Celsius")
print()

# Listenelemente addieren
def addiere_listenelemente(zahlenliste):
    summe = 0
    for zahl in zahlenliste:
        summe = summe + zahl
    return summe

print("Listensumme:", addiere_listenelemente([2, 4, 6, 8]))
print()

# Listenelemente addieren und prüfen
def addiere_und_pruefe(zahlenliste):
    summe = 0
    for zahl in zahlenliste:
        summe = summe + zahl

    ist_groesser_als_zehn = summe > 10
    return summe, ist_groesser_als_zehn

summe, ist_groesser_als_zehn = addiere_und_pruefe([1, 2, 3, 4, 5])
print("Summe:", summe)
print("Größer als 10:", ist_groesser_als_zehn)
print()

# Check Gerade Zahl
def ist_gerade(zahl):
    return zahl % 2 == 0

print("Ist 14 gerade?", ist_gerade(14))
print("Ist 9 gerade?", ist_gerade(9))
print()

# Countdown
def countdown(startzahl):
    for zahl in range(startzahl, -1, -1):
        print(zahl)

countdown(5)
print()

# Minimum in Liste finden
def minimum_in_liste_finden(zahlenliste):
    kleinste_zahl = zahlenliste[0]
    for zahl in zahlenliste:
        if zahl < kleinste_zahl:
            kleinste_zahl = zahl
    return kleinste_zahl

print("Kleinste Zahl:", minimum_in_liste_finden([7, 3, 9, 1, 5]))
print()

# Länge eines Strings
def laenge_eines_strings(text):
    anzahl_zeichen = len(text)
    return anzahl_zeichen

print("Länge:", laenge_eines_strings("Umschulung"))
print()

# Multiplikationstabelle
def gib_multiplikationstabelle_aus(zahl):
    for faktor in range(1, 11):
        ergebnis = zahl * faktor
        print(zahl, "x", faktor, "=", ergebnis)

gib_multiplikationstabelle_aus(4)
print()

# Palindrome prüfen
def ist_palindrom(text):
    text_klein = text.lower()
    umgedrehter_text = text_klein[::-1]
    return text_klein == umgedrehter_text

print("Ist 'Lagerregal' ein Palindrom?", ist_palindrom("Lagerregal"))
print("Ist 'Python' ein Palindrom?", ist_palindrom("Python"))
print()

# Mehrere Rückgabewerte
def finde_laengstes_und_kuerzestes_wort(text):
    wort_liste = text.split()
    laengstes_wort = wort_liste[0]
    kuerzestes_wort = wort_liste[0]

    for wort in wort_liste:
        if len(wort) > len(laengstes_wort):
            laengstes_wort = wort
        if len(wort) < len(kuerzestes_wort):
            kuerzestes_wort = wort

    return laengstes_wort, kuerzestes_wort

laengstes_wort, kuerzestes_wort = finde_laengstes_und_kuerzestes_wort("Der schnelle braune Fuchs springt")
print("Längstes Wort:", laengstes_wort)
print("Kürzestes Wort:", kuerzestes_wort)


