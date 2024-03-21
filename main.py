import database as db
import admin_mod as admin
import penztar_mod as cashier
import ui

def run():
    drinks = db.import_drinks()
    guests = db.import_guests()
    while True:
        ui.main_menu()
        choice = int(input("Válasszon menüpontot: "))
        if choice == 0:
            break
        elif choice == 1:
            while True:
                ui.cashier_menu()
                cash_choice = int(input("Válasszon menüpontot: "))
                if cash_choice == 0:
                    break
                elif cash_choice == 1:
                    guests = cashier.new_costumer(guests)
                elif cash_choice == 2:
                    cashier.order(drinks, guests)
                elif cash_choice == 3:
                    cashier.pay(guests)
        elif choice == 2:
            admin.admin_mode(drinks)


if __name__ == "__main__":
    run()
