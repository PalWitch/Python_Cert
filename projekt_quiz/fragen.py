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
]