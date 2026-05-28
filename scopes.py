'''
    Globale Variablen: Außerhalb von Funktionen definiert; im gesamten Code gültig.
    Lokale Variablen: Innerhalb von Funktionen definiert; nur in ihrer eigenen Funktion gültig.
    Schattenbildung: Lokale Variablen können den gleichen Namen wie globale Variablen haben, aber sie sind separate Instanzen.
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
def test_argument(arg):
   arg = "Geändert"
   print(arg)

var = "Original"
test_argument(var)
print(var)  # Bleibt "Original"

# Rückgabewerte und Scope
def gib_zurueck():
   return "Rückgabewert"

global_var = gib_zurueck()
print(global_var)