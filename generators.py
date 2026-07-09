# Was ist die Ausgabe? (yield-Grundlagen)
'''
Was ist die Ausgabe des folgenden Codes?
'''
def mein_generator():
    yield 1
    yield 2
    yield 3

gen = mein_generator()
print(next(gen))
print(next(gen))
'''
1
2

Erklärung: 
Die Generator-Funktion mein_generator enthält drei yield-Anweisungen. 
Beim ersten next(gen) wird der Code bis zum ersten yield ausgeführt und 1 zurückgegeben. 
Die Funktion wird pausiert. Beim zweiten next(gen) wird der Code ab dem ersten yield fortgesetzt 
bis zum zweiten yield — und 2 zurückgegeben. 
Der dritte Wert 3 wird nie abgefragt, weil kein weiterer next()-Aufruf erfolgt.
'''


# Countdown-Generator
'''
Schreibe eine Generator-Funktion countdown(n), die von n bis 1 herunterzählt.

for zahl in countdown(5):
    print(zahl)

Erwartete Ausgabe:
5
4
3
2
1
'''
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for zahl in countdown(5):
    print(zahl)
'''
Erklärung: Die Funktion verwendet yield in einer while-Schleife. 
Bei jedem next()-Aufruf (intern durch die for-Schleife) wird der aktuelle Wert von n zurückgegeben und danach um 1 verringert. 
Sobald n <= 0 ist, endet die Funktion und StopIteration wird ausgelöst.
'''


# Gerade Zahlen Generator
'''
Schreibe eine Generator-Funktion gerade_zahlen(n), die die ersten n geraden Zahlen erzeugt (beginnend bei 2).

print(list(gerade_zahlen(5)))

Erwartete Ausgabe:

[2, 4, 6, 8, 10]
'''
def gerade_zahlen(n):
    zahl = 2
    for _ in range(n):
        yield zahl
        zahl += 2

print(list(gerade_zahlen(5)))
# [2, 4, 6, 8, 10]
'''
Erklärung: Der Generator hält den aktuellen Zustand (zahl) zwischen den yield-Aufrufen. 
Bei jedem next() wird die aktuelle gerade Zahl zurückgegeben und zahl um 2 erhöht. 
Nach n Durchläufen endet die for-Schleife und der Generator ist erschöpft.
'''


# Generator-Erschöpfung — Was passiert?
'''
Was ist die Ausgabe des folgenden Codes? Erkläre, warum.

def zahlen():
    yield 1
    yield 2
    yield 3

gen = zahlen()

print(sum(gen))
print(sum(gen))
print(list(gen))

Lösung

6
0
[]

Erklärung: Ein Generator kann nur einmal durchlaufen werden.

    sum(gen) beim ersten Mal iteriert über alle Werte (1 + 2 + 3 = 6) und erschöpft den Generator.
    sum(gen) beim zweiten Mal findet keine Werte mehr → sum() über eine leere Sequenz ergibt 0.
    list(gen) findet ebenfalls keine Werte mehr → leere Liste [].

Um den Generator erneut zu verwenden, muss ein neuer Generator erstellt werden: gen = zahlen().
'''


# Fibonacci als Generator
'''
Schreibe eine Generator-Funktion fibonacci(), die die unendliche Fibonacci-Folge erzeugt (0, 1, 1, 2, 3, 5, 8, 13, ...).
Verwende den Generator, um die ersten 10 Fibonacci-Zahlen auszugeben:

gen = fibonacci()
for _ in range(10):
    print(next(gen), end=" ")

Erwartete Ausgabe:

0 1 1 2 3 5 8 13 21 34
'''
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
for _ in range(10):
    print(next(gen), end=" ")
# 0 1 1 2 3 5 8 13 21 34
'''
Erklärung: Der Generator speichert den Zustand der beiden Variablen a und b zwischen den yield-Aufrufen. 
Die while True-Schleife macht den Generator unendlich — er erzeugt immer neue Fibonacci-Zahlen, solange next() aufgerufen wird. 
Das ist nur mit Generatoren möglich, nicht mit Listen.
'''


# Datei zeilenweise mit Generator
'''
Schreibe eine Generator-Funktion lese_zeilen(dateipfad), die eine Textdatei zeilenweise liest und jede Zeile (ohne Zeilenumbruch) per yield zurückgibt.

for zeile in lese_zeilen("beispiel.txt"):
    print(zeile)

Warum ist ein Generator hier besser als datei.readlines()?
'''
def lese_zeilen(dateipfad):
    with open(dateipfad, "r") as datei:
        for zeile in datei:
            yield zeile.rstrip("\n")

for zeile in lese_zeilen("beispiel.txt"):
    print(zeile)
