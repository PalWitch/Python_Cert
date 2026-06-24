# Gemeinsame Hobbys
'''
Gegeben sind zwei Listen mit Hobbys von zwei Personen:

hobbys_anna = ["Lesen", "Schwimmen", "Kochen", "Yoga"]
hobbys_ben = ["Kochen", "Gaming", "Lesen", "Radfahren"]

Finde mithilfe von Sets heraus, welche Hobbys beide gemeinsam haben. Gib das Ergebnis aus.
'''

hobbys_anna = ["Lesen", "Schwimmen", "Kochen", "Yoga"]
hobbys_ben = ["Kochen", "Gaming", "Lesen", "Radfahren"]

gemeinsam = set(hobbys_anna) & set(hobbys_ben)
print(gemeinsam)  # {'Lesen', 'Kochen'}

# Alternativ mit Methode:

gemeinsam = set(hobbys_anna).intersection(hobbys_ben)


# Fehlende Zutaten
'''
Du hast ein Rezept und einen Vorrat. Finde heraus, welche Zutaten dir fehlen.

rezept = {"Mehl", "Zucker", "Eier", "Butter", "Milch"}
vorrat = {"Mehl", "Eier", "Milch"}
'''
rezept = {"Mehl", "Zucker", "Eier", "Butter", "Milch"}
vorrat = {"Mehl", "Eier", "Milch"}

fehlend = rezept - vorrat
print(fehlend)  # {'Zucker', 'Butter'}

# Alternativ mit Methode:

fehlend = rezept.difference(vorrat)


# Kursverwaltung
'''
In einer Programmierschule gibt es drei Kurse. Jeder Kurs hat eine Teilnehmerliste:

python_kurs = {"Anna", "Ben", "Clara", "David", "Eva"}
java_kurs = {"Ben", "Frank", "Clara", "Gina"}
web_kurs = {"Anna", "Gina", "Hugo", "David"}

Löse folgende Teilaufgaben:
    Finde alle Teilnehmer insgesamt (ohne Duplikate).
    Finde Teilnehmer, die in allen drei Kursen sind.
    Finde Teilnehmer, die nur im Python-Kurs sind (und in keinem anderen).
    Finde Teilnehmer, die genau zwei Kurse besuchen.
    Prüfe, ob der python_kurs ein Superset aller Teilnehmer ist, die in Python und Java sind.
        Tipps:
        Vereinigung: | oder .union()
        Schnittmenge: & oder .intersection()
        Differenz: - oder .difference()
'''

python_kurs = {"Anna", "Ben", "Clara", "David", "Eva"}
java_kurs = {"Ben", "Frank", "Clara", "Gina"}
web_kurs = {"Anna", "Gina", "Hugo", "David"}

# 1. Alle Teilnehmer
alle = python_kurs | java_kurs | web_kurs
print("Alle:", alle)

# 2. In allen drei Kursen
in_allen = python_kurs & java_kurs & web_kurs
print("In allen drei:", in_allen)  # set() – niemand ist in allen drei

# 3. Nur im Python-Kurs
nur_python = python_kurs - java_kurs - web_kurs
print("Nur Python:", nur_python)  # {'Eva'}

# 4. Genau zwei Kurse
# Idee: In mindestens zwei, aber nicht in allen drei
in_py_und_java = python_kurs & java_kurs
in_py_und_web = python_kurs & web_kurs
in_java_und_web = java_kurs & web_kurs

in_mindestens_zwei = in_py_und_java | in_py_und_web | in_java_und_web
genau_zwei = in_mindestens_zwei - in_allen
print("Genau zwei Kurse:", genau_zwei)  # {'Anna', 'Ben', 'Clara', 'David', 'Gina'}

# 5. Superset-Prüfung
py_und_java = python_kurs & java_kurs  # {'Ben', 'Clara'}
print("Python ist Superset von Python∩Java:", python_kurs.issuperset(py_und_java))  # True
