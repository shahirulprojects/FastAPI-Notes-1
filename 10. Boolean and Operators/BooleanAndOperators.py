"""
Boolean and Operators
"""

like_cofee = False
favourite_number = 7
favourite_food = "Lasagna"

print(type(like_cofee))
print(type(favourite_number))
print(type(favourite_food))

# Comparison Operators (note: in python, there is no === operator, we use == instead. Use == to compare values)
print(1 == 2)  # False
print(1 != 2)  # True
print(1 > 2)  # False
print(1 < 2)  # True
print(1 >= 1)  # True
print(1 <= 2)  # True

# Logical Operators
print(1 > 3 and 5 < 7)  # False
print(1 > 3 or 5 < 7)  # True
print(not (1 == 1))  # not (True) = False

# Identity Operators (Checks whether two variables point to the same object in memory, not whether they just have the same value. Use is only for None, singletons (True, False), and identity checks.)
a = [1, 2, 3]
b = [1, 2, 3]

a == b  # True  (same contents)
a is b  # False (different objects)
