# Multiplizieren
'''
def sum_up(box_or_value):

    if isinstance(box_or_value, list):
        summe = 0

        for obj in box_or_value:
            summe += sum_up(obj)

    else:
        summe = box_or_value

    return summe

all_summed_up = sum_up([[1,2,3], [4,5,[6,7,8]]])
print(all_summed_up)

Wie muss der obige Code angepasst werden, damit die Zahlen nicht summiert, sondern multipliziert werden?
'''

def multiply_up(box_or_value):
    if isinstance(box_or_value, list):
        product = 1 # Aus 0 eine 1

        for obj in box_or_value:
            product *= multiply_up(obj) # Aus += ein *=

    else:
        product = box_or_value

    return product

all_multiplied_up = multiply_up([[1, 2, 3], [4, 5, [6, 7, 8]]])
print(all_multiplied_up)


# umständlich
'''
Gebe der folgenden Funktion einen Namen, der beschreibt, was sie tut.
'''
def func(my_list):
    if len(my_list) == 0:
        return 0
    return my_list[0] + func(my_list[1:])

func([1,2,3])
'''
Sie summiert die Elemente einer Liste/Tupel... auf. 
Also wäre auch hier sum_up oder sigma ein schöner Name.
'''


# Fakultät berechnen
'''
Man kann die Fakultät einer Zahl n mit der folgenden Formel berechnen:

n! = 1, wenn n <= 1
n! = n * (n-1)!, andernfalls

Nutze das, um eine rekursive Implementierung von der Fakultätsfunktion zu programmieren.
'''
def fak(n):
    if n <= 1:
        return 1
    return n * fak(n-1)



# Binäre Suche
'''
In dieser Aufgabe sollen sie die binäre Suche rekursiv implementieren. 
Bei der binären Suche gehen hier davon aus, dass wir eine sortierte Liste haben. 
In dieser Liste wird nach einem bestimmten Eintrag gesucht. 
Die Funktion binary_search(my_list, element) gibt also True zurück, wenn der Eintrag in der Liste gefunden wurde und False anderfalls.

Ablauf der binären Suche: Man betrachtet zunächst das Element m genau in der Mitte der Liste. 
Ist m bereits das gesuchte Element e, so sind wir fertig und können True zurückgeben. 
Andernfalls suchen wir in der linken Teilliste von m weiter, wenn m < e ist. 
Ist jedoch m > e, so suchen wir in der rechten Teilliste weiter. 
Die binäre Suche beginnt also auf einem kleinen Problem immer wieder von vorn. 
Wenn wir jemals eine leere Liste durchsuchen sollen, wissen wir, dass e sich nicht in der Liste befindet und wir können False zurückgeben.
'''
def binary_search(my_list, element):
    if len(my_list) == 0:
        return False

    mid_index = len(my_list) // 2
    mid_element = my_list[mid_index]

    if mid_element < element:
        return binary_search(my_list[mid_index + 1:], element)
    elif mid_element > element:
        return binary_search(my_list[:mid_index], element)
    else:
        return True

print(binary_search([1, 2, 3, 5, 6, 9, 10], 9))  # True
print(binary_search([1, 2, 3, 5, 6, 9, 10], 8))  # False


# Summe einer Liste rekursiv
'''
Schreibe eine rekursive Funktion summe(liste), die die Summe aller Elemente einer Liste berechnet.

Hinweis: Der Basisfall ist eine leere Liste (Summe = 0). 
Im rekursiven Fall addierst du das erste Element zum Ergebnis des rekursiven Aufrufs mit dem Rest der Liste.

print(summe([1, 2, 3, 4, 5]))  # 15
print(summe([]))                # 0
print(summe([10]))              # 10

Tipp
Nutze Slicing (liste[1:]), um den Rest der Liste zu erhalten.
'''
def summe(liste):
    if len(liste) == 0:
        return 0
    return liste[0] + summe(liste[1:])

print(summe([1, 2, 3, 4, 5]))  # 15
print(summe([]))                # 0
print(summe([10]))              # 10


# String umkehren
'''
Schreibe eine rekursive Funktion umkehren(text), die einen String umdreht.

print(umkehren("Hallo"))   # "ollaH"
print(umkehren("Python"))  # "nohtyP"
print(umkehren("a"))       # "a"
print(umkehren(""))        # ""

Hinweis: Überlege, wie du das letzte Zeichen vor den Rest des umgekehrten Strings setzen kannst.
'''
def umkehren(text):
    if len(text) <= 1:
        return text
    return text[-1] + umkehren(text[:-1])

print(umkehren("Hallo"))   # "ollaH"
print(umkehren("Python"))  # "nohtyP"
print(umkehren("a"))       # "a"
print(umkehren(""))        # ""
'''
Erklärung: Im Basisfall (leerer String oder ein Zeichen) wird der String direkt zurückgegeben. 
Im rekursiven Fall wird das letzte Zeichen vorne angehängt und der Rest des Strings rekursiv umgekehrt.
'''


# Fibonacci-Folge
'''
Die Fibonacci-Folge ist definiert als:
fib(0) = 0
fib(1) = 1
fib(n) = fib(n-1) + fib(n-2), für n > 1

Schreibe eine rekursive Funktion fib(n), die die n-te Fibonacci-Zahl berechnet.
print(fib(0))   # 0
print(fib(1))   # 1
print(fib(6))   # 8
print(fib(10))  # 55

Tipp
Der Basisfall hat hier zwei Bedingungen: n == 0 und n == 1.
'''
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(0))   # 0
print(fib(1))   # 1
print(fib(6))   # 8
print(fib(10))  # 55
'''
Achtung: Diese naive Implementierung hat eine exponentielle Laufzeit, da viele Werte mehrfach berechnet werden. 
Für große n wird die Berechnung sehr langsam. In der Praxis würde man hier Memoisation oder eine iterative Lösung verwenden.
'''


# Verschachtelte Liste flatten
'''
Schreibe eine rekursive Funktion flatten(liste), die eine beliebig tief verschachtelte Liste in eine flache Liste umwandelt.

print(flatten([1, [2, 3], [4, [5, 6]]]))         # [1, 2, 3, 4, 5, 6]
print(flatten([[1, [2]], [3, [4, [5]]]]))        # [1, 2, 3, 4, 5]
print(flatten([1, 2, 3]))                        # [1, 2, 3]
print(flatten([]))                               # []

Hinweis: Prüfe für jedes Element, ob es eine Liste ist (isinstance(element, list)). Wenn ja, rufe flatten rekursiv auf. Wenn nein, füge das Element direkt zur Ergebnisliste hinzu.
'''
def flatten(liste):
    ergebnis = []
    for element in liste:
        if isinstance(element, list):
            ergebnis.extend(flatten(element))
        else:
            ergebnis.append(element)
    return ergebnis

print(flatten([1, [2, 3], [4, [5, 6]]]))         # [1, 2, 3, 4, 5, 6]
print(flatten([[1, [2]], [3, [4, [5]]]]))        # [1, 2, 3, 4, 5]
print(flatten([1, 2, 3]))                        # [1, 2, 3]
print(flatten([]))                               # []
'''
Erklärung: Die Funktion geht jedes Element der Liste durch. 
Ist ein Element selbst eine Liste, wird flatten rekursiv aufgerufen und das Ergebnis mit extend angefügt. 
Ist es keine Liste, wird es direkt mit append hinzugefügt.
'''