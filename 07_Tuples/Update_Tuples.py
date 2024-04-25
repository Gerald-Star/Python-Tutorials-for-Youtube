
# To update Tuples, you can convert them to a list, update the list, and convert the list back into a tuple.

# Example: Change the second item in the tuple to "kiwi":

fruits = ("apple", "banana", "cherry")
y = list(fruits)
y[1] = "kiwi"
fruits = tuple(y)
print(fruits)  # Output: ('apple', 'kiwi', 'cherry')


# Add Items
# Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
# But there is a workaround. You can convert the tuple into a list, add your item(s), and convert the list back into a tuple.

# Example: Add "orange" to the fruits tuple:

fruits = ("apple", "banana", "cherry")
y = list(fruits)
y.append("orange")
fruits = tuple(y)
print(fruits)  # Output: ('apple', 'banana', 'cherry', 'orange')

# Remove Items
# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
# Convert the tuple into a list, remove the item(s), and convert the list back into a tuple.

# Example: Remove "banana" from the tuple:

fruits = ("apple", "banana", "cherry")
y = list(fruits)
y.remove("banana")
fruits = tuple(y)
print(fruits)  # Output: ('apple', 'cherry')

print()
# The del keyword can delete the tuple completely:

fruits = ("apple", "banana", "cherry")
del fruits
# print(fruits)  # This will raise an error because the tuple no longer exists
# Output: NameError: name 'fruits' is not defined

# Join Two Tuples
# To join two or more tuples you can use the + operator:

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)  # Output: ('a', 'b', 'c', 1, 2, 3)

print()
#* Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator:

fruits_multiply = ("apple", "banana", "cherry")
fruits_multiply = fruits_multiply * 2

print(fruits_multiply)  # Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# Tuple Methods
# Python has two built-in methods that you can use on tuples.

# count() Method
# The count() method returns the number of times a specified value appears in the tuple.

fruits_count = ("apple", "banana", "cherry", "apple")

x = fruits_count.count("apple")
print(x)  # Output: 2

# index() Method
# The index() method finds the first occurrence of the specified value.

fruits_index = ("apple", "banana", "cherry")

x = fruits_index.index("cherry")

print(x)  # Output: 2

#! If the item is not found, a ValueError is raised:

#! fruits_index = ("apple", "banana", "cherry")

#! x = fruits_index.index("orange")

#! print(x)  # Output: ValueError: tuple.index(x): x not in tuple

#! Note: The index() method only returns the first occurrence of the value.

# Tuple Length
# To determine how many items a tuple has, use the len() method:

fruits_length = ("apple", "banana", "cherry")

print(len(fruits_length))  # Output: 3

# Note: The len() method returns the number of items in a tuple.
