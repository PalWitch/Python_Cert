# Länge eines Strings ermitteln
text = "Dies ist ein Beispiel"
print(f"Länge des Strings: {len(text)}")

# String rückwärts ausgeben
text = "Python"
print(text[::-1])

# String in Großbuchstaben konvertieren
text = "python"
print(text.upper())

# Anzahl der Vokale zählen
text = "Ich bin ein Star, holt mich hier raus!"
text = text.lower()
vocals = text.count("a") + text.count("e") + text.count("i") + text.count("o") + text.count("u")
print(f"Vokale in {text}: {vocals}")

# Erster und letzter Buchstabe eines Strings
text = "Python"
print(f"Erster Buchstabe: {text[0]}, Letzter Buchstabe: {text[-1]}")

# Zeichen ersetzen
text = "Python ist großartig."
neuer_text = text.replace("groß", "super")
print(neuer_text)

# Leerzeichen entfernen
text = " Text mit Leerzeichen "
ohne_leerzeichen = text.strip()
print(ohne_leerzeichen)

# String in Wörter aufteilen
text = "Dies ist ein Satz."
woerter = text.split()
print(woerter)

# Überprüfung, ob ein String nur aus Zahlen besteht
text = "12345"
if text.isdigit():
   print("Der String besteht nur aus Zahlen.")
else:
   print("Der String enthält andere Zeichen als Zahlen.")

# Funktion zur Überprüfung von Anagrammen
s1, s2 = "listen", "silent" 
if sorted(s1.lower()) == sorted(s2.lower()):
    print(f"{s1} ist Anagramm von {s2}")
else:
    print("Kein Anagramm")

# Anzahl der Wörter in einem String zählen
text = "Dies ist ein Beispiel Satz."
woerter = text.split()
anzahl_woerter = len(woerter)
print(f"Anzahl der Wörter: {anzahl_woerter}")

# String in Titel-Case umwandeln
text = "python ist großartig"
titel_case = text.title()
print(titel_case)

# Palindrom-Überprüfung
text = 'Anna'
text = text.lower()  # Um Groß-/Kleinschreibung zu ignorieren
if text == text[::-1]:
   print(f"{text} ist ein Palindrom")
else:
   print(f"{text} ist KEIN Palindrom")

# Vokale verboten
text = "Bastian weiß Bescheid😲"
replace_symbol = "*"
text = text.lower().replace("a", replace_symbol).replace("e", replace_symbol).replace("i", replace_symbol).replace("o", replace_symbol).replace("u", replace_symbol)
print(f"Text ohne Vokale: {text}")