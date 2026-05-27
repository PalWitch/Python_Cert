# Übung: Dictionaries

## Setup

1. Dieses repository klonen
   `git clone https://github.com/git-url/project.git`

2. Ensure you have Python 3.5 or later installed
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

Die testzs können auch über Python gestartet werden:
`python -m unittest discover tests -f`

## Übung 1: Wörterbuch umkehren

Schreiben Sie eine Funktion `woerterbuch_umkehren(dict)`, die ein Dictionary als Eingabe nimmt und ein neues Dictionary zurückgibt, bei dem die Schlüssel und Werte vertauscht sind. Nehmen Sie an, dass die Werte im ursprünglichen Dictionary eindeutig sind.

Beispiel:

```python
eingabe = {'a': 1, 'b': 2, 'c': 3}
ausgabe = {1: 'a', 2: 'b', 3: 'c'}
```

## Übung 2: Dictionary-Fusion

Schreiben Sie eine Funktion `dictionaries_zusammenfuehren(*dicts)`, die beliebig viele Dictionaries als Eingabe nimmt und sie zu einem einzigen Dictionary zusammenführt. Wenn ein Schlüssel in mehreren Dictionaries vorkommt, soll der Wert aus dem letzten Dictionary verwendet werden.

> Hinweis: Der Paremeter _dicts_, ist mit einem Sternchen versehen. Dadurch enthält _dicts_ immer ein Tuple mit allen übergebenen Werten.

###Beispiel:

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'d': 5}
result = dictionaries_zusammenfuehren(dict1, dict2, dict3)
# result == {'a': 1, 'b': 3, 'c': 4, 'd': 5}
```

## Übung 3: Häufigste Wörter

Die Funktion soll ein Dictionary zurückgeben, das die Wörter Text und ihre Häufigkeit enthält.
Groß- und Kleinschreibung soll ignoriert werden.

### Beispiel:

```python
text = "Der Hund läuft. Der Hund bellt. Die Katze miaut."
n = 2
ausgabe = {'der': 2, 'hund': 2}
```

### Tips:

#### String in Liste umwandeln

`text.split(" ")` -> `["Der", "Hund", "läuft.", ...]`

#### Punkte entfernen

```
wort = "läuft."
wort = wort.replace(".", "") # Mit nichts ersetzen
```

#### Testen ob ein Eintrag schon vorhanden ist:

```
words = { "Der": 1 }
print("Der" in words)
# -> True
```
