class Employee:

    def __init__(self, full_name, salary):
        self.full_name = full_name
        self.salary = salary


class Programmer(Employee):

    def __init__(self, full_name, salary, programming_language):
        Employee.__init__(self, full_name, salary)
        self.programming_language = programming_language


nora = Programmer("Nora Nav", 60000, "Python")
print(nora.full_name)
print(nora.salary)
print(nora.programming_language)
