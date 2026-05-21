#################################################
# Dies wird ein einfacher Zinsrechner in Python #
#################################################

print("Herzlich Willkommen zum 'einfachen Zinsrechner' by AnnK\n")

anfangskapital = input("Bitte gib die Zahl ein, deren Endsumme du mit Zinsen haben möchtest.\n")
zinssatz       = input("\nBitte gib den Prozentsatz des Zinses ein.\n")
anlagedauer    = input("\nBitte gib die Anlagedauer in Jahren ein.\n")

endsumme = float(anfangskapital) * (1 + (float(zinssatz) / 100) * float(anlagedauer))
print(f"Die Endsumme beträgt: {endsumme:.2f} Euro")