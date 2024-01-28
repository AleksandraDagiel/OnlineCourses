class Student:

    def __init__(self, student_id, name, age, gpa):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gpa = gpa

    def __str__(self):
        return f"Student {self.name} " \
               f"| Student ID { self.student_id} " \
               f"| Age: {self.age} " \
               f"| GPA: {self.gpa}"


# student = Student("43S233", "Nora Nac", 23, 4.32)
# print(student)


class Backpack:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("This item is not in the backpack")

    def __len__(self):
        return len(self.items)


my_backpack = Backpack()
my_backpack.add_item("Water Bottle")
my_backpack.add_item("First Aid Kit")
my_backpack.add_item("Sleeping Bag")
print(len(my_backpack))

my_backpack.remove_item("Sleeping Bag")
print(len(my_backpack))


class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point2D(new_x, new_y)

    def __str__(self):
        return f"{self.x}, {self.y}"


# pointA = Point2D(5, 6)
# pointB = Point2D(2, 3)
#
# pointC = pointA + pointB
# print(pointC)


class Bookshelf:

    def __init__(self):
        self.content = [[],
                        [],
                        []]

    def add_book(self, book, location):
        self.content[location].append(book)

    def take_book(self, book, location):
        self.content[location].remove(book)

    def __getitem__(self, location):
        return self.content[location]


my_bookshelf = Bookshelf()

my_bookshelf.add_book("Les Miserables", 0)
my_bookshelf.add_book("Pride and Prejudice", 0)
my_bookshelf.add_book("Frankenstein", 0)

my_bookshelf.add_book("Sense and Sensibility", 1)
my_bookshelf.add_book("Jane Eyre", 1)
my_bookshelf.add_book("The Little Prince", 1)

my_bookshelf.add_book("Moby Dick", 2)
my_bookshelf.add_book("The Adventures of Huckleberry Fin ", 2)
my_bookshelf.add_book("Dracula", 2)

# print(my_bookshelf[0])


class BankAccount:

    def __init__(self, account_owner, account_number, initial_balance):
        self.account_owner = account_owner
        self.account_number = account_number
        self.balance = initial_balance

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def __bool__(self):
        return self.balance > 0


my_account = BankAccount("Nora Nav", "345-455-43234", 45322.42)
print(my_account.balance)
print(bool(my_account.balance))

my_account.balance = 0
print(my_account.balance)
print(bool(my_account.balance))


class Circle:

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def __lt__(self, other):
        return (self.radius < other.radius
                and self.color == other.color)

    def __le__(self, other):
        return (self.radius <= other.radius
                and self.color == other.color)

    def __gt__(self, other):
        return(self.radius > other.radius
               and self.color == other.color)

    def __ge__(self, other):
        return (self.radius >= other.radius
                and self.color == other.color)

    def __eq__(self, other):
        return (self.radius == other.radius
                and self.color == other.color)

    def __ne__(self, other):
        return (self.radius != other.radius
                or self.color != other.color)


circleA = Circle(5, "Blue")
circleB = Circle(5, "Green")
circleC = Circle(7, "Red")
circleD = Circle(5, "Blue")

print(circleA <= circleB)
print()