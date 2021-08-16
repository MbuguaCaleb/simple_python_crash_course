# A Tuple is a collection which is ordered and unchangeable.
# Allows duplicate members.

# Its just like a list but it is unchangeable
fruits = ('Apples', 'Oranges', 'Grapes')

fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# print(fruits, fruits2)

# If you only have one item in a tuple then you must
# Have a trailing Comma

# Otherwise it gonna be looked like a String

fruits = ('Apples',)

print(fruits, type(fruits))


# A Set is a collection which is unordered and unindexed.
# No duplicate members.
fruits_set = {'Apples', 'Oranges', 'Mango'}

# check if in set
# remember a set is unindex
# so i cannot access values like i would in a list
print('Apples' in fruits_set)

# add to set
fruits_set.add('Lemon')

print(fruits_set)


fruits_set.remove('Mango')

print(fruits_set)

# clear srt
fruits_set.clear()
print(fruits_set)


# Delete
##del fruits_set


# Sets do not allow duplicated
fruits_set.add('Apples')
