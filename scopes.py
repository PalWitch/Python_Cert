'''
    Globale Variablen: Außerhalb von Funktionen definiert; im gesamten Code gültig.
    Lokale Variablen: Innerhalb von Funktionen definiert; nur in ihrer eigenen Funktion gültig.
    Shadowing: Lokale Variablen können den gleichen Namen wie globale Variablen haben, aber sie sind separate Instanzen.
'''

# Globale Variable
global_var = "Ich bin global"

def test_global():
   print(global_var)

test_global()

# Lokale Variable
def test_lokal():
   lokal_var = "Ich bin lokal"
   print(lokal_var)

test_lokal()

# Globale und lokale Variable mit demselben Namen
var = "Ich bin global"

def test_gleichnamig():
   var = "Ich bin lokal"
   print(var)  # Lokale Variable
   print(globals()['var'])  # Globale Variable

test_gleichnamig()

# Änderung einer globalen Variable
global_var = "Ursprünglich global"

def test_aendern():
   global_var = "Geändert lokal"
   print(global_var)

test_aendern()
print(global_var)  # Bleibt unverändert "Ursprünglich global"

# Verwenden des global-Keywords
global_var = "Ursprünglich global"

def test_global_keyword():
   global global_var
   global_var = "Geändert global"
   print(global_var)

test_global_keyword()
print(global_var)  # Wird zu "Geändert global"

# Nested Functions Scope
def außen():
   außen_var = "Variable von außen"

   def innen():
       print(außen_var)

   innen()

außen()

# Lokale Variable in einer Schleife
def test_schleife():
   for i in range(3):
       schleifen_var = i
   print(schleifen_var)

test_schleife()

# Funktionsargument Scope
'''
Beim Funktionsaufruf erhält der Parameter `arg` eine Referenz auf dasselbe Objekt wie das Argument `var`.
Innerhalb der Funktion wird `arg` neu zugewiesen (`arg = "Geändert"`) und verweist dann auf ein neues Objekt.
Die Variable `var` außerhalb der Funktion bleibt unverändert.
'''
def test_argument(arg):
   arg = "Geändert"   
   print(arg)         # Gibt "Geändert" aus

var = "Original"
test_argument(var)
print(var)            # Bleibt "Original"

# Rückgabewerte und Scope
def gib_zurueck():
   return "Rückgabewert"

global_var = gib_zurueck()
print(global_var)




# Zwei Varianten für ein Ergebnis
'''Gemini'''
def args_zu_dict(*args):
    # Dictionaries benötigen Schlüssel-Wert-Paare.
    # Wir erzeugen Tupel-Paare, indem wir args mit sich selbst um eins versetzt zippen.
    # 'None' dient als Füllwert, falls die Länge ungerade ist.
    return dict(zip(args[::2], list(args[1::2]) + [None]))
'''
args[::2]:      Extrahiert alle Elemente an geraden Positionen (d.h. Index 0, 2, 4...), die als Keys dienen sollen.
args[1::2]:     Extrahiert alle Elemente an ungeraden Positionen (Index 1, 3, 5...), welche die Values bilden.
+ [None]:       Falls eine ungerade Anzahl an Parametern übergeben wird, ist das values-Tupel ein Element kürzer als das keys-Tupel. 
                Das Anhängen von None gleicht dies aus, damit jeder Key sein Value (oder None) erhält.
zip() & dict(): Führt die Schlüssel und Werte zusammen und konvertiert sie in das finale Dictionary.
'''

# Beispiele:
print(args_zu_dict("Name", "Anna", "Alter")) 
# {'Name': 'Anna', 'Alter': None}

print(args_zu_dict("Name", "Anna", "Alter", 28)) 
# {'Name': 'Anna', 'Alter': 28}

'''Perplexity'''
def args_to_dict(*args):
    result = {}
    # paarweise durchlaufen: key = args[0], args[2], ...; value = args[1], args[3], ...
    for i in range(0, len(args), 2):
        key = args[i]
        # Falls kein passender Wert existiert, verwenden wir None
        value = args[i + 1] if i + 1 < len(args) else None
        result[key] = value
    return result

# Beispiele:
print(args_to_dict("a", 1, "b", 2))
# {'a': 1, 'b': 2}

print(args_to_dict("name", "Nicky", "age"))
# {'name': 'Nicky', 'age': None}



# Scope – Lesezugriff
'''
Was gibt das folgende Programm aus? Überlege zuerst, bevor du es ausführst.

name = "Alice"

def begruessung():
    print(f"Hallo, {name}!")

begruessung()
print(name)


Ausgabe:

Hallo, Alice!
Alice

Die Funktion begruessung() hat keinen eigenen name – sie liest daher die globale Variable. 
Ein reiner Lesezugriff auf eine globale Variable ist innerhalb einer Funktion erlaubt.
'''


# Scope – global Keyword
'''
Schreibe eine Funktion toggle(), die eine globale Variable aktiv (Startwert False) bei jedem Aufruf umschaltet (True → False → True …). 
Nutze das global-Keyword.

Erwartetes Verhalten:

print(aktiv)   # False
toggle()
print(aktiv)   # True
toggle()
print(aktiv)   # False
'''
aktiv = False

