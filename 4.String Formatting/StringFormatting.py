"""
String Formatting
"""

# Example 1 (using the f-string)
first_name = "Eric"
# Method 1 (using the + operator)
print("Hello " + first_name)
# Method 2 (using the f-string, only use the curly braces when we are using the f-string)
print(f"Hello {first_name}")

# Example 2 (using the format method)
sentence = "Hi {} {}"  # the order of the placeholder matters because it will be replaced in the order that we pass the arguments
last_name = "Roby"
print(
    sentence.format(first_name, last_name)
)  # the first_name will be replaced in the first placeholder and the last_name will be replaced in the second placeholder
print("My name is {} and I am {} years old".format(first_name, 25))

print(f"Hi {first_name} {last_name} I hope you are learning")
