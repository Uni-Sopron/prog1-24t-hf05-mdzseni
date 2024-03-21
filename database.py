import json

DRINKS = "data/drinks.json"
GUESTS = "data/guests.json"

ENTITIES = list[dict[str, str | int]]

def export_drinks(drinks: ENTITIES) -> None:
    with open(DRINKS, "w", encoding="utf-8") as f:
        json.dump(drinks, f, ensure_ascii=False, indent=4)

def export_guests(guests: ENTITIES) -> None:
    with open(GUESTS, "w", encoding="utf-8") as f:
        json.dump(guests, f, ensure_ascii=False, indent=4)

def import_guests() -> ENTITIES:
    with open(GUESTS, encoding="utf-8") as f:
        return json.load(f)

#Added import_drinks
def import_drinks() -> ENTITIES:
    with open(DRINKS, encoding="utf-8") as f:
        return json.load(f)

def new_guest(name: str) -> bool:
    guests = import_guests()
    for g in guests:
        if g["name"] == name:
            return False
    guests.append({"name": name, "balance": 0})
    export_guests(guests)
    return True