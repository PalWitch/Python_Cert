'''
Ein einzelner Stern * entpackt eine Liste, ein Tupel oder eine andere Sequenz in einzelne Positionsargumente.
Zwei Sterne ** entpacken ein Dictionary in benannte Argumente.
'''

# *args: Ausgabe vorhersagen
'''
Welche Ausgabe erzeugt der Code?
'''
def show_items(*items):
    print(type(items))
    print(items)
    print(len(items))

show_items("Laptop", "Maus", "Tastatur")
'''
Lösung:

<class 'tuple'>
('Laptop', 'Maus', 'Tastatur')
3

*items sammelt alle Positionsargumente in einem Tupel.
'''

# **kwargs: Ausgabe vorhersagen

'''
Welche Ausgabe erzeugt der Code?
'''
def show_settings(**settings):
    print(type(settings))
    print(settings["theme"])
    print(settings.get("debug", False))


show_settings(theme="dark", language="de")
'''
Lösung:

class 'dict'
dark
False

**settings sammelt benannte Argumente in einem Dictionary. Da debug nicht uebergeben wurde, liefert get("debug", False) den Defaultwert.
'''


# Flexible Rechnung mit args und kwargs
'''
Schreibe eine Funktion calculate_total(*prices, **options).
Anforderungen:

    prices enthaelt beliebig viele Preise.
    options kann discount enthalten, z.B. discount=0.1 fuer 10 Prozent.
    options kann shipping enthalten, z.B. shipping=4.99.
    Fehlen die Optionen, gelten discount=0 und shipping=0.
    Rueckgabe ist der Gesamtpreis nach Rabatt plus Versand.

Beispiel:
print(calculate_total(10, 20, 30, discount=0.1, shipping=4.99))
'''

def calculate_total(*prices, **options):
    discount = options.get("discount", 0)
    shipping = options.get("shipping", 0)

    subtotal = sum(prices)
    discounted_total = subtotal * (1 - discount)
    return discounted_total + shipping

print(calculate_total(10, 20, 30, discount=0.1, shipping=4.99))


# Entpacken mit * und ** debuggen
'''
Der Code soll create_user("Ada", "Lovelace", active=True, role="admin") aufrufen, 
aber die Werte liegen in einer Liste und einem Dictionary.

Repariere den Aufruf.

def create_user(first_name, last_name, active=False, role="user"):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "active": active,
        "role": role,
    }

names = ["Ada", "Lovelace"]
options = {"active": True, "role": "admin"}

user = create_user(names, options)
print(user)
'''

def create_user(first_name, last_name, active=False, role="user"):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "active": active,
        "role": role,
    }

names = ["Ada", "Lovelace"]
options = {"active": True, "role": "admin"}

user = create_user(*names, **options)
print(user)

'''
*names entpackt die Liste in Positionsargumente. **options entpackt das Dictionary in benannte Argumente.
'''
