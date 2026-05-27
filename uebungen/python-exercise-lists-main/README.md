# Übung: List Comprehension

Beschreibung

## Setup

1. Dieses repository klonen
`git clone https://github.com/fabiandarga/python-exercise-lists.git`

2. Sicherstellen, dass Python 3.5 oder höher installiert ist
`python --version`

## Diese Übung enhält Tests

In dem du die Tests startet kannst du den Fortschritt deiner Arbeit sehen.

### Windows  
Die tests starten:
`run_tests.bat`

### Linux/macOS
Berechtigung setzten:  
`chmod u+x run_tests.sh`

Tests starten:  
`./run_tests.sh`

### Universell
Die tests können auch über Python gestartet werden:  
`python -m unittest discover tests -f`

----

## Übung 1: Gerade Zahlen
Erstellen Sie eine List Comprehension, die eine Liste mit geraden Zahlen von 0 bis 20 (einschließlich) generiert.

**Erwartete Ausgabe:**
```python
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

## Übung 2: Quadrieren von Zahlen
Gegeben sei die Liste `zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`. Erstellen Sie eine List Comprehension, die eine neue Liste mit den Quadraten der Zahlen generiert, aber nur wenn das Quadrat größer als 20 ist.

**Erwartete Ausgabe:**
```python
[25, 36, 49, 64, 81, 100]
```

## Übung 3: Filtern von Strings
Gegeben sei die Liste von Wörtern `woerter = ['apfel', 'banane', 'kirsche', 'dattel', 'erdbeere', 'feige', 'traube']`. Erstellen Sie eine List Comprehension, die eine neue Liste generiert, die nur die Wörter enthält, die:
1. Mit einem Vokal beginnen (a, e, i, o, u)
2. Eine Länge von mehr als 5 Buchstaben haben

**Erwartete Ausgabe:**
```python
['erdbeere']
```

## Bonus-Herausforderung:
Erstellen Sie eine List Comprehension, die die folgende Liste von Listen abflacht:
```python
verschachtelte_liste = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
Das Ergebnis sollte eine einzige Liste mit allen Zahlen sein.

**Erwartete Ausgabe:**
```python
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Hinweis: Denken Sie beim Lösen dieser Übungen an die Struktur einer List Comprehension:
```python
[ausdruck for element in iterable if bedingung]
```

