class Electronic_Device():

    def __init__(self, production_year, brand):
        self.production_year = production_year
        self.brand = brand


class Computer(Electronic_Device):

    def __init__(self, production_year, brand, memory_storage=1):
        Electronic_Device.__init__(self, production_year, brand)
        self.memory_storage = memory_storage


class TV(Electronic_Device):

    def __init__(self, production_year, brand, size):
        Electronic_Device.__init__(self, production_year, brand)
        self.size = size


class Desktop(Computer):

    def __init__(self, production_year, brand, build_in_screen=False):
        Computer.__init__(self, production_year, brand)
        self.build_in_screen = build_in_screen


class Laptop(Computer):

    def __init__(self, production_year, brand, weight):
        Computer.__init__(self, production_year, brand)
        self.weight = weight


computer = Computer(2019, "Toshiba")
print(computer.brand, computer.memory_storage)

desktop = Desktop(2023, "Asus")
desktop.memory_storage = 5
print(desktop.memory_storage)