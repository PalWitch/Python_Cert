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