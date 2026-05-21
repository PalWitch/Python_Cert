#########################################################
# Dies wird ein Programm, das einen Tannenbaum zeichnet #
#########################################################

wahl = int(input("Bitte gib die Breite des Tannenbaums (ungerade Zahl) ein: "))

zeilen_krone = (wahl + 1) // 2
mitte        = wahl // 2         # mittlere Spalte

# Baumkrone
for zeile in range(zeilen_krone):             # äußere Schleife: Zeilen
    for spalte in range(wahl):                # innere Schleife: Spalten
        linker_stern  = mitte - zeile
        rechter_stern = mitte + zeile

        if linker_stern <= spalte <= rechter_stern:
            print("*", end="")
        else:
            print(" ", end="")
    print()  # Zeilenumbruch

# Stamm
for spalte in range(wahl):
    if mitte - 1 <= spalte <= mitte + 1:
        print("|", end="")
    else:
        print(" ", end="")
print()