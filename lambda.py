# Einfache Lambda-Funktion
'''
Was ist die Ausgabe des folgenden Codes?
'''
verdoppeln = lambda x: x * 2
print(verdoppeln(5))
print(verdoppeln("Ha"))
'''
10
HaHa

Erklärung: Die Lambda-Funktion verdoppeln nimmt ein Argument x und gibt x * 2 zurück. 
Bei 5 ergibt das 10 (Multiplikation), bei "Ha" ergibt das "HaHa" (String-Wiederholung).
'''

# Lambda vs. def — Was ist die Ausgabe?
'''
Sind die beiden folgenden Funktionen gleichwertig? Was gibt der Code aus?
'''
def addiere_def(a, b):
    return a + b

addiere_lambda = lambda a, b: a + b

print(addiere_def(3, 4))
print(addiere_lambda(3, 4))
print(type(addiere_def))
print(type(addiere_lambda))
'''
7
7
<class 'function'>
<class 'function'>

Erklärung: Beide Funktionen sind funktional gleichwertig — sie addieren zwei Zahlen. 
Auch der Typ ist identisch: function. Der Unterschied liegt nur in der Schreibweise. 
Lambda-Funktionen sind auf einen einzigen Ausdruck beschränkt und haben keinen eigenen 
Namen (der Name addiere_lambda ist nur der Variablenname).
 '''


# Sortieren nach Stringlänge
'''
Gegeben ist eine Liste von Wörtern:

woerter = ["Python", "ist", "eine", "Programmiersprache"]

Sortiere die Liste nach der Länge der Wörter (kürzestes zuerst) mithilfe von sorted() und einer Lambda-Funktion.

Erwartete Ausgabe:
['ist', 'eine', 'Python', 'Programmiersprache']
'''

woerter = ["Python", "ist", "eine", "Programmiersprache"]
sortiert = sorted(woerter, key=lambda w: len(w))
print(sortiert)
# ['ist', 'eine', 'Python', 'Programmiersprache']
'''
Erklärung: Der key-Parameter von sorted() erwartet eine Funktion, die für jedes Element einen Vergleichswert liefert. 
lambda w: len(w) gibt die Länge jedes Wortes zurück, danach wird sortiert.
'''

# Sortieren nach Dictionary-Wert
'''
Gegeben ist eine Liste von Dictionaries mit Schülerdaten:

schueler = [
    {"name": "Anna", "note": 2.3},
    {"name": "Ben", "note": 1.7},
    {"name": "Clara", "note": 1.0},
    {"name": "David", "note": 3.0},
]

    Sortiere die Liste nach der Note (beste Note zuerst) mit sorted() und einer Lambda-Funktion.
    Sortiere die Liste nach dem Namen (alphabetisch).
'''
schueler = [
    {"name": "Anna", "note": 2.3},
    {"name": "Ben", "note": 1.7},
    {"name": "Clara", "note": 1.0},
    {"name": "David", "note": 3.0},
]

# 1. Nach Note sortieren
nach_note = sorted(schueler, key=lambda s: s["note"])
print(nach_note)
# [{'name': 'Clara', 'note': 1.0}, {'name': 'Ben', 'note': 1.7},
#  {'name': 'Anna', 'note': 2.3}, {'name': 'David', 'note': 3.0}]

# 2. Nach Name sortieren
nach_name = sorted(schueler, key=lambda s: s["name"])
print(nach_name)
# [{'name': 'Anna', 'note': 2.3}, {'name': 'Ben', 'note': 1.7},
#  {'name': 'Clara', 'note': 1.0}, {'name': 'David', 'note': 3.0}]


# Quadratzahlen mit map()

'''
Verwende map() mit einer Lambda-Funktion, um aus der Liste [1, 2, 3, 4, 5] eine Liste der Quadratzahlen zu erzeugen.
Erwartete Ausgabe:
[1, 4, 9, 16, 25]

Tipp
map() gibt ein Map-Objekt zurück. Verwende list(), um es in eine Liste umzuwandeln.
'''
zahlen = [1, 2, 3, 4, 5]
quadrate = list(map(lambda x: x ** 2, zahlen))
print(quadrate)
# [1, 4, 9, 16, 25]
'''
Erklärung: map() wendet die Lambda-Funktion auf jedes Element der Liste an. Das Ergebnis ist ein Iterator, der mit list() in eine Liste umgewandelt wird.
'''

# Gerade Zahlen filtern
'''
Verwende filter() mit einer Lambda-Funktion, um aus der Liste [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] nur die geraden Zahlen herauszufiltern.

Erwartete Ausgabe:
[2, 4, 6, 8, 10]
'''
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gerade = list(filter(lambda x: x % 2 == 0, zahlen))
print(gerade)
# [2, 4, 6, 8, 10]
'''
Erklärung: filter() behält nur die Elemente, für die die Lambda-Funktion True zurückgibt. x % 2 == 0 ist True für gerade Zahlen.
'''


# map() und filter() kombiniert
'''
Gegeben ist eine Liste von Zahlen:

zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Verwende filter() und map() zusammen mit Lambda-Funktionen, um:
    Nur die ungeraden Zahlen herauszufiltern
    Diese dann zu quadrieren
Erwartete Ausgabe:
[1, 9, 25, 49, 81]

Schreibe das in einer einzigen Zeile (ohne Zwischenvariable).
Tipp
Du kannst das Ergebnis von filter() direkt als Eingabe für map() verwenden.
'''
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ergebnis = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, zahlen)))
print(ergebnis)
# [1, 9, 25, 49, 81]
'''
Erklärung: filter() gibt einen Iterator der ungeraden Zahlen zurück. 
Dieser wird direkt an map() weitergegeben, das jede Zahl quadriert.

Alternative mit List Comprehension (oft lesbarer):
ergebnis = [x ** 2 for x in zahlen if x % 2 != 0]
'''


# Lambda als Rückgabewert einer Funktion
'''
Was ist die Ausgabe des folgenden Codes? Erkläre, was hier passiert.

def multiplizierer(faktor):
    return lambda x: x * faktor

verdoppeln = multiplizierer(2)
verdreifachen = multiplizierer(3)

print(verdoppeln(5))
print(verdreifachen(5))
print(multiplizierer(10)(7))

Lösung

10
15
70

Erklärung: Die Funktion multiplizierer gibt eine Lambda-Funktion zurück, die den übergebenen faktor "einschließt" (Closure). 
Jeder Aufruf von multiplizierer erzeugt eine neue Funktion mit einem festen Faktor:

    verdoppeln = multiplizierer(2) erzeugt lambda x: x * 2
    verdreifachen = multiplizierer(3) erzeugt lambda x: x * 3
    multiplizierer(10)(7) erzeugt lambda x: x * 10 und ruft sie sofort mit 7 auf → 70

Dieses Muster nennt man Closure — die Lambda-Funktion "erinnert sich" an den Wert von faktor aus dem umgebenden Scope, 
auch nachdem multiplizierer bereits zurückgekehrt ist.
'''