def toggle():
    global aktiv
    aktiv = not aktiv

print(aktiv)   # False
toggle()
print(aktiv)   # True
toggle()
print(aktiv)   # False
'''
Ohne global würde Python aktiv als lokale Variable interpretieren und einen UnboundLocalError auslösen, weil man versucht, 
eine lokale Variable zu lesen, bevor sie zugewiesen wurde.
'''


# Closure – Logger-Funktion
'''
In vielen Projekten möchte man Log-Nachrichten mit einem festen Präfix versehen (z. B. dem Modulnamen).

Schreibe eine Funktion erstelle_logger(praefix), die eine neue Funktion zurückgibt. Die zurückgegebene Funktion nimmt eine nachricht entgegen und gibt sie mit dem Präfix aus.

Erwartetes Verhalten:

db_log = erstelle_logger("[DB]")
auth_log = erstelle_logger("[AUTH]")

db_log("Verbindung hergestellt")   # [DB] Verbindung hergestellt
auth_log("Login erfolgreich")      # [AUTH] Login erfolgreich
db_log("Query ausgeführt")         # [DB] Query ausgeführt
'''
def erstelle_logger(praefix):
    def log(nachricht):
        print(f"{praefix} {nachricht}")
    return log

db_log = erstelle_logger("[DB]")
auth_log = erstelle_logger("[AUTH]")

db_log("Verbindung hergestellt")   # [DB] Verbindung hergestellt
auth_log("Login erfolgreich")      # [AUTH] Login erfolgreich
db_log("Query ausgeführt")         # [DB] Query ausgeführt
'''
log ist eine Closure – sie merkt sich den Wert von praefix aus dem Enclosing Scope. 
Dieses Muster wird in der Praxis häufig für Logger, Konfigurationen oder Factory-Funktionen eingesetzt.
'''

 
# Closure – Validierung mit Grenzwerten
'''
Bei der Eingabevalidierung prüft man oft, ob ein Wert in einem bestimmten Bereich liegt.

Schreibe eine Funktion erstelle_validator(min_wert, max_wert), die eine neue Funktion zurückgibt. Die zurückgegebene Funktion nimmt einen wert entgegen und gibt True zurück, wenn er im Bereich min_wert bis max_wert (jeweils inklusive) liegt, sonst False.

Erwartetes Verhalten:

ist_prozent = erstelle_validator(0, 100)
ist_temperatur = erstelle_validator(-40, 60)

print(ist_prozent(50))       # True
print(ist_prozent(101))      # False
print(ist_temperatur(-10))   # True
print(ist_temperatur(80))    # False
'''
def erstelle_validator(min_wert, max_wert):
    def validiere(wert):
        return min_wert <= wert <= max_wert
    return validiere

ist_prozent = erstelle_validator(0, 100)
ist_temperatur = erstelle_validator(-40, 60)

print(ist_prozent(50))       # True
print(ist_prozent(101))      # False
print(ist_temperatur(-10))   # True
print(ist_temperatur(80))    # False
'''
Die innere Funktion validiere ist eine Closure, die sich min_wert und max_wert merkt. 
Solche Validierungs-Fabriken sind ein gängiges Muster bei der Eingabeprüfung.
'''


# Scope & Closure – Rabattrechner
'''
Erstelle ein kleines Rabatt-System mit Scope und Closure:

    Definiere eine globale Variable waehrung = "€".
    Schreibe eine Funktion rabatt_rechner(prozent), die eine neue Funktion zurückgibt. Die zurückgegebene Funktion nimmt einen preis entgegen und gibt den rabattierten Preis als formatierten String zurück (z. B. "80.00 €").
    Erstelle damit zwei Rabatt-Funktionen: mitarbeiter_rabatt (20 %) und vip_rabatt (30 %).

Erwartetes Verhalten:

print(mitarbeiter_rabatt(100))      # "80.00 €"
print(vip_rabatt(100))              # "70.00 €"
print(mitarbeiter_rabatt(59.99))    # "47.99 €"

Hinweis: Nutze round() für die Rundung auf zwei Nachkommastellen.
'''
waehrung = "€"  # globale Variable

def rabatt_rechner(prozent):
    def berechne(preis):
        reduziert = round(preis * (1 - prozent / 100), 2)
        return f"{reduziert:.2f} {waehrung}"
    return berechne

mitarbeiter_rabatt = rabatt_rechner(20)
vip_rabatt = rabatt_rechner(30)

print(mitarbeiter_rabatt(100))     # 80.00 €
print(vip_rabatt(100))             # 70.00 €
print(mitarbeiter_rabatt(59.99))   # 47.99 €
'''
Hier kommen mehrere Konzepte zusammen:

    Globaler Scope: waehrung wird in der inneren Funktion gelesen (LEGB-Regel: Global).
    Closure:        berechne merkt sich den Wert von prozent aus dem Enclosing Scope.
    Lokaler Scope:  reduziert und preis existieren nur innerhalb von berechne.
'''