# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""


x = 1  # int
y = 2.5  # float
name = 'Caleb Will Pass Python Interview'  # str

# Booleans must have a capital T or Capitat F
is_cool = True  # bool

# Multiple Assignment
x, y, name, is_cool = (1, 2.5, 'Caleb', True)


# Used to Output Data
print('Hello')
print(is_cool)
print(x, y, name, is_cool)


# Basic Math
a = x+y
print(a)

# getting type of a variable
print(type(x))

# cast x into String
x = str(x)

# cast float to int
y = int(y)


print(type(x))
print(type(y), y)


z = float(y)

print(type(z), z)
