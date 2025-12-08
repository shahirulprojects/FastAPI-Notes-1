"""
Lists are a collection of data
"""

my_list = [80, 96, 72, 100, 8]
print(my_list)
print(
    my_list[-1]
)  # print the last element of the list, equivalent to my_list[len(my_list) - 1]

my_list[1] = 9  # replace the value at the specified index
print(my_list)

my_list.append(1000)  # assign a value to the end of the list
print(my_list)

my_list.insert(2, 1000)  # insert a value at the specified index
print(my_list)

my_list.remove(8)  # remove the first occurrence of the specified value
print(my_list)

my_list.pop(0)  # remove the value at the specified index
print(my_list)

my_list.sort(
    reverse=True
)  # sort the list in descending order, if in ascending order, we just use my_list.sort()
print(my_list)

print(
    my_list[0:2]
)  # print the elements from index 0 to 2, but not including 2 (slicing)

print(my_list[2:])  # print the elements from index 2 to the end of the list

print(
    my_list[:2]
)  # print the elements from the start to index 2, but not including 2 (slicing)

print(
    my_list[0:5:2]
)  # print the elements from index 0 to 5, but not including 5, but take every 2nd element (selang 1)

my_list.clear()  # clear the list
print(my_list)
