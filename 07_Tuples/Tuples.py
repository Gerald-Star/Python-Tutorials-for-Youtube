
# ? Python Tuples
#! Tuple is one of the built-in data types in Python. 
#! Others include List, Set, and Dictionary.

# A tuple is a collection of items that are ordered and immutable.
# Tuples are written with round brackets.
# Tuple items are indexed, the first item has index [0], the second item has index [1], and so on.
# Tuple items are ordered, meaning that the items have a defined order, and that order will not change.
# Tuple items are immutable, meaning that we cannot change, add, or remove items after the tuple has been created.
# Tuple items do not need to be of the same data type.
# Tuple items can be of any data type: string, int, bool, etc.
# Tuple items are allowed to be duplicated.
# Tuple items are unchanged, meaning that we cannot change, add, or remove items after the tuple has been created.

#? TUPLE USE CASES

# Use a tuple when the order of elements is important and you want to ensure that the collection of items does not change.
# Use a tuple when you want to store multiple items in a single variable.
# Use a tuple when you want to return multiple values from a function.
# Use a tuple when you want to use a collection of items as a key in a dictionary.
# Use a tuple when you want to use a collection of items in a set.
# Use a tuple when you want to use a collection of items in a list.
# Use a tuple when you want to use a collection of items in a dictionary.


#* Example 1: Create a tuple
# A tuple is a collection of items that are ordered and immutable.


fruits = ("apple", "banana", "cherry")
print(fruits)  # Output: ('apple', 'banana', 'cherry')

# Example 2: Access items in a tuple
# Tuple items are indexed, the first item has index [0], the second item has index [1], and so on.

# Access items in a tuple
fruits = ("apple", "banana", "cherry")
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry

# Access items in a tuple using negative index
fruits = ("apple", "banana", "cherry")
print(fruits[-1])  # Output: cherry
print(fruits[-2])  # Output: banana
print(fruits[-3])  # Output: apple


#? Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items.

fruits_range = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(fruits_range[2:5])  # Output: ('cherry', 'orange', 'kiwi')

# Note: The search will start at index 2 (included) and end at index 5 (not included).
# By leaving out the start value, the range will start at the first item.

print(fruits_range[:4])  # Output: ('apple', 'banana', 'cherry', 'orange')

# By leaving out the end value, the range will go on to the end of the list.

print(fruits_range[2:])  # Output: ('cherry', 'orange', 'kiwi', 'melon', 'mango')


# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the tuple:

print(fruits_range[-4:-1])  # Output: ('orange', 'kiwi', 'melon')

print()

#? Example 3: Change the value of a tuple item
# Tuple items are immutable, meaning that we cannot change, add, or remove items after the tuple has been created.
"""
fruits = ("apple", "banana", "cherry")
fruits[0] = "orange"  # TypeError: 'tuple' object does not support item assignment

"""

# Example 4: Loop through a tuple
# Loop through a tuple

fruits = ("apple", "banana", "cherry")
for x in fruits:
    print(x)
# Output:
# apple
# banana
# cherry


# Example 5: Check if an item exists in a tuple
# Check if an item exists in a tuple
fruits = ("apple", "banana", "cherry")
if "banana" in fruits:
    print("Yes, 'banana' is in the fruits tuple")
# Output: Yes, 'banana' is in the fruits tuple

# Example 6: Check the length of a tuple
# Check the length of a tuple

fruits = ("apple", "banana", "cherry")
print(len(fruits))  # Output: 3


# Example 7: Tuple allows duplicate values
# Tuple allows duplicate values
fruits = ("apple", "banana", "cherry", "banana")
print(fruits)  # Output: ('apple', 'banana', 'cherry', 'banana')

# Example 8: Tuple items can be of any data type
# Tuple items can be of any data type
fruits = ("apple", 5, True, "banana")
print(fruits)  # Output: ('apple', 5, True, 'banana')


print()

# Example 9: Tuple type of
# Tuple type of
fruits = ("apple", "banana", "cherry")
print(type(fruits))  # Output: <class 'tuple'>

# Example 10: Create a tuple with one item
# To create a tuple with one item, you must add a comma after the item, otherwise Python will not recognize it as a tuple.
# Create a tuple with one item
fruits = ("apple",)
print(fruits)  # Output: ('apple',)
print(type(fruits))  # Output: <class 'tuple'>

#! Different from type string

fruits = ("apple")
print(fruits)  # Output: apple
print(type(fruits))  # Output: <class 'str'>

print()

#?  Example 11: Tuple constructor


fruits = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(fruits)  # Output: ('apple', 'banana', 'cherry')

# Example 12: Tuple constructor with one item
# Tuple constructor with one item
fruits = tuple(("apple",))  # note the double round-brackets
print(fruits)  # Output: ('apple',)

# Example 13: Tuple constructor with multiple data types
# Tuple constructor with multiple data types

fruits = tuple(("apple", 5, True, "banana"))  # note the double round-brackets
print(fruits)  # Output: ('apple', 5, True, 'banana')

# Example 14: Tuple constructor with multiple data types
# Tuple constructor with multiple data types

fruits = tuple(("apple", 5, False, "banana"))  # note the double round-brackets
print(fruits)  # Output: ('apple', 5, False, 'banana')


# To check if an item exists in a tuple, use the in keyword:

# Example 15: Check if an item exists in a tuple
# Check if an item exists in a tuple

fruits = ("apple", "banana", "cherry")
if "banana" in fruits:
    print("Yes, 'banana' is in the fruits tuple")
# Output: Yes, 'banana' is in the fruits tuple

# Example 16: Check if an item does not exist in a tuple

# Check if an item does not exist in a tuple
fruits = ("apple", "banana", "cherry")
if "orange" not in fruits:
    print("Yes, 'orange' is not in the fruits tuple")