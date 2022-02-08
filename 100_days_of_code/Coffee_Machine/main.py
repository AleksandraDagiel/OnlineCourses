from resources import resources
from menu import MENU


def coffee_choice(money):
    """Return coffee choice. Hidden functionalities: machine off and report."""
    user_coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_coffee_choice == "off":
        exit()
    elif user_coffee_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: $%0.2f" % money)
        coffee_choice(money)
    elif user_coffee_choice == "espresso" or user_coffee_choice == "latte" or user_coffee_choice == "cappuccino":
        print(f"Your drink choice: {user_coffee_choice}")
        return user_coffee_choice
    else:
        print("You have chosen wrong drink.")
        coffee_choice(money)


def check_resources_sufficient(coffee_type):
    """Check if there are enough water, milk and coffee to make chosen coffee."""
    if MENU[coffee_type]['ingredients']['coffee'] > resources['coffee']:
        print('Sorry there is not enough coffee.')
        return False
    elif MENU[coffee_type]['ingredients']['water'] > resources['water']:
        print('Sorry there is not enough water.')
        return False
    elif 'milk' in MENU[coffee_type]['ingredients']:
        if MENU[coffee_type]['ingredients']['milk'] > resources['milk']:
            print('Sorry there is not enough milk.')
            return False
        else:
            return True
    else:
        return True


#  5. Process coins.
def money_insert():
    """Returns how much money user inserted to the machine."""
    print("Please insert coins.")
    coins_quarters = int(input("How many quarters? "))
    coins_dimes = int(input("How many dimes? "))
    coins_nickles = int(input("How many nickles? "))
    coins_pennies = int(input("How many pennies? "))
    coins_total = (coins_quarters * 0.25) + (coins_dimes * 0.1) + (coins_nickles * 0.05) + (coins_pennies * 0.05)
    return coins_total


def check_if_enough_money(coffee, money_inserted, profit_money):
    """Check if given money is enough, if yes then give change, if no then return money."""
    if MENU[coffee]['cost'] == money_inserted:
        return MENU[coffee]['cost']
    elif MENU[coffee]['cost'] < money_inserted:
        money_to_return = money_inserted - MENU[coffee]['cost']
        print(f"Here is $%0.2f dollars in change." % money_to_return)
        return MENU[coffee]['cost']
    else:
        print(f"Money needed: ${MENU[coffee]['cost']}; Money inserted: ${money_inserted}.")
        print("Sorry that's not enough money. Money refunded.")
        coffee_choice(profit_money)


# 7. Make Coffee.
def update_resources(coffee_type):
    """Lower resources depend on coffee choice."""
    resources['water'] = resources['water'] - MENU[coffee_type]['ingredients']['water']
    resources['coffee'] = resources['coffee'] - MENU[coffee_type]['ingredients']['coffee']
    if 'milk' in MENU[coffee_type]['ingredients']:
        resources['milk'] = resources['milk'] - MENU[coffee_type]['ingredients']['milk']
    return resources


def make_coffee(profit_money):
    """Main function od coffee machine. Make your coffee!"""
    coffee_type = coffee_choice(profit_money)
    if check_resources_sufficient(coffee_type):
        profit_money += check_if_enough_money(coffee_type, money_insert(), profit_money)
        update_resources(coffee_type)
        print(f"Here is your {coffee_type}. Enjoy!")
    make_coffee(profit_money)


profit_money = 0
make_coffee(profit_money)
