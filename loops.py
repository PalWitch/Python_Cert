# while-Schleife
zaehler = 1
while zaehler <= 5:
    print(f"while-Durchlauf: {zaehler}")
    zaehler += 1

print("---")

# for-Schleife mit range()
for zahl in range(1, 6):
    print(f"for-Zahl: {zahl}")

print("---")

# for-Schleife über eine Liste
farben = ["rot", "blau", "gruen", "gelb"]
for farbe in farben:
    print(f"Farbe: {farbe}")

print("---")

# break-Beispiel
for zahl in range(1, 11):
    if zahl == 6:
        print("Abbruch bei 6")
        break
    print(zahl)

print("---")

# continue-Beispiel
for zahl in range(1, 8):
    if zahl % 2 == 0:
        continue
    print(f"Ungerade Zahl: {zahl}")

print("---")

# enumerate()-Beispiel
obst = ["Apfel", "Banane", "Kirsche"]
for index, sorte in enumerate(obst, start=1):
    print(f"{index}. {sorte}")
