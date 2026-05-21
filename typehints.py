from typing import TypedDict


class Student(TypedDict):
    alter: int
    noten: list[float]


class Bericht(TypedDict):
    name: str
    alter: int
    noten: list[float]
    durchschnitt: float


def berechne_durchschnitt(noten: list[float]) -> float:
    """Berechnet den Durchschnitt einer Liste von Noten"""
    return sum(noten) / len(noten)


def finde_schueler(schueler_dict: dict[str, Student], name: str) -> Student | None:
    """Findet einen Schüler in einem Dictionary und gibt seine Informationen zurück"""
    return schueler_dict.get(name)


def formatiere_note(note: float) -> str:
    """Formatiert eine Note als String mit einem '+' wenn sie besser als 2.0 ist"""
    if note < 2.0:
        return str(note) + "+"
    return str(note)


def erstelle_bericht(name: str, alter: int, noten: list[float]) -> Bericht:
    """Erstellt einen Bericht für einen Schüler"""
    return {
        "name": name,
        "alter": alter,
        "noten": noten,
        "durchschnitt": berechne_durchschnitt(noten)
    }


def aktualisiere_alter(schueler: Student, neues_alter: int) -> Student:
    """Aktualisiert das Alter eines Schülers"""
    schueler["alter"] = neues_alter
    return schueler


def main() -> None:
    schueler_daten: dict[str, Student] = {
        "Max": {"alter": 16, "noten": [1, 2, 2, 3]},
        "Lisa": {"alter": "17", "noten": [1, 1, 2, 1]},   
        "Tom": {"alter": 16, "noten": [2, 3, 2, 4]}     
    }

    try:
        print("Schülerberichte:")
        for name, daten in schueler_daten.items():
            bericht = erstelle_bericht(name, daten["alter"], daten["noten"])
            print(f"\nBericht für {name}:")
            print(f"Alter: {bericht['alter']}")
            print(f"Notendurchschnitt: {formatiere_note(bericht['durchschnitt'])}")

        lisa_info = finde_schueler(schueler_daten, "Lisa")
        if lisa_info is not None:
            lisa_info["noten"].append(2.5)

        tom_durchschnitt: float = berechne_durchschnitt(schueler_daten["Tom"]["noten"])

        max_aktualisiert: Student = aktualisiere_alter(schueler_daten["Max"], 17)  

    except (TypeError, AttributeError) as e:
        print(f"\nFehler aufgetreten: {e}")
        print("Dieser Fehler könnte durch Type-Hints verhindert werden!")


if __name__ == "__main__":
    main()