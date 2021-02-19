from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def inpint(message):
    while True:
        try:
            n = int(input(message))
        except ValueError:
            print("Not a valid input! Please enter a valid number.")
        else:
            return n


def display_menu():
    print("Welcome! What would you like to have?")
    print("\n 1.Espresso :$1.50\n 2.Latte :$2.50\n 3.Cappuccino :$3.00\n  or\n 4.Display Report\n 5.Exit")
    option = int(inpint(""))
    return option


menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
menu_opt = {1: "espresso", 2: "latte", 3: "cappuccino"}
flag = True

while flag:
    opt = display_menu()
    if 1 <= opt <= 3:
        drink = menu_opt[opt]
        item = menu.find_drink(drink)
        if coffee.is_resource_sufficient(item):
            if money.make_payment(item.cost):
                coffee.make_coffee(item)
            else:
                print("insufficient money paid.")
        else:
            print("Resource insufficient.")
    elif opt == 4:
        coffee.report()
        money.report()
    elif opt == 5:
        flag = False
    else:
        print("Invalid option. Try again")
