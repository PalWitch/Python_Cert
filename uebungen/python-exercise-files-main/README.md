# Übung: CSV Datei einlesen

## Beschreibung
Schreibe eine Funktion, die eine CSV-Datei (Comma Separated Values) einliest und die Daten als Liste von Dictionaries zurückgibt.

## Setup
1. Es wird Python > 3.5 benötigt.
2. Dieses repository klonen
`git clone https://github.com/fabiandarga/python-exercise-files.git`

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


## Datei: mitarbeiter.csv
Die Datei enthält Mitarbeiterdaten in folgendem Format:
```
name,age,role
Anna Schmidt,34,Entwicklerin
Max Müller,28,Designer
...
```
- Die erste Zeile enthält die Spaltenüberschriften
- Jede weitere Zeile enthält die Daten eines Mitarbeiters
- Die Werte sind durch Kommas getrennt

## Aufgabe
1. Implementiere die Funktion `read_csv_file(filepath: str)`, die:
   - Die CSV-Datei einliest
   - Die Daten in eine Liste von Dictionaries umwandelt
   - Diese Liste zurückgibt

## Erwartetes Ergebnis
Die Funktion soll eine Liste von Dictionaries zurückgeben, zum Beispiel:
```python
[
    {'name': 'Anna Schmidt', 'age': '34', 'role': 'Entwicklerin'},
    {'name': 'Max Müller', 'age': '28', 'role': 'Designer'},
    # ...weitere Einträge
]
```

## Hinweise
- Verwende `with open(filepath, 'r') as file:` um die Datei zu öffnen
- Mit `file.readlines()` kannst du alle Zeilen als Liste einlesen
- Oder mit `for line in file:` darüber iterieren (bevorzugt)
- Jede Zeile kannst du mit `line.strip().split(',')` in ihre Einzelteile zerlegen
- Die erste Zeile enthält die Spaltennamen, die du als Dictionary-Schlüssel verwenden sollst
- Das csv-Modul soll NICHT verwendet werden

## Testen
Du kannst deine Lösung testen, indem du das Programm ausführst und die ausgegebenen Dictionaries überprüfst.