'''
Erklärung: Der Generator liest die Datei zeilenweise — es wird immer nur eine Zeile gleichzeitig im Speicher gehalten. 
Bei datei.readlines() wird die gesamte Datei auf einmal in den Speicher geladen, was bei großen Dateien 
(z.B. Logfiles mit Millionen Zeilen) zu Speicherproblemen führen kann.

Zusätzlich kümmert sich with open(...) um das automatische Schließen der Datei, und rstrip("\n") entfernt den Zeilenumbruch 
am Ende jeder Zeile.
'''


# Generator-Pipeline
'''
Erstelle eine Pipeline aus drei Generator-Funktionen:

    erzeuge_zahlen(n) — erzeugt Zahlen von 1 bis n
    quadriere(iterable) — quadriert jeden Wert
    filtere_groesser_als(iterable, grenze) — gibt nur Werte > grenze weiter

Verkette die Generatoren zu einer Pipeline und gib das Ergebnis für n=10 und grenze=20 aus.

Erwartete Ausgabe:

[25, 36, 49, 64, 81, 100]
'''
def erzeuge_zahlen(n):
    for i in range(1, n + 1):
        yield i

def quadriere(iterable):
    for x in iterable:
        yield x ** 2

def filtere_groesser_als(iterable, grenze):
    for x in iterable:
        if x > grenze:
            yield x

    # Pipeline verketten
ergebnis = filtere_groesser_als(quadriere(erzeuge_zahlen(10)), 20)
print(list(ergebnis))
    # [25, 36, 49, 64, 81, 100]
'''
Erklärung: Die Generatoren werden wie Rohre in einer Pipeline verkettet:

    erzeuge_zahlen(10) liefert: 1, 2, 3, ..., 10
    quadriere(...) quadriert jeden Wert: 1, 4, 9, ..., 100
    filtere_groesser_als(..., 20) gibt nur Werte > 20 weiter: 25, 36, ..., 100

Der Vorteil: Jeder Wert fließt einzeln durch die gesamte Pipeline. Es wird keine Zwischenliste im Speicher gehalten.
'''


# Eigenes range() nachbauen
'''
Baue die eingebaute Funktion range() als Generator-Funktion mein_range(start, stop, step=1) nach.

Die Funktion soll sich wie range() verhalten:

print(list(mein_range(0, 10, 2)))   # [0, 2, 4, 6, 8]
print(list(mein_range(5, 0, -1)))   # [5, 4, 3, 2, 1]
print(list(mein_range(1, 5)))       # [1, 2, 3, 4]

Hinweis: Berücksichtige sowohl positive als auch negative Schrittweiten.
'''
def mein_range(start, stop, step=1):
    if step == 0:
        raise ValueError("step darf nicht 0 sein")

    current = start
    if step > 0:
        while current < stop:
            yield current
            current += step
    else:
        while current > stop:
            yield current
            current += step

print(list(mein_range(0, 10, 2)))   # [0, 2, 4, 6, 8]
print(list(mein_range(5, 0, -1)))   # [5, 4, 3, 2, 1]
print(list(mein_range(1, 5)))       # [1, 2, 3, 4]
'''
Erklärung: Die Funktion unterscheidet zwischen positivem und negativem step:
    Bei positivem step wird gezählt, solange current < stop
    Bei negativem step wird gezählt, solange current > stop
    step == 0 löst wie bei echtem range() einen ValueError aus
Im Gegensatz zum echten range() (das ein spezielles Objekt ist) erzeugt unsere Version einen einfachen Generator.
'''


# Quadratzahlen-Generator
def quadratzahlen(n):
    for i in range(1, n + 1):
        yield i ** 2    

print(list(quadratzahlen(5)))  # [1, 4, 9, 16, 25]


# Buchstaben-Generator
def buchstaben(wort):
    for buchstabe in wort:
        yield buchstabe

print(list(buchstaben("Hallo")))  # ['H', 'a', 'l', 'l', 'o']


# Running Sum
def running_sum(numbers):
    for i in range(len(numbers)):
        yield sum(numbers[:i + 1])   

'''
def running_sum(numbers):
    current_sum = 0
    for num in numbers:
        current_sum += num
        yield current_sum
'''   

print(list(running_sum([1, 2, 3, 4])))  # [1, 3, 6, 10]


# Generator schreiben (gerade Zahlen)
def even_numbers(limit):
    current = 0
    while current <= limit:
        yield current
        current += 2


# Filter-Generator schreiben (nur Wörter, deren Länge mindestens min_length ist)
def only_long(words, min_length):
    for word in words:
        if len(word) >= min_length:
            yield word