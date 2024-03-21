def main_menu():
    print("\n0 - Kilépés")
    print("1 - Pénztáros mód")
    print("2 - Admin mód")

def cashier_menu(): 
        print("\n0 - Vissza a főmenübe")
        print("1 - Új törzsvendég")
        print("2 - Rendelés")
        print("3 - Befizetés")

def admin_menu(drinks):
    print("0 - Vissza")
    for i, drink in enumerate(drinks, 1):
        print(f"{i} - {drink['name']}: {drink['price']} Ft/{drink['unit']}")
    print(f"{len(drinks) + 1} - Új ital hozzáadása")

def guests_list(guests):
    for i, guest in enumerate(guests, 1):
        print(f"{i} - {guest['name']}: {guest['balance']} Ft")

def drinks_list(drinks):
    for i, drink in enumerate(drinks, 1):
        if drink['stock'] > 0:
            print(f"{i} - {drink['name']}: {drink['price']} Ft/{drink['unit']}")