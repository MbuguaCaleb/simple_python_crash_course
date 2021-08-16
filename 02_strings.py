# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = "Caleb"
age = 25

# concateename
# method one
#print('Hello, My name is' + name + 'and i am ' + str(age) + 'Years')


# String Formatting

# Postional Arguments

# Like back ticks then i add .format function
# Helps me avoid casting
#print('My name is {name} and I am {age}'.format(name=name, age=age))

# f string(Python 3.6 and After)
#print(f'Hello, My name is {name} and i am {age}')

# String Methods
s = 'helloworld'

# capitalize String
# Remember this i a method this i must have parantesis
print(s.capitalize())

# all uper case
print(s.upper())

# all lower
print(s.lower())

print(s.swapcase())

# can be used both in Strings ans Arrays
print(len(s))

# Replace
# It is doing the replacement despite the case
print(s.replace('world', 'everyone'))

# will count the no of h in sub
sub = 'h'
print(s.count('sub'))

# Starts With
print(s.startswith('hello'))

# Ends With
print(s.endswith('d'))

# split into a list
print(s.split())


# Find Postion
print(s.find('r'))


# is all alphabetic
print(s.isalpha())

# is all aplhanumberic
print(s.isalnum())

# is all numeric
print(s.isnumeric())
