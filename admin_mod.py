import database as db
import ui

def admin_mode(drinks):
    while True:
        ui.admin_menu(drinks)
        choice = input("Válasszon italt: ")
        if choice == '0':
            break
        elif choice == str(len(drinks) + 1):
            new_drink = {}
            new_drink['name'] = input("name: ") or drink['name']
            new_drink['unit'] = input("unit: ") or drink['unit']
            new_drink['price'] = int(input("price: ") or drink['price'])
            new_drink['stock'] = int(input("stock: ") or drink['stock'])
            drinks.append(new_drink)
            db.export_drinks(drinks)
        else:
            index = int(choice) - 1
            if 0 <= index < len(drinks):
                drink = drinks[index]
                drink['name'] = input(f"name[{drink['name']}]: ") or drink['name']
                drink['unit'] = input(f"unit[{drink['unit']}]: ") or drink['unit']
                drink['price'] = int(input(f"price[{drink['price']}]: ") or drink['price'])
                drink['stock'] = int(input(f"stock[{drink['stock']}]: ") or drink['stock'])

    db.export_drinks(drinks)