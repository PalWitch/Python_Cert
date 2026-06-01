class Rectangle:
    def __init__(self, sizeA: float|int, sizeB: float|int):
        self.sizeA = sizeA
        self.sizeB = sizeB

    def get_volume(self) -> float|int:
        return self.sizeA * self.sizeB

class Square(Rectangle):
    def __init__(self, size: float|int):
        super().__init__(size, size)

s = Square(4)
print(s.get_volume())
print(type(s))
print(type(s).__mro__)
print(Square.__mro__)
print(isinstance(s, Square))
print(isinstance(s, Rectangle))

# Typen erkennen

class Auto:
    def __init__(self, marke: str, modell: str):
        self.marke = marke
        self.modell = modell

    def starten(self) -> str:
        return f"{self.marke} {self.modell} wird gestartet."

class Elektroauto(Auto):
    def __init__(self, marke: str, modell: str, reichweite: int):
        super().__init__(marke, modell)
        self.reichweite = reichweite

    def starten(self) -> str:
        return f"{super().starten()} Elektromotor wird aktiviert."

    def aufladen(self) -> str:
        return f"{self.marke} {self.modell} wird aufgeladen."

    # Instanzen erstellen
mein_auto = Auto("Volkswagen", "Golf")
mein_elektroauto = Elektroauto("Tesla", "Model S", 500)

    # Methoden aufrufen
print(mein_auto.starten())          # Ausgabe: "Volkswagen Golf wird gestartet."
print(mein_elektroauto.starten())   # Ausgabe: "Tesla Model S wird gestartet. Elektromotor wird aktiviert."
print(mein_elektroauto.aufladen())  # Ausgabe: "Tesla Model S wird aufgeladen."



# Verschiedene Tiere
class Tier:
    def __init__(self, name: str):
        self.name = name

    def bewegen(self):
        print(f"{self.name} bewegt sich.")


class Hund(Tier):
    def bellen(self):
        print(f"{self.name} bellt.")

class Katze(Tier):
    def miauen(self):
        print(f"{self.name} miaut.")

tier1 = Tier("Tier1")
tier1.bewegen()

hund1 = Hund("Bello")
hund1.bewegen()
hund1.bellen()

katze1 = Katze("Minka")
katze1.bewegen()
katze1.miauen()

#  Geometry
from math import isclose

class Form:
    def umfang(self):
        raise NotImplementedError("Kann nicht für diese Allgemeine Form bestimmt werden")

    def inhalt(self):
        raise NotImplementedError("Kann nicht für diese Allgemeine Form bestimmt werden")


class Dreieck(Form):
    def __init__(self, size_a: float, size_b: float, size_c: float):
        self.size_a = size_a
        self.size_b = size_b
        self.size_c = size_c

    def umfang(self):
        return self.size_a + self.size_b + self.size_c

    def inhalt(self):
        s = self.umfang() / 2
        result = (s * (s - self.size_a) * (s - self.size_b) * (s - self.size_c)) ** 0.5
        return result

    def hat_90_grad_winkel(self):
        squared_sizes = [s ** 2 for s in (self.size_a, self.size_b, self.size_c)]
        squared_sizes.sort()
        return isclose(squared_sizes[0] + squared_sizes[1], squared_sizes[2])


class Kreis(Form):
    PI = 3.14159265358979323846

    def __init__(self, radius):
        self.radius = radius

    def umfang(self):
        return 2 * self.PI * self.radius

    def inhalt(self):
        return self.PI * self.radius ** 2


class Viereck(Form):
    def __init__(self, size_a, size_b, size_c, size_d):
        self.size_a = size_a
        self.size_b = size_b
        self.size_c = size_c
        self.size_d = size_d

    def umfang(self):
        return self.size_a + self.size_b + self.size_c + self.size_d


class Parallelogramm(Viereck):
    def __init__(self, size_a, size_b):
        super().__init__(size_a, size_b, size_a, size_b)

    def inhalt(self):
        return self.size_a * self.size_b
    

# Punkte
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Punkt):
            return Punkt(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type. Use with another Punkt object.")

    def __eq__(self, other):
        return (isinstance(other, Punkt)
                and self.x == other.x
                and self.y == other.y)

    def __sub__(self, other):
        if isinstance(other, Punkt):
            return Punkt(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Unsupported operand type. Use with another Punkt object.")

# Multiplizieren von Rechts (fortsetzung)
   
    def __eq__(self, other):
            return (isinstance(other, Punkt)
                    and isclose(self.x, other.x)
                    and isclose(self.y, other.y))

    def __sub__(self, other):
        return self + other * (-1)

    def __mul__(self, other):
        if isinstance(other, int | float):
            return Punkt(self.x * other, self.y * other)
        else:
            raise TypeError("Unsupported operand type. Use int or float")
    
# Zugriff wie bei Listen (Fortsetzung)
    def __getitem__(self, item):
        if item in [0, -2]:
            return self.x
        elif item in [1, -1]:
            return self.y
        else:
            raise IndexError("Index muss 0 für x oder 1 für y sein.")

    def __setitem__(self, key, value):
        if key in [0, -2]:
            self.x = value
        elif key in [1, -1]:
            self.y = value
        else:
            raise IndexError("Index muss 0 für x oder 1 für y sein.")

# Was ist nötig
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        if isinstance(other, int | float):
            return self.age < other
        raise TypeError(f"Comperator operation only allowed for Persons and float and int")

    def __le__(self, other):
        if isinstance(other, Person):
            return self.age <= other.age
        if isinstance(other, int | float):
            return self.age <= other
        raise TypeError(f"Comperator operation only allowed for Persons and float and int")

    def __contains__(self, item):
        if not isinstance(item, str):
            raise TypeError(f"Item ist darf nicht vom Type {type(item)}, sondern muss vom Typ str sein.")
        return item in self.name

