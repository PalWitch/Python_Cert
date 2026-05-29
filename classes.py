class Roboter:
    pass

x = Roboter()
y = Roboter()
y2 = y

print(f'id von x: {id(x)}')
print(f'id von y: {id(y)}')
print(f'id von y2: {id(y2)}')

# Typ untersuchen

print(f"Typ von x: {type(x)}")
print(f"Typ von y: {type(y)}")
print(f"Typ von y2: {type(y2)}")

# mehrere Instanzen erzeugen
class Car: 
    pass

a = Car() 
b = Car() 
c = Car()

print(f"a ID: {id(a)}")
print(f"b ID: {id(b)}")
print(f"c ID: {id(c)}")

# ------------------

class Roboter:
    pass

x = Roboter()
y = Roboter()

x.name = 'Marvin'
x.baujahr = 1990

y.name = 'Justin'
y.baujahr = 2005

print(x.__dict__)
print(y.__dict__)


# Durchschnittsnote berechnen
class student:
    pass
Max = student()
Max.name = "Max Mustermann"
Max.Mathenote = 2.0
Max.Deutschnote = 1.0
Max.Englischnote = 1.5  

print(f"{Max.name} hat folgende Durchschnittsnote: {(Max.Mathenote + Max.Deutschnote + Max.Englischnote) / 3:.2f}")

# -------------------
class Buchhaltung: 
    pass

booking = Buchhaltung() 
booking.food_spending = 100 
booking.car_spending = 230 
booking.february_income = 200

summe = 0 
for name, value in booking.__dict__.items(): 
    if 'spending' in name: summe += value

print(summe)

print(sum(value for name, value in booking.__dict__.items() if 'spending' in name))

# Instanz als Parameter übergeben
class Person: 
    pass

anna = Person() 
anna.name = "Anna Lena Zitrova"

karl = Person() 
karl.name = "Karl Gustav"

def getInitials(person): 
    return "".join(word[0] for word in person.name.split())

print(getInitials(anna)) # 'ALZ' print(getInitials(karl)) # 'KG'

# Koordinaten setzen
class Point: 
    def set_coordinates(self, x, y):    # Methode
        self.x = x 
        self.y = y

    def get_coordinates(self):          # Methode
        return self.x, self.y

point = Point() 
point.set_coordinates(3, 5) 
x, y = point.get_coordinates()
print(f"Punkt hat den x-Wert {x} und den y-Wert {y}")

# Koordinaten von vornherein setzen
class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 

    def set_coordinates(self, x, y): 
        self.x = x 
        self.y = y

    def get_coordinates(self):
        return self.x, self.y

point = Point(4, 7) 
x, y = point.get_coordinates() 
print(f"Punkt hat den x-Wert {x} und den y-Wert {y}")

# Auf in den Kampf!
class Gladiator: 
    def __init__(self,name, hitpoints, attackpower): 
        self.name = name 
        self.hitpoints = hitpoints 
        self.attackpower = attackpower

    def attack(self, enemy):
        enemy.hitpoints -= self.attackpower

    def is_alive(self):
        return self.hitpoints > 0

    def health_check(self):
        if self.is_alive():
            return f"{self.name} hat noch {self.hitpoints} HP."
        else:
            return f"{self.name} liegt am Boden."

attacker = Gladiator(name="Glassy", hitpoints=10, attackpower=20) 
defender = Gladiator(name="Tanky", hitpoints=30, attackpower=5)

print(defender.health_check()) # Tanky hat noch 30 HP 
attacker.attack(defender) 
print(defender.health_check()) # Tanky hat noch 10 HP 
attacker.attack(defender) 
print(defender.health_check()) # Tanky liegt am Boden

# Ab in die Arena!
class Arena: 
    def __init__(self, attacker: Gladiator, defender: Gladiator): 
        self.attacker = attacker 
        self.defender = defender

    def fight(self):
        while self.attacker.is_alive() and self.defender.is_alive():
            self.attacker, self.defender = self.defender, self.attacker
            self.attacker.attack(self.defender)

        winner = self.attacker if self.attacker.is_alive() else self.defender

        print(f"The winner is {winner.name}!🎉🎉🎉")

arena = Arena(attacker=attacker, defender=defender)

arena.fight()       
