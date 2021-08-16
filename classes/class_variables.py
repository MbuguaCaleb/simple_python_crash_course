class Employee:

    raise_amount = 1.04
    no_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@gmail.com'

        Employee.no_of_employees += 1

    def fullname(self):
        return '{}{}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Caleb', 'Mbugua', 100000)
emp_2 = Employee('Mercy', 'Wanjiru', 70000)

# Class Variables are variables that are shared among all instances of
# a class

# Instnace variables are unique to each class and they are the ones
# called from our constructor method

print(emp_1.pay)

emp_1.apply_raise()
print(emp_1.pay)


# I can change the raise amount from the class or from the instance itself

print(emp_1.__dict__)

# Print class variable
print(emp_1.raise_amount)


emp_1.raise_amount = 2.5
print(emp_1.__dict__)


Employee.raise_amount = 3
print(emp_2.raise_amount)

print(Employee.no_of_employees)
