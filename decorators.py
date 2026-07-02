# Funktion als Argument übergeben
'''
Was ist die Ausgabe des folgenden Codes?
'''
def anwenden(func, wert):
    return func(wert)

def verdoppeln(x):
    return x * 2

def quadrieren(x):
    return x ** 2

print(anwenden(verdoppeln, 5))
print(anwenden(quadrieren, 5))
print(anwenden(len, "Hallo"))
'''
Lösung

10
25
5

Erklärung: Die Funktion anwenden nimmt eine Funktion als Argument entgegen und ruft sie mit dem übergebenen Wert auf. 
Das ist möglich, weil Funktionen in Python First-Class Objects sind — sie können wie jeder andere Wert gespeichert und übergeben werden.

    anwenden(verdoppeln, 5) → verdoppeln(5) → 10
    anwenden(quadrieren, 5) → quadrieren(5) → 25
    anwenden(len, "Hallo") → len("Hallo") → 5

Dieses Konzept ist die Grundlage für Dekoratoren.
'''


# Was ist die Ausgabe? (einfacher Dekorator)
'''
Was ist die Ausgabe des folgenden Codes?
'''
def mein_dekorator(func):
    def wrapper():
        print("Vorher")
        func()
        print("Nachher")
    return wrapper

@mein_dekorator
def sage_hallo():
    print("Hallo!")

sage_hallo()
'''
Lösung

Vorher
Hallo!
Nachher

Erklärung: 
Der Dekorator @mein_dekorator ersetzt sage_hallo durch die Funktion wrapper.
Beim Aufruf von sage_hallo() wird also tatsächlich wrapper() aufgerufen:
    print("Vorher") → gibt "Vorher" aus
    func() → ruft die originale sage_hallo auf → gibt "Hallo!" aus
    print("Nachher") → gibt "Nachher" aus
Die @-Syntax ist gleichbedeutend mit: sage_hallo = mein_dekorator(sage_hallo)
'''


# Logging-Dekorator schreiben
'''
Schreibe einen Dekorator log, der bei jedem Funktionsaufruf den Funktionsnamen und die übergebenen Argumente ausgibt.

@log
def addiere(a, b):
    return a + b

@log
def begruessung(name):
    return f"Hallo, {name}!"

addiere(3, 5)
begruessung("Anna")

Erwartete Ausgabe:

Aufruf: addiere(3, 5)
Aufruf: begruessung('Anna',)

Hinweis: Verwende *args und **kwargs, damit der Dekorator mit beliebigen Funktionen funktioniert.
'''
from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Aufruf: {func.__name__}{args}")
        return func(*args, **kwargs)
    return wrapper

@log
def addiere(a, b):
    return a + b

@log
def begruessung(name):
    return f"Hallo, {name}!"

addiere(3, 5)       # Aufruf: addiere(3, 5)
begruessung("Anna") # Aufruf: begruessung('Anna',)
'''
Erklärung: Der wrapper fängt alle Argumente mit *args und **kwargs auf, gibt den Funktionsnamen (func.__name__) 
und die Argumente aus, und leitet den Aufruf an die Originalfunktion weiter. 
@wraps(func) sorgt dafür, dass die Metadaten der Originalfunktion erhalten bleiben.
'''


# Zeitmessung mit Dekorator
'''
Schreibe einen Dekorator zeitmessung, der misst, wie lange eine Funktion zur Ausführung braucht, und die Dauer in Sekunden ausgibt.

import time

@zeitmessung
def langsame_berechnung():
    time.sleep(1)
    return 42

ergebnis = langsame_berechnung()
print(f"Ergebnis: {ergebnis}")

Erwartete Ausgabe (ungefähr):

langsame_berechnung dauerte 1.0012 Sekunden
Ergebnis: 42

Hinweis: Verwende time.time() für die Zeitmessung.
'''
import time
from functools import wraps

