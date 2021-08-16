# Regular methods automatically take in the instance as the first argument

# Class methods take in the class as the first argument

# Static methods on the other hand dont parse anything automatically

# they behave like normal functions but we include them because they
# have a logical connection with the class

import datetime


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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # class methods as alternative constructors
    # May be data being passed into my class id formatted in a particular way
    # I can have my class method as an alterative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False

        return True


emp_1 = Employee('Caleb', 'Mbugua', 100000)
emp_2 = Employee('Mercy', 'Wanjiru', 70000)


my_date = datetime.date(2021, 7, 12)
print(Employee.is_workday(my_date))
# i can call the class method directly without passing an instance
# initially the method would not have known

# Employee.set_raise_amount(1.05)

# # same as
# Employee.raise_amount = 1.07

# print(Employee.raise_amount)
# print(emp_1.raise_amount)


# Maybe i want to format my data in a particular way before passing
# It to my constructor
# emp_str_1 = 'Caleb-Mbugua-400000'
# emp_str_2 = 'Mercy-Wanjiru-500000'

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)
