# A List is a collection which is ordered and changeable. Allows duplicate members.

# create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pear']

# use a constructor
numbers2 = list((1, 2, 3, 4, 5))

print(fruits[2])

print(len(fruits))

# When it comes to Python, Its Not Push but append
fruits.append('Melon')

print(fruits)


fruits.remove('Grapes')

print(fruits)


# Insert into Positon
fruits.insert(2, 'Strawberries')

print(fruits)

# Change Value
fruits[0] = 'BlueBerries'

# Remove from certain postions
fruits.pop(2)

print(fruits)

# Reverse List
fruits.reverse()

print(fruits)

# Sort
fruits.sort()

print(fruits)

# Reverse Sort
fruits.sort(reverse=True)

print(fruits)
