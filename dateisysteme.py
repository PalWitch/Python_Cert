# Dateisysteme #
################

# Alternativen zu read
'''readgibt einen String mit der gesamten Datei zurück.
   readline gibt die erste Zeile der Datei zurück. Beim zweiten Aufruf wird die zweite Zeile gelesen usw. Wenn es keine Zeile mehr zu lesen gibt, werden leere Zeilen zurückgegeben.
   readlines gibt eine Liste mit den Zeilen der Datei zurück.
'''

# Fehler fangen
try:
    datei = open("not_existing", "r")
    inhalt = datei.read()
    print(inhalt)
    datei.close()
except FileNotFoundError as e:
    print(f"Datei existiert nicht: {e.filename}")

# Zeilenweise lesen
path = "beispiel.txt"
with open(path) as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line)
        input()

# Zeichen zählen
def count_characters_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return len(content)


print("Anzahl der Zeichen in der Datei:", count_characters_in_file("beispiel.txt"))


'''Modus 	Beschreibung
   "r" 	    Lesen (default)
   "w" 	    Schreiben
   "x" 	    Exklusives Schreiben
   "a" 	    Anhängen
   "b" 	    Binärmodus
   "t" 	    Textmodus (default)
   "+" 	    Aktualisieren (Lesen/Schreiben)
'''

# Binäres Lesen
'''Lese beispiel.txt und mein_passwort.png mit r, rt und rb. Was ist möglich?

Lösung
Die beispiel.txt lässt sich in allen Fällen lesen. "rt" liefert den exakten Text zurück, r erzeugt nach jeder Zeile einen Absatz und "rb" führt Zeilenumbrüche etc. nicht aus.
Die mein_passwort.png lässt sich nur im Modus "rb" ohne Fehler anzeigen, jedoch ist die Ausgabe nicht für Menschen verständlich. 
'''

# Inhalte schreiben
from os import system


path = "meintext.txt"
with open(path, "wt") as file:
    while True:
        user_input = input()

        if user_input == "quit":
            break

file.write(user_input + "\n")

system("notepad.exe " + path) # Windows

# Anhängen
with open("save_file", "a") as datei:
    datei.write("Hallo\n")

# Umkehrung einer Datei
def reverse_file_content(file_path, save_file):
    with open(file_path, 'r') as file_in, open(save_file, 'w') as file_out:
        lines = file_in.readlines()
        file_out.writelines(reversed(lines))

reverse_file_content("beispiel.txt", "beispiel_reversed.txt")

# ZENSUR
class Censorer:
    @staticmethod
    def create_censored_file(org_file_path, censored_file_path, censored_words, symbol="*"):
        with open(org_file_path, "rt") as org, open(censored_file_path, "wt") as censored:
            text = org.read()
            for word_to_censor in censored_words:
                replacement = symbol * len(word_to_censor)
                text = text.replace(word_to_censor, replacement)
            censored.write(text)

# CSV als Speicherformat nutzen
from csv import reader, writer

class Person:
    def init(self, name, age):
        self.name = name
        self.age = age

def __str__(self):
    return f"Person: {self.name}, {self.age}"

@classmethod
def create_persons_from_csv(cls, file_path):
    result = list()
    with open(file_path) as csv_file:
        for zeile in reader(csv_file):
            name, age = zeile
            result.append(cls(name, age))

    return result

def save_to_csv(self, file_path, mode="a"):
    with open(file_path, mode, newline="") as csv_file:
        writer(csv_file).writerow([self.name, self.age])


csv_file_path = "persons.csv"
persons = Person.create_persons_from_csv(csv_file_path)

for person in persons:
    print(person)

Person("Gustav", 32).save_to_csv(csv_file_path)

# CSV-Datei filtern
@classmethod
def create_persons_from_csv(cls, file_path, csv_filter=None):
    result = list()
    with open(file_path) as csv_file:
        for zeile in reader(csv_file):
            name, age = zeile
            if not csv_filter or csv_filter(name, age):
                result.append(cls(name, age))

    return result

# Erstelle und analysiere eine Dateiliste mit pathlib
from pathlib import Path
        
ziel_verzeichnis = Path(".") 

print("Analysiere Verzeichnis...\n")

for datei in ziel_verzeichnis.iterdir():
    if datei.is_file():
        dateiname = datei.name
        dateigroesse_kb = datei.stat().st_size / 1024
        erweiterung = datei.suffix
        
        print(f"Dateiname: {dateiname}, Größe: {dateigroesse_kb:.2f}KB, Erweiterung: {erweiterung}")
