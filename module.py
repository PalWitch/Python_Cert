# Eigenes Modul: Preisrechner
''' 
    Erstelle zwei Dateien im selben Ordner.

    Datei price_tools.py:

    Konstante TAX_RATE = 0.19
    Funktion gross_price(net_price)
    Funktion format_price(value), Rueckgabe z.B. "119.00 EUR"

    Datei main.py:

    importiere das Modul mit import price_tools
    berechne den Bruttopreis fuer 100
    gib den formatierten Preis aus

    Lösung
'''
#price_tools.py:

TAX_RATE = 0.19


def gross_price(net_price):
    return net_price * (1 + TAX_RATE)


def format_price(value):
    return f"{value:.2f} EUR"

#main.py:

import price_tools

price = price_tools.gross_price(100)
print(price_tools.format_price(price))


# Importfehler erklaeren
'''
    Erklaere jeweils die wahrscheinlichste Ursache und eine passende Loesung.

    ModuleNotFoundError: No module named 'price_tools'
    AttributeError: module 'price_tools' has no attribute 'gross_price'
    Eine Datei heisst random.py, danach funktioniert import random komisch.

    Lösung

    Python findet keine Datei bzw. kein Paket mit diesem Namen. Loesung: Dateiname, Ordner und aktuelles Arbeitsverzeichnis pruefen.
    Das Modul wurde gefunden, aber der Name gross_price existiert darin nicht. Loesung: Schreibweise und Inhalt von price_tools.py pruefen.
    Die eigene Datei random.py ueberschattet das Standardmodul random. Loesung: eigene Datei umbenennen, z.B. random_demo.py.
'''


# Mini-Paket fuer Kursmaterial
'''
    Baue eine kleine Modulstruktur:

    course_tools/
        __init__.py
        grading.py
        text_tools.py
    main.py

    Anforderungen:
        grading.py enthaelt average(*ratings).
        grading.py enthaelt needs_repeat(*ratings), Rueckgabe True, wenn der Durchschnitt kleiner als 3 ist.
        text_tools.py enthaelt headline(text), Rueckgabe in Grossbuchstaben.
        main.py importiert beide Module und testet die Funktionen.

    Lösung
'''
# course_tools/grading.py:

def average(*ratings):
    if not ratings:
        return 0
    return sum(ratings) / len(ratings)

def needs_repeat(*ratings):
    return average(*ratings) < 3

# course_tools/text_tools.py:

def headline(text):
    return text.upper()

# main.py:

from course_tools import grading
from course_tools import text_tools

print(text_tools.headline("args und kwargs"))
print(grading.average(2, 3, 2, 4))
print(grading.needs_repeat(2, 3, 2, 4))


# platform: Diagnose-Skript
'''
Schreibe ein kleines Diagnose-Skript mit dem Modul platform.

Anforderungen:

    importiere platform
    gib das Betriebssystem aus
    gib die Maschinenarchitektur aus
    gib die Python-Version aus
    gib die Python-Implementierung aus

Beispielausgabe:

System: Darwin
Machine: arm64
Python-Version: 3.12.11
Implementierung: CPython

Die konkreten Werte duerfen je nach Rechner anders sein.
Lösung
'''
import platform


print("System:", platform.system())
print("Machine:", platform.machine())
print("Python-Version:", platform.python_version())
print("Implementierung:", platform.python_implementation())

# Die Ausgabe ist systemabhaengig. Wichtig ist, welche Funktion welche Art von Information liefert.


# platform: Ausgabe einordnen

'''
Ordne die folgenden Ausgaben den passenden platform-Funktionen zu.

Funktionen:

    platform.system()
    platform.machine()
    platform.python_version()
    platform.python_implementation()

Ausgaben:

    "CPython"
    "3.12.11"
    "Darwin"
    "arm64"

Schreibe zu jeder Ausgabe die passende Funktion und eine kurze Begruendung.
Lösung

    "CPython" gehoert zu platform.python_implementation(), weil es die Python-Implementierung beschreibt.
    "3.12.11" gehoert zu platform.python_version(), weil es die Python-Version als String beschreibt.
    "Darwin" gehoert zu platform.system(), weil es den Systemnamen liefert. Auf macOS ist das haeufig "Darwin".
    "arm64" gehoert zu platform.machine(), weil es die Maschinenarchitektur beschreibt.
'''


# Standardmodule zuordnen
'''
Ordne das passende Standardmodul zu.

Module:

    platform
    os
    sys
    math
    random
    datetime

Situationen:

    Du willst wissen, ob das Programm auf Windows, Linux oder macOS laeuft.
    Du brauchst die Quadratwurzel von 81.
    Du willst eine Zufallszahl zwischen 1 und 6.
    Du willst das heutige Datum ausgeben.
    Du willst das aktuelle Arbeitsverzeichnis anzeigen.
    Du willst sehen, in welchen Pfaden Python nach Modulen sucht.

Lösung

    platform, z.B. platform.system()
    math, z.B. math.sqrt(81)
    random, z.B. random.randint(1, 6)
    datetime, z.B. datetime.date.today()
    os, z.B. os.getcwd()
    sys, z.B. sys.path
'''