def zeitmessung(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        ergebnis = func(*args, **kwargs)
        dauer = time.time() - start
        print(f"{func.__name__} dauerte {dauer:.4f} Sekunden")
        return ergebnis
    return wrapper

@zeitmessung
def langsame_berechnung():
    time.sleep(1)
    return 42

ergebnis = langsame_berechnung()
print(f"Ergebnis: {ergebnis}")
'''
Erklärung: Der Dekorator speichert die Startzeit vor dem Funktionsaufruf und berechnet die Differenz danach. 
Wichtig ist, dass der wrapper den Rückgabewert der Originalfunktion speichert und zurückgibt (return ergebnis), 
damit die dekorierte Funktion weiterhin korrekt funktioniert.
'''


# functools.wraps — Warum ist das wichtig?
'''
Was ist die Ausgabe des folgenden Codes? Was ändert sich, wenn man @wraps(func) hinzufügt?
'''
def mein_dekorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@mein_dekorator
def addiere(a, b):
    """Addiert zwei Zahlen."""
    return a + b

print(addiere.__name__)
print(addiere.__doc__)
'''
Ohne @wraps:
    wrapper
    None

Mit @wraps:
    addiere
    Addiert zwei Zahlen.

Erklärung: 
Ohne @wraps(func) wird addiere durch wrapper ersetzt — und wrapper hat seinen eigenen __name__ ("wrapper") 
und keinen Docstring (None).

Mit @wraps(func) werden die Metadaten der Originalfunktion (__name__, __doc__, __module__ etc.) auf den Wrapper kopiert:
from functools import wraps

def mein_dekorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

Das ist besonders wichtig für Debugging, help() und Tools, die auf Funktionsmetadaten zugreifen.
'''


# Zugriffskontrolle mit Dekorator
'''
Schreibe einen Dekorator nur_admin, der prüft, ob der erste Parameter einer Funktion den Wert "admin" hat. Falls nicht, soll eine Fehlermeldung ausgegeben und None zurückgegeben werden.

@nur_admin
def daten_loeschen(benutzer, datensatz):
    print(f"{datensatz} wurde gelöscht!")
    return True

daten_loeschen("admin", "Kundendaten")   # Kundendaten wurde gelöscht!
daten_loeschen("gast", "Kundendaten")    # Zugriff verweigert!

Erwartete Ausgabe:
    Kundendaten wurde gelöscht!
    Zugriff verweigert!
'''
from functools import wraps

def nur_admin(func):
    @wraps(func)
    def wrapper(benutzer, *args, **kwargs):
        if benutzer != "admin":
            print("Zugriff verweigert!")
            return None
        return func(benutzer, *args, **kwargs)
    return wrapper

@nur_admin
def daten_loeschen(benutzer, datensatz):
    print(f"{datensatz} wurde gelöscht!")
    return True

daten_loeschen("admin", "Kundendaten")   # Kundendaten wurde gelöscht!
daten_loeschen("gast", "Kundendaten")    # Zugriff verweigert!
'''
Erklärung: Der Wrapper fängt den ersten Parameter (benutzer) ab und prüft, ob er "admin" ist. 
Nur wenn ja, wird die Originalfunktion aufgerufen. 
Andernfalls wird eine Fehlermeldung ausgegeben und None zurückgegeben.

Dieses Muster wird in der Praxis häufig für Autorisierung und Berechtigungsprüfungen verwendet.
'''


# Dekorator mit Parameter (@repeat(n=3))
'''
Schreibe einen Dekorator repeat(n), der eine Funktion n-mal ausführt.

@repeat(n=3)
def sage_hallo():
    print("Hallo!")

sage_hallo()

Erwartete Ausgabe:
    Hallo!
    Hallo!
    Hallo!

Hinweis: Dekoratoren mit Parametern benötigen drei Verschachtelungsebenen.
'''
from functools import wraps

def repeat(n):
    def dekorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            ergebnis = None
            for _ in range(n):
                ergebnis = func(*args, **kwargs)
            return ergebnis
        return wrapper
    return dekorator

@repeat(n=3)
def sage_hallo():
    print("Hallo!")

sage_hallo()
# Hallo!
# Hallo!
# Hallo!
'''
Erklärung: 
Drei Verschachtelungsebenen sind nötig:

    repeat(n=3) wird aufgerufen → gibt dekorator zurück
    dekorator(sage_hallo) wird aufgerufen → gibt wrapper zurück
    wrapper() wird aufgerufen → führt sage_hallo() dreimal aus

Das ist äquivalent zu: sage_hallo = repeat(n=3)(sage_hallo)
'''


# Mehrere Dekoratoren stapeln
'''
Was ist die Ausgabe des folgenden Codes? Erkläre die Reihenfolge der Ausführung.
'''
def sterne(func):
    def wrapper(*args, **kwargs):
        print("***")
        ergebnis = func(*args, **kwargs)
        print("***")
        return ergebnis
    return wrapper

def ausrufezeichen(func):
    def wrapper(*args, **kwargs):
        print("!!!")
        ergebnis = func(*args, **kwargs)
        print("!!!")
        return ergebnis
    return wrapper

@sterne
@ausrufezeichen
def sage(text):
    print(text)

sage("Hallo")
'''

***
!!!
Hallo
!!!
***

Erklärung: 
Mehrere Dekoratoren werden von unten nach oben angewendet:

sage = sterne(ausrufezeichen(sage))
    Zuerst wird ausrufezeichen(sage) ausgeführt → sage wird mit !!! umhüllt
    Dann wird sterne(...) auf das Ergebnis angewendet → alles wird mit *** umhüllt

Beim Aufruf von sage("Hallo") wird der äußerste Wrapper (sterne) zuerst ausgeführt:
    sterne.wrapper → print("***")
    ausrufezeichen.wrapper → print("!!!")
    Originales sage → print("Hallo")
    ausrufezeichen.wrapper → print("!!!")
    sterne.wrapper → print("***")

Die Dekoratoren bilden eine Art Zwiebelschicht um die Originalfunktion.
'''