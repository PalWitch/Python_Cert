"""
Fragen-Datenbank für die Quiz-Engine.

Jede Frage ist ein Dictionary mit:
- 'frage': Text der Frage (str)
- 'antworten': Liste von Antwortmöglichkeiten (list[str])
- 'antworten_richtig': Index der richtigen Antwort (int, 0-basiert)
- 'erklaerung': Erklärung, warum diese Antwort richtig ist (str)
- 'kategorie': Kategorie der Frage (str)
- 'schwierigkeit': Schwierigkeitsgrad (int)
"""

from typing import List, Dict, Any

Frage = Dict[str, Any]

fragen: List[Frage] = [
    {
        "frage": "Welcher Datentyp ist 5?",
        "antworten": ["int", "float", "str", "bool"],
        "antworten_richtig": 0,
        "erklaerung": "5 ist eine ganze Zahl ohne Dezimalpunkt, daher int.",
        "kategorie": "Datentypen",
        "schwierigkeit": 1,
    },
    {
        "frage": "Welcher Datentyp ist 5.0?",
        "antworten": ["int", "float", "str", "bool"],
        "antworten_richtig": 1,
        "erklaerung": "5.0 hat einen Dezimalpunkt, daher float.",
        "kategorie": "Datentypen",
        "schwierigkeit": 1,
    },
    {
        "frage": "Was gibt 3 // 2 aus?",
        "antworten": ["1", "1.5", "2", "Error"],
        "antworten_richtig": 0,
        "erklaerung": "// ist Ganzzahldivision (Floor Division), 3 // 2 ergibt 1.",
        "kategorie": "Operatoren",
        "schwierigkeit": 1,
    },
    {
        "frage": "Welche Ausgabe hat print(True and False)?",
        "antworten": ["True", "False", "None", "Error"],
        "antworten_richtig": 1,
        "erklaerung": "True and False ist False, da beide True sein müssen.",
        "kategorie": "Operatoren",
        "schwierigkeit": 1,
    },
    {
        "frage": "Welche Kontrollstruktur wiederholt Code, solange eine Bedingung wahr ist?",
        "antworten": ["if", "for", "while", "else"],
        "antworten_richtig": 2,
        "erklaerung": "Die while-Schleife wiederholt Code, solange die Bedingung True ist.",
        "kategorie": "Kontrollstrukturen",
        "schwierigkeit": 1,
    },
    {
        "frage": "Welche Syntax ist korrekt für eine if-Anweisung?",
        "antworten": [
            "if x > 0",
            "if x > 0:",
            "if (x > 0)",
            "if x > 0 then",
        ],
        "antworten_richtig": 1,
        "erklaerung": "In Python braucht die if-Zeile einen Doppelpunkt am Ende.",
        "kategorie": "Syntax",
        "schwierigkeit": 1,
    },
    {
        "frage": "Was macht der Ausdruck len([1, 2, 3])?",
        "antworten": ["Gibt 2 zurück", "Gibt 3 zurück", "Gibt 4 zurück", "Fehler"],
        "antworten_richtig": 1,
        "erklaerung": "Die Liste [1, 2, 3] hat drei Elemente, also len(...) = 3.",
        "kategorie": "Datentypen",
        "schwierigkeit": 1,
    },
    {
        "frage": "Was passiert bei int('abc')?",
        "antworten": ["0", "abc", "ValueError", "TypeError"],
        "antworten_richtig": 2,
        "erklaerung": "Ein String wie 'abc' kann nicht in int umgewandelt werden -> ValueError.",
        "kategorie": "Exceptions",
        "schwierigkeit": 1,
    },
    {
        "frage": "Welche Schleife passt zu: 'für jedes Element in einer Liste'?",
        "antworten": ["if-Schleife", "for-Schleife", "while-Schleife", "switch"],
        "antworten_richtig": 1,
        "erklaerung": "Die for-Schleife iteriert über Elemente einer Sequenz wie einer Liste.",
        "kategorie": "Kontrollstrukturen",
        "schwierigkeit": 1,
    },
    {
        "frage": "Was macht der Ausdruck print('Hallo' + ' ' + 'Welt')?",
        "antworten": [
            "Gibt HalloWelt aus",
            "Gibt Hallo Welt aus",
            "Fehler",
            "Gibt nur Hallo aus",
        ],
        "antworten_richtig": 1,
        "erklaerung": "Die Strings werden mit Leerzeichen dazwischen verkettet: 'Hallo Welt'.",
        "kategorie": "Strings",
        "schwierigkeit": 1,
    },
    {
    "frage": "Welchen Typ hat das Ergebnis von 3 + 4.0 in Python?",
    "antworten": ["int", "float", "str", "bool"],
    "antworten_richtig": 1,
    "erklaerung": "Bei einer Rechnung mit int und float wird zu float befördert, also ist das Ergebnis ein float.",
    "kategorie": "Datentypen",
    "schwierigkeit": 2,
},
{
    "frage": "Was ist der Typ von variable x nach x = True + 2?",
    "antworten": ["bool", "int", "float", "TypeError"],
    "antworten_richtig": 1,
    "erklaerung": "True wird wie 1 behandelt, daher ist True + 2 = 3 und der Typ ist int.",
    "kategorie": "Datentypen",
    "schwierigkeit": 3,
},{
    "frage": "Was ist das Ergebnis von 2 ** 3 ** 2?",
    "antworten": ["64", "512", "36", "Fehler"],
    "antworten_richtig": 1,
    "erklaerung": "Potenzierung ist rechtsassoziativ: 3 ** 2 = 9, dann 2 ** 9 = 512.",
    "kategorie": "Operatoren",
    "schwierigkeit": 3,
},
{
    "frage": "Welches Ergebnis hat der Ausdruck 10 % 3?",
    "antworten": ["0", "1", "3", "Fehler"],
    "antworten_richtig": 1,
    "erklaerung": "10 geteilt durch 3 hat Rest 1, und genau den liefert der Modulo-Operator %.",
    "kategorie": "Operatoren",
    "schwierigkeit": 2,
},{
    "frage": "Wie oft wird der Körper der Schleife ausgeführt: for i in range(2, 7, 2)?",
    "antworten": ["2 Mal", "3 Mal", "4 Mal", "5 Mal"],
    "antworten_richtig": 1,
    "erklaerung": "range(2, 7, 2) erzeugt die Werte 2, 4, 6 – also 3 Durchläufe.",
    "kategorie": "Kontrollstrukturen",
    "schwierigkeit": 2,
},
{
    "frage": "Was passiert bei while x < 5: x += 2, wenn x mit 0 startet?",
    "antworten": [
        "Endlosschleife",
        "Die Schleife läuft 2 Mal",
        "Die Schleife läuft 3 Mal",
        "Die Schleife läuft 4 Mal",
    ],
    "antworten_richtig": 2,
    "erklaerung": "x nimmt nacheinander die Werte 0, 2, 4 an und wird dann auf 6 erhöht – also 3 Durchläufe.",
    "kategorie": "Kontrollstrukturen",
    "schwierigkeit": 3,
},{
    "frage": "Welche der folgenden Zeilen ist in Python eine gültige Funktionsdefinition?",
    "antworten": [
        "def meine_funktion:",
        "def meine_funktion()",
        "def meine_funktion():",
        "funktion meine_funktion():",
    ],
    "antworten_richtig": 2,
    "erklaerung": "Eine Funktionsdefinition braucht Klammern und einen Doppelpunkt: def name():",
    "kategorie": "Syntax",
    "schwierigkeit": 2,
},
{
    "frage": "Welche Variante ist die korrekte Syntax für eine else-if-Verzweigung?",
    "antworten": ["elseif", "else if", "elif", "else: if"],
    "antworten_richtig": 2,
    "erklaerung": "In Python heißt der Zwischenschritt elif und wird ohne Leerzeichen geschrieben.",
    "kategorie": "Syntax",
    "schwierigkeit": 2,
},{
    "frage": "Welche Exception wird typischerweise bei 1 / 0 ausgelöst?",
    "antworten": ["TypeError", "ZeroDivisionError", "ValueError", "IndexError"],
    "antworten_richtig": 1,
    "erklaerung": "Division durch 0 löst in Python ZeroDivisionError aus.",
    "kategorie": "Exceptions",
    "schwierigkeit": 2,
},
{
    "frage": "Was passiert bei lst[10], wenn lst = [1, 2, 3] ist?",
    "antworten": [
        "Es wird 0 zurückgegeben",
        "Es wird None zurückgegeben",
        "IndexError",
        "ValueError",
    ],
    "antworten_richtig": 2,
    "erklaerung": "Der Index 10 existiert nicht, daher wird ein IndexError ausgelöst.",
    "kategorie": "Exceptions",
    "schwierigkeit": 3,
},{
    "frage": "Was ist das Ergebnis von 'abc' * 3?",
    "antworten": ["'abc3'", "'abcabc'", "'abcabcabc'", "Fehler"],
    "antworten_richtig": 2,
    "erklaerung": "Strings können mit einer Zahl multipliziert werden, es entsteht eine Wiederholung: 'abcabcabc'.",
    "kategorie": "Strings",
    "schwierigkeit": 2,
},
{
    "frage": "Was liefert 'Python'[1:4]?",
    "antworten": ["'Pyt'", "'yth'", "'ytho'", "'tho'"],
    "antworten_richtig": 1,
    "erklaerung": "Der Slice startet bei Index 1 (y) und geht bis vor Index 4, also 'yth'.",
    "kategorie": "Strings",
    "schwierigkeit": 3,
},
]