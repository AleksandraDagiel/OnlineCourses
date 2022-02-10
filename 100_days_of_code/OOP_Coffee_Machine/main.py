from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_machine_on = True
coffee_menu = menu.get_items()

while is_machine_on:
    user_choice = input(f"What would you like? ({coffee_menu}): ")
    if user_choice == 'off':
        is_machine_on = False
    elif user_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        ordered_drink = menu.find_drink(user_choice)
    if coffee_maker.is_resource_sufficient(ordered_drink):
        coffee_price = ordered_drink.cost
        payment_successful = money_machine.make_payment(cost=coffee_price)
        if payment_successful:
            coffee_maker.make_coffee(ordered_drink)




