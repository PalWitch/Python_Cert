import logging

class Customer:
    def __init__(self):
        self.name = None
        self.age = None

    def add_name(self, name:str):
        if not isinstance(name, str):
            logging.error("Name muss ein String sein.")
            raise TypeError("Name muss ein String sein.")
        if not name.isalpha():
            logging.error("Der Name darf nur Buchstaben enthalten.")
            raise ValueError("Der Name darf nur Buchstaben enthalten.")
           
        self.name = name
        print(f"Name: {self.name}")

    def add_age(self, age:int):
        if not isinstance(age, int):
            logging.error("Alter muss ein Integer sein.")
            raise TypeError("Alter muss ein Integer sein.")
        if age < 0 or age > 120:
            logging.error("Alter muss zwischen 0 und 120 liegen.")
            raise ValueError("Alter muss zwischen 0 und 120 liegen.")
        self.age = age
        print(f"Alter: {self.age}")

class AgeException(ValueError, TypeError):
    """Wird ausgelöst, wenn ein ungültiges Alter angegeben wird."""
    pass

def check_age(age):
    if age < 0 or age > 120:
        logging.error("Alter muss zwischen 0 und 120 liegen!")
        raise AgeException("Alter muss zwischen 0 und 120 liegen!")
    print(f"Alter {age} ist gültig.")
