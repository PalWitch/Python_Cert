import csv

def read_csv_file(filepath: str):
    """
    Liest eine CSV-Datei ein und gibt die Daten als Liste von Dictionaries zurück.
    Die erste Zeile der CSV-Datei enthält die Spaltennamen.

    Beispiel für den Rückgabewert:
    [
        {'name': 'Anna Schmidt', 'age': '34', 'role': 'Entwicklerin'},
        {'name': 'Max Müller', 'age': '28', 'role': 'Designer'},
        ...
    ]
    """
    
    with open(filepath, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)


if __name__ == "__main__":
    try:
        # Datei einlesen
        mitarbeiter = read_csv_file("mitarbeiter.csv")

        # Zur Kontrolle ausgeben
        for m in mitarbeiter:
            print(m)

    except FileNotFoundError:
        print("Fehler: Die Datei wurde nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
