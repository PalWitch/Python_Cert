# Benutzereingaben filtern und sortieren #
##########################################

kunden = []

while True:
    # in while true, damit beliebig viele Eingaben erfolgen können
    print("Bitte beginnen Sie mit der Kundeneingabe: \n")
    eingabe = input('Kunde: "Name, Alter, eMail" oder "ende": ')
    if eingabe.lower() == "ende":
        break

    daten = [daten.strip() for daten in eingabe.split(",")]
    if len(daten) != 3:
        print("Bitte exakt Name, Alter und eMail eingeben.")
        continue
    
    name, alter_string, email = daten
    '''Kurz für:
       name = daten[0]
       alter_string = daten[1]
       email = daten[2]
    '''
    if not alter_string.isdigit():
        print("Das Alter muss eine Zahl sein.")
        continue

    kunden.append({"name": name, "alter": int(alter_string), "email": email})

gefiltert = [kunde for kunde in kunden if kunde["alter"] > 30]
gefiltert.sort(key=lambda kunde: kunde["alter"], reverse=True)
''' in Python ist eine lambda‑Funktion immer eine kleine anonyme Funktion 
    – also eine Funktion ohne Namen, die in einer Zeile genau einen Ausdruck 
    auswertet und dessen Ergebnis zurückgibt.
    lambda kunde: kunde["alter"] gibt für jeden Kunden das Alter zurück
    und sort() verwendet diesen Wert als Sortierschlüssel.
''' 

if not gefiltert:
    print("Es wurden keine Kunden über 30 gefunden.")
else:
    for kunde in gefiltert:
        print(f'{kunde["name"]}: {kunde["alter"]}, {kunde["email"]}')