from resources import resources
from menu import MENU

# Coffee Machine Program Requirements
# The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.


def coffee_choice():
    user_coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
    # 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    if user_coffee_choice == "off":
        exit()
    # 3. Print report.
    elif user_coffee_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit_money}")
        coffee_choice()
    elif user_coffee_choice == "espresso" or user_coffee_choice == "latte" or user_coffee_choice == "cappuccino":
        print(f"Your drink choice: {user_coffee_choice}")
        return user_coffee_choice
    else:
        print("You have chosen wrong drink.")
        coffee_choice()


# 4. Check resources sufficient?
def check_resources_sufficient(coffee_type):
    """Check if there are enough water, milk and coffee to make chosen coffee."""
    if 'milk' in MENU[coffee_type]['ingredients']:
        for resource in resources:
            if MENU[coffee_type]['ingredients'][resource] > resources[resource]:
                print(f'Sorry there is not enough {resource}.')
                coffee_choice()
    else:
        if MENU[coffee_type]['ingredients']['coffee'] > resources['coffee']:
            print('Sorry there is not enough coffee.')
            coffee_choice()
        elif MENU[coffee_type]['ingredients']['water'] > resources['water']:
            print('Sorry there is not enough water.')
            coffee_choice()


#  5. Process coins.
def money_insert():
    """Returns how much money user inserted to the machine."""
    print("Please insert coins.")
    coins_quarters = int(input("How many quarters? "))
    coins_dimes = int(input("How many dimes? "))
    coins_nickles = int(input("How many nickles? "))
    coins_pennies = int(input("How many pennies? "))
    coins_total = (coins_quarters * 0.25) + (coins_dimes * 0.1) + (coins_nickles * 0.05) + (coins_pennies * 0.05)
    print(f"Total money inserted: ${coins_total}")
    return coins_total


def check_if_enough_money(coffee, money_inserted):
    if MENU[coffee]['cost'] == money_inserted:
        return MENU[coffee]['cost']
    elif MENU[coffee]['cost'] < money_inserted:
        money_to_return = money_inserted - MENU[coffee]['cost']
        print(f"Here is ${round(money_to_return, 3)} dollars in change.")
        return 0
    else:
        print(f"Money needed: ${MENU[coffee]['cost']}; Money inserted: ${money_inserted}.")
        print("Sorry that's not enough money. Money refunded.")
        coffee_choice()


profit_money = 0
coffee_type = coffee_choice()
check_resources_sufficient(coffee_type)
profit_money += check_if_enough_money(coffee_type, money_insert())


# TODO 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.
# TODO 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.
