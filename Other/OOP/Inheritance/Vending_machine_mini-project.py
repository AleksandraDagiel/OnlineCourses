class VendingMachine:
    total_revenue = 0  # Total revenue of all vending machines in the system

    snack_prices = {"candy": 2.00, "soda": 1.50, "chips": 3.00, "cookies": 3.50}

    def __init__(self, inventory, serial, days_until_maintenance):
        self.inventory = inventory
        self.revenue = 0
        self.serial = serial
        self.days_until_maintenance = days_until_maintenance

    def sales_menu(self):

        while True:

            greetings = "\nWelcome! I have:\n"
            request = "\nPlease enter the number of the item: "

            print(greetings)

            i = 1
            for snack in self.inventory:
                print("(" + str(i) + ") " + snack.capitalize())
                i += 1

            cust_input = int(input(request))

            while cust_input <= 0 or cust_input > len(self.inventory):
                print("Please enter a number from 1 to", len(self.inventory))
                cust_input = int(input(request))

            self.process_sale(list(self.inventory.keys())[cust_input - 1].lower())
            answer = int(input("\nWould you like to buy another snack?\nEnter 1 for YES and 0 for NO: "))

            if not answer:
                break

    def process_sale(self, option):  # option must be in lowercase

        print("\nYou selected: %s" % option.capitalize())

        if self.inventory[option] > 0:

            print("Great! I currently have %d %s in my inventory\n" % (self.inventory[option], option))

            num_items = int(input("How many %s would you like to buy?\n" % option))

            while num_items <= 0:
                print("Please enter a positive integer")
                num_items = int(input("\nHow many %s would you like to buy?\n" % option))

            if num_items <= self.inventory[option]:
                self.remove_from_inventory(option, num_items)

                total = self.update_revenue(option, num_items)

                print("That would be: $ " + str(total))

                print("\nThank you for your purchase!")
                print("Now I have %d %s and my revenue is $%d" % (self.inventory[option], option, self.revenue))

            else:
                print("I don't have so many %s. Sorry! :(" % option)

        else:
            print("I don't have any more %s. Sorry! :(" % option)

    def remove_from_inventory(self, option, num_items):
        self.inventory[option] -= num_items

    def update_revenue(self, option, num_items):
        # Find price of the snack
        price = self.find_snack_price(option)

        # Update Instance and class
        self.revenue += num_items * price
        VendingMachine.total_revenue += num_items * price

        return num_items * price

    def find_snack_price(self, snack):
        return VendingMachine.snack_prices[snack]

    def display_revenue(self):
        print("The total revenue of this vending machine is:", self.revenue)


class HospitalVendingMachine(VendingMachine):

    snack_prices = {"candy": 1.00, "soda": 0.50, "chips": 2.00, "cookies": 1.50}

    def __init__(self, inventory, serial, days_until_maintenance):
        VendingMachine.__init__(self, inventory, serial, days_until_maintenance)

    def sales_menu(self):
        print("Welcome to our Hospital Vending Machine \nWe hope you are feeling better today!")
        VendingMachine.sales_menu(self)


    def find_snack_price(self, snack):
        return HospitalVendingMachine.snack_prices[snack]

    def print_days_until_maintenance(self):
        print("I have %d days until maintenance, thanks for asking." % self.days_until_maintenance)


class SchoolVendingMachine(VendingMachine):

    snack_prices = {"candy": 3.20, "soda": 2.50, "chips": 1.10, "cookies": 8.00}
    student_debt = {"Lulu": 500, "Gino": 100, "Penelope": 150}

    def __init__(self, inventory, serial, days_until_maintenance):
        VendingMachine.__init__(self, inventory, serial, days_until_maintenance)

    def sales_menu(self):
        print("Welcome to our School Vending Machine \nWe hope you have a great day full of learning!")
        VendingMachine.sales_menu(self)

    def find_snack_price(self, snack):
        return SchoolVendingMachine[snack]

    def print_student_debt(self, name):
        print("The debt of %s with this vending machine is: $%d" % (name, SchoolVendingMachine.student_debt[name.capitalize()]))


floor_machine = VendingMachine({"candy": 36, "soda": 15, "chips": 40, "cookies": 120}, "011423424", 24)
floor_machine.sales_menu()

hospital_machine = HospitalVendingMachine({"candy": 32, "soda": 50, "chips": 45, "cookies": 80}, "03223424", 15)
# hospital_machine.sales_menu()

school_machine = SchoolVendingMachine({"candy": 36, "soda": 15, "chips": 40, "cookies": 120}, "0534424", 2)
# school_machine.sales_menu()