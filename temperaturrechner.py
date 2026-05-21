#########################################################################
# Dies wird ein einfacher Umrechner von Celsius und Fahreheit in Python #
#########################################################################

print("Herzlich Willkommen zum 'einfachen Temperaturrechner' by AnnK\n")

wert = float(input("Bitte gib den Wert der Temperatur an.\n"))

einheit = input("\nBitte gib an, ob die Temperatur in Celsius 'C' oder Fahrenheit 'F' ist.\n")

if einheit == "C":
    fahrenheit = (wert * 9/5) + 32
    print(f"\nDie Temperatur in Fahrenheit beträgt: {fahrenheit:.2f} F")
elif einheit == "F":
    celsius = (wert - 32) * 5/9
    print(f"\nDie Temperatur in Celsius beträgt: {celsius:.2f} C")
else:
    print(f"\nUngültige Eingabe. Bitte gib 'C' für Celsius oder 'F' für Fahrenheit ein.")