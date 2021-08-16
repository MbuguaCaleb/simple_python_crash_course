# Classes allow us to logically group our data and functions in a way #that is easy to reuse and also easy to build upon if need be


class Employee:

    # Takes Self as the first argumnet
    # It is what is used to instanticate a class
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@gmail.com'

   # Every method in a class takes in the instance as first argument
   # automatically.
   # How am i going to access class attibutes without self
    def fullname(self):
        return '{}{}'.format(self.first, self.last)

        # Instances of a class are called Objects
emp_1 = Employee('Caleb', 'Mbugua', 100000)
emp_2 = Employee('Mercy', 'Wanjiru', 70000)


print(emp_1)
print(emp_2)


print(emp_1.email)
print(emp_2.email)

# Instance Variable
# These are variables that are unique to each instance of a class


print(emp_1.fullname())
print(emp_2.fullname())

# I can call a method from a class Name Direcly but i must pass an
# instnace for this to work

Employee.fullname(emp_1)
Employee.fullname(emp_2)


# Remember when you want to change a class variable, You may manipulate it from the class itself
