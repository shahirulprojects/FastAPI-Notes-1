"""
Sets are similar to lists but are unordered (meaning it could be in any location of the memory meaning we cannot get a set by index) and cannot contain duplications
Use curly brackets
"""

my_set = {1, 2, 3, 4, 5, 1, 2}
print(my_set)  # will print {1, 2, 3, 4, 5}
print(len(my_set))  # will print 5

# looping through a set
for x in my_set:
    print(x)


my_set.discard(3)  # remove the specified value from the set if it exists
print(my_set)  # will print {1, 2, 4, 5}
my_set.add(6)  # add the specified value to the set
print(my_set)  # will print {1, 2, 4, 5, 6}
my_set.update([7, 8])  # add multiple values to the set, we cannot do my_set.add([7, 8])
print(my_set)  # will print {1, 2, 4, 5, 6, 7, 8}
my_set.clear()  # clear the set
print(my_set)

"""
Tuples are similar to lists (ordered) but are immutable (meaning we cannot change the values of the tuple once it is created)
Use parentheses
"""

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1])
# my_tuple[1] = 100  # this will raise an error because tuples are immutable
