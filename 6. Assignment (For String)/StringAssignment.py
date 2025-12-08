"""
String Assignment we will do together:

Ask the user how many days until their birthday
and print an approx number of weeks until their birthday

Weeks is = 7 days

decimals within the return is allowed..
"""

days = int(
    input("How many days until your birthday? ")
)  # if the input is not convertable to int, the value will throw an error

print(type(days))  # to check the type of the variable days
print(round(days / 7, 2))  # round to 2 decimal places
