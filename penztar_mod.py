import database as db
import ui

def new_costumer(guests):
    name = input("Add meg a nevet: ")
    for guest in guests:
        if guest['name'] == name:
            print("Létezik már ilyen nevű vendég")
            return guests
    guests.append({"name": name, "balance": 0})
    db.export_guests(guests)
    return guest

def order(drinks, guests):
    ui.guests_list(guests)
    guest_idx = int(input("Válasszon vendéget:"))
    if guest_idx == 0:
        return
    ui.drinks_list(drinks)
    drink_idx = int(input("Válasszon italt: "))
    if drink_idx == 0:
        return
    dl = int(input("Mennyiség dl egységben: "))

    if dl <= 0:
        print('Nemnegatív egész számot adjon meg!')
    drink = drinks[drink_idx]
    if drink['stock'] < dl:
        print("Nincs elég készlet! (A visszalépéshez adjon meg 0 mennyiséget.)")
        return order(drinks, guests)
    
    guest = guests[guest_idx]
    price = drink['price'] * dl
    guest['balance'] += price
    drink['stock'] -= dl

    db.export_drinks(drinks)
    db.export_guests(guests)
    print(f"+{price} Ft {guest['name']} számlájára írva, egyenleg: {guest['balance']} Ft")

def pay(guests):
    ui.guests_list(guests)
    guest_idx = int(input("Válasszon vendéget: "))
    amount = int(input("Adja meg a befizetett összeget Ft-ban: "))
    if amount <= 0:
        print("Nemnegatív számot adjon meg!")
        return pay(guests)
    guests[guest_idx]['balance'] += amount

    db.export_guests(guests)
    print(f"{amount} Ft befizetve, új egyenleg: {guests[guest_idx]['balance']} Ft")

 