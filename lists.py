# append() vs. extend()
'''
Was gibt der folgende Code aus? Überlege zuerst, bevor du ihn ausführst.

a = [1, 2, 3]
b = [1, 2, 3]

a.append([4, 5])
b.extend([4, 5])

print("a:", a)
print("b:", b)
print("len(a):", len(a))
print("len(b):", len(b))

Lösung
a: [1, 2, 3, [4, 5]]
b: [1, 2, 3, 4, 5]
len(a): 4
len(b): 5
    append() fügt das übergebene Objekt als ein einzelnes Element hinzu – hier die gesamte Liste [4, 5].
    extend() fügt jedes Element des übergebenen Iterables einzeln hinzu.
'''

# remove() vs. pop()
'''
Gegeben ist folgende Liste:

tiere = ["Hund", "Katze", "Vogel", "Katze", "Fisch"]

    Entferne das erste Vorkommen von "Katze" mit remove().
    Entferne das letzte Element mit pop() und speichere es in einer Variable.
    Entferne das Element an Index 0 mit pop().
    Gib die Liste und das mit pop() entfernte Element aus.
'''

tiere = ["Hund", "Katze", "Vogel", "Katze", "Fisch"]

tiere.remove("Katze")       # ["Hund", "Vogel", "Katze", "Fisch"]
letztes = tiere.pop()       # "Fisch", Liste: ["Hund", "Vogel", "Katze"]
tiere.pop(0)                # "Hund", Liste: ["Vogel", "Katze"]

print("Liste:", tiere)      # ["Vogel", "Katze"]
print("Entfernt:", letztes) # Fisch
'''
    remove(x) entfernt nach Wert (nur erstes Vorkommen).
    pop(i) entfernt nach Index und gibt das Element zurück.
    pop() ohne Argument entfernt das letzte Element.
'''


# sort() vs. sorted()
'''
Was gibt der folgende Code aus? Überlege zuerst, bevor du ihn ausführst.

zahlen = [5, 2, 8, 1, 9]

ergebnis = zahlen.sort()
print("ergebnis:", ergebnis)
print("zahlen:", zahlen)

neue_zahlen = [5, 2, 8, 1, 9]
ergebnis2 = sorted(neue_zahlen, reverse=True)
print("ergebnis2:", ergebnis2)
print("neue_zahlen:", neue_zahlen)

Lösung
ergebnis: None
zahlen: [1, 2, 5, 8, 9]
ergebnis2: [9, 8, 5, 2, 1]
neue_zahlen: [5, 2, 8, 1, 9]

    sort() sortiert in-place und gibt None zurück – häufige PCAP-Falle!
    sorted() gibt eine neue Liste zurück und lässt das Original unverändert.
'''

# Slicing
'''
Gegeben ist folgende Liste:

buchstaben = ["a", "b", "c", "d", "e", "f", "g"]

Schreibe jeweils einen Slice-Ausdruck, der folgendes Ergebnis liefert:

    ["c", "d", "e"]
    ["a", "b", "c"]
    ["e", "f", "g"]
    ["a", "c", "e", "g"]
    ["g", "f", "e", "d", "c", "b", "a"]
'''
buchstaben = ["a", "b", "c", "d", "e", "f", "g"]

print(buchstaben[2:5])   # 1. ["c", "d", "e"]
print(buchstaben[:3])    # 2. ["a", "b", "c"]
print(buchstaben[4:])    # 3. ["e", "f", "g"]  (oder [-3:])
print(buchstaben[::2])   # 4. ["a", "c", "e", "g"]
print(buchstaben[::-1])  # 5. ["g", "f", "e", "d", "c", "b", "a"]

# index(), count() und in
'''
Gegeben ist folgende Liste:

noten = [2, 1, 3, 2, 1, 4, 2, 5, 1]

    Wie oft kommt die Note 2 vor?
    An welchem Index steht die erste 4?
    Prüfe mit dem in-Operator, ob die Note 6 enthalten ist.
    Was passiert, wenn du noten.index(6) aufrufst?
'''
noten = [2, 1, 3, 2, 1, 4, 2, 5, 1]

print(noten.count(2))    # 3
print(noten.index(4))    # 5
print(6 in noten)        # False
# noten.index(6)         # ValueError: 6 is not in list
'''
Tipp: Vor index() immer mit in prüfen, ob das Element existiert, um einen ValueError zu vermeiden.
'''

# List Comprehensions
'''
Schreibe jeweils eine List Comprehension für folgende Aufgaben:

    Eine Liste der Quadrate von 1 bis 10.
    Alle geraden Zahlen von 1 bis 20.
    Alle Wörter aus der Liste ["Hallo", "Hi", "Python", "Hey", "Welt"], die mit "H" beginnen.
'''
# 1. Quadrate
quadrate = [x ** 2 for x in range(1, 11)]
print(quadrate)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 2. Gerade Zahlen
gerade = [x for x in range(1, 21) if x % 2 == 0]
print(gerade)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 3. Wörter mit "H"
woerter = ["Hallo", "Hi", "Python", "Hey", "Welt"]
h_woerter = [w for w in woerter if w.startswith("H")]
print(h_woerter)  # ["Hallo", "Hi", "Hey"]

# Kopie vs. Referenz
'''
Was gibt der folgende Code aus? Erkläre, warum.

original = [1, 2, [3, 4]]

referenz = original
flache_kopie = original.copy()

original[0] = 99
original[2][0] = 99

print("original:", original)
print("referenz:", referenz)
print("flache_kopie:", flache_kopie)

Tipp
Denke daran: copy() und [:] erstellen nur eine flache Kopie. Verschachtelte Objekte werden weiterhin geteilt.

Lösung
original: [99, 2, [99, 4]]
referenz: [99, 2, [99, 4]]
flache_kopie: [1, 2, [99, 4]]

    referenz = original erstellt keine Kopie, sondern eine zweite Referenz auf dasselbe Objekt. Alle Änderungen wirken sich auf beide aus.
    copy() erstellt eine flache Kopie – die äußere Liste ist neu, aber die inneren Objekte (z. B. [3, 4]) werden nicht kopiert, sondern referenziert.
    Deshalb ändert original[2][0] = 99 auch die flache Kopie, aber original[0] = 99 nicht.
    Für vollständig unabhängige Kopien: import copy → copy.deepcopy(original).
'''
