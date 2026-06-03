# Getter, Setter, statische und Klassen-Methoden

class Auto:
    def __init__(self, marke, kilometerstand):
        self.marke = marke
        self._kilometerstand = kilometerstand  # protected

    def info(self):
        return f"{self.marke} mit {self._kilometerstand} km"

a = Auto("VW", 50000)
print(a.info())
print(a._kilometerstand)  # Funktioniert, aber sollte vermieden werden


class Konto:
    def __init__(self, inhaber, kontostand):
        self.inhaber = inhaber
        self.__kontostand = kontostand  # private

    def einzahlen(self, betrag):
        self.__kontostand += betrag

    def get_kontostand(self):
        return self.__kontostand

k = Konto("Max", 1000)
print(k.get_kontostand())  # 1000

# Direkter Zugriff schlägt fehl:
try:
    print(k.__kontostand)
except AttributeError as e:
    print(f"Fehler: {e}")

# Aber über Name Mangling erreichbar:
print(k._Konto__kontostand)  # 1000


# Notendurchschnitt
class Student:
    def __init__(self, mathe, python, englisch):
        self.mathe = mathe
        self.python = python
        self.englisch = englisch

    def get_durchschnitt(self):
        return (self.mathe + self.python + self.englisch) / 3

    durchschnitt = property(get_durchschnitt)

print(Student(1,2,1).durchschnitt) # 1.333333333

# Radius oder Durchmesser
class Kreis:
    def __init__(self, radius):
        self.radius = radius    # Nutzt die set_radius Methode

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        if isinstance(radius, int | float):
            self.__radius = max(0, radius)
        else:
            raise TypeError()

    def get_diameter(self):
        return self.radius * 2

    def set_diameter(self, diameter):
        self.radius = diameter / 2

    def __mul__(self, other):
        if isinstance(other, int | float):
            return Kreis(self.radius * other)
        else:
            raise TypeError()

    diameter = property(get_diameter, set_diameter)
    radius = property(get_radius, set_radius)

# Noch mal in Dekoratoren

class Student:
    def __init__(self, mathe, python, englisch):
        self.mathe = mathe
        self.python = python
        self.englisch = englisch

    @property
    def durchschnitt(self):
        return (self.mathe + self.python + self.englisch) / 3

print(Student(1,2,1).durchschnitt) # 1.333333333


class Kreis:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if isinstance(radius, int | float):
            self.__radius = max(0, radius)
        else:
            raise TypeError()

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    def __mul__(self, other):
        if isinstance(other, int | float):
            return Kreis(self.radius * other)
        else:
            raise TypeError()
        

'''statische und Klassenmethoden
   Statische Methothen werden mit @staticmethod dekoriert und haben 
   keinen Zugriff auf die Instanz oder die Klasse. Sie sind wie normale Funktionen

   Klassenmethoden werden mit @classmethod dekoriert und haben Zugriff auf die Klasse, 
   aber nicht auf die Instanz. Sie erhalten die Klasse als ersten Parameter
   (meist cls genannt) und können damit auf Klassenattribute und andere Klassenmethoden zugreifen.
'''
# statische Methode (besonders gern für Utility-Funktionen, die keinen Zugriff auf Instanz oder Klasse benötigen)
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

       # Die statischen Methoden können direkt von der Klasse aufgerufen werden
celsius_temp = 25
fahrenheit_equivalent = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp} Grad Celsius entsprechen {fahrenheit_equivalent:.2f} Grad Fahrenheit.")

fahrenheit_temp = 77
celsius_equivalent = TemperatureConverter.fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp} Grad Fahrenheit entsprechen {celsius_equivalent:.2f} Grad Celsius.")

# Klassenmethode (besonders nützlich für alternative Konstruktoren oder Methoden, die auf Klassenebene arbeiten)
class Car:
    total_cars = 0

    def __init__(self, brand):
        self.brand = brand
        Car.total_cars += 1

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

total = Car.get_total_cars()
print(total)

car1 = Car("Volkswagen")
car2 = Car("Toyota")

total_now = Car.get_total_cars()
print(total_now)

# verschiedene Ursprünge
class Person:
    person_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.person_count += 1

    @classmethod
    def get_count(cls):
        """
        Gibt zurück, wie viele Personen bisher erstellt wurden.
        """
        return cls.person_count

    @classmethod
    def from_dict(cls, person_dict):
        """
        Erstellt ein Person-Objekt aus einem Dictionary.

        :param person_dict: Ein Dictionary mit den Schlüsseln 'name' und 'age'.
        :return: Ein Person-Objekt.
        """
        return cls(person_dict['name'], person_dict['age'])

    @classmethod
    def from_person(cls, parent):
        """
        Erstellt eine Junior-Person basierend auf einer bestehenden Person.

        :param parent: Person, deren Namen als Grundlage dient.
        :return: Ein Person-Objekt mit Namenszusatz 'Jr.' und Alter 0.
        """
        return cls(parent.name + " Jr.", 0)

import unittest

class TestPerson(unittest.TestCase):
    def setUp(self):
        # Vor jedem Test wird der Zähler zurückgesetzt
        Person.person_count = 0

    def test_init(self):
        p = Person("Alice", 30)
        self.assertEqual(p.name, "Alice")
        self.assertEqual(p.age, 30)

    def test_from_dict(self):
        p = Person.from_dict({'name': 'Bob', 'age': 40})
        self.assertEqual(p.name, "Bob")
        self.assertEqual(p.age, 40)

    def test_from_person(self):
        parent = Person("Walter", 50)
        p = Person.from_person(parent)
        self.assertEqual(p.name, "Walter Jr.")
        self.assertEqual(p.age, 0)

    def test_get_count(self):
        Person.from_person(Person("Walter", 50))
        self.assertEqual(Person.get_count(), 2)