# Support-Check fuer ein Python-Problem
'''
Ein Teilnehmer meldet: "Bei mir laeuft das Python-Skript nicht."

Schreibe ein kleines Support-Skript, das Informationen sammelt, die man fuer eine erste Fehlersuche wirklich gebrauchen kann.

Das Skript soll ausgeben:

    Betriebssystem
    Rechnerarchitektur
    Python-Version
    aktuelles Arbeitsverzeichnis
    eine Liste der Dateien im aktuellen Arbeitsverzeichnis
    Datum und Uhrzeit, zu der der Support-Check ausgefuehrt wurde

Recherchiere selbst, welche Standardmodule und Funktionen dafuer geeignet sind. Es sollen keine externen Pakete installiert oder importiert werden.
Lösung

Geeignete Standardmodule und Funktionen:

    platform.system() fuer das Betriebssystem
    platform.machine() fuer die Rechnerarchitektur
    platform.python_version() fuer die Python-Version
    os.getcwd() fuer das aktuelle Arbeitsverzeichnis
    os.listdir() fuer die Dateien im aktuellen Arbeitsverzeichnis
    datetime.datetime.now() fuer Datum und Uhrzeit des Checks

Sinnvolle Module: platform, os, datetime.
'''
import platform
import os
from datetime import datetime

print("=== Support-Check ===")
print(f"Betriebssystem: {platform.system()}")
print(f"Rechnerarchitektur: {platform.machine()}")
print(f"Python-Version: {platform.python_version()}")
print(f"Aktuelles Arbeitsverzeichnis: {os.getcwd()}")

print("\nDateien und Ordner im aktuellen Arbeitsverzeichnis:")
for eintrag in os.listdir():
    print(f"- {eintrag}")

print(f"\nAusgefuehrt am: {datetime.now()}")



# Lernkarten-Session mit Zeitmessung
'''
Schreibe ein kleines Konsolenprogramm fuer eine kurze Lernkarten-Session.

Anforderungen:

    Es gibt eine Liste mit mehreren Wiederholungsfragen.
    Die Fragen sollen in zufaelliger Reihenfolge gestellt werden.
    Vor jeder neuen Frage soll eine kurze Pause entstehen.
    Am Ende soll angezeigt werden, wie lange die Session ungefaehr gedauert hat.

Beispielfragen koennen sein:

    "Erklaere *args in einem Satz."
    "Nenne eine Dunder Method."
    "Was liefert platform.system()?"

Recherchiere selbst, welche Standardmodule und Funktionen dafuer geeignet sind. Es sollen keine externen Pakete installiert oder importiert werden.
Lösung

Geeignete Standardmodule und Funktionen:

    random.shuffle() fuer eine zufaellige Reihenfolge der Fragen
    time.sleep() fuer die kurze Pause zwischen den Fragen
    time.time() oder datetime.datetime.now() fuer Start- und Endzeit

Sinnvolle Module: random, time oder alternativ datetime.
'''
import random
import time

fragen = [
    "Erklaere *args in einem Satz.",
    "Nenne eine Dunder Method.",
    "Was liefert platform.system()?",
    "Wofuer benutzt man os.getcwd()?",
    "Was macht random.shuffle()?"
]

random.shuffle(fragen)

start = time.time()

print("=== Lernkarten-Session startet ===")

for frage in fragen:
    time.sleep(2)
    print(f"\nFrage: {frage}")
    input("Druecke Enter fuer die naechste Frage...")

ende = time.time()
dauer = ende - start

print(f"\nDie Session dauerte ungefaehr {dauer:.1f} Sekunden.")



# Datei-Aufraeumhelfer als Trockenlauf
'''
Schreibe ein Programm, das beim Aufraeumen eines Projektordners hilft.

Das Programm soll:

    das aktuelle Arbeitsverzeichnis untersuchen
    alle Dateien anzeigen, die auf .py, .md oder .ipynb enden
    fuer jede gefundene Datei den Dateinamen und die Dateigroesse ausgeben
    die Dateien nach Groesse sortiert anzeigen
    nichts loeschen und nichts verschieben, nur anzeigen
    am Ende einen Zeitstempel fuer den Bericht ausgeben

Recherchiere selbst, welche Standardmodule und Funktionen dafuer geeignet sind. Es sollen keine externen Pakete installiert oder importiert werden.
Lösung

Geeignete Standardmodule und Funktionen:

    os.getcwd() fuer das aktuelle Arbeitsverzeichnis
    os.listdir() fuer die Dateien im Ordner
    os.path.isfile() zum Pruefen, ob ein Eintrag eine Datei ist
    os.path.getsize() fuer die Dateigroesse
    str.endswith() fuer die Dateiendungen, kein Modul noetig
    datetime.datetime.now() fuer den Zeitstempel

Sinnvolle Module: os, datetime.
'''
import os
from datetime import datetime

print("=== Datei-Aufraeumhelfer (Trockenlauf) ===")

ordner = os.getcwd()
print(f"Aktuelles Arbeitsverzeichnis: {ordner}\n")

dateien = []

for eintrag in os.listdir(ordner):
    if os.path.isfile(eintrag) and eintrag.endswith((".py", ".md", ".ipynb")):
        groesse = os.path.getsize(eintrag)
        dateien.append((eintrag, groesse))

dateien.sort(key=lambda item: item[1])

if dateien:
    print("Gefundene Dateien, sortiert nach Groesse:")
    for name, groesse in dateien:
        print(f"{name} - {groesse} Bytes")
else:
    print("Keine passenden Dateien gefunden.")

print(f"\nBericht erstellt am: {datetime.now()}")