
# Unpack Tuples
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

# Example 1: Packing a tuple
fruits = ("mango", "guava", "pineapple")
print(fruits)  # Output: ('mango', 'guava', 'pineapple')

print()

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

# Example 2: Unpacking a tuple

fruits = ("mango", "guava", "pineapple")
(mango, guava, pineapple) = fruits

print(mango)  # Output: mango
print(guava)  # Output: guava
print(pineapple)  # Output: pineapple

print()

# Using Asterisk *

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

# Example 3: Unpacking a tuple with an asterisk

fruits = ("mango", "guava", "pineapple", "apple", "banana", "cherry")

(mango, guava, *rest) = fruits

print(mango)  # Output: mango
print(guava)  # Output: guava
print(rest)  # Output: ['pineapple', 'apple', 'banana', 'cherry']

print()

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

# Example 4: Unpacking a tuple with an asterisk

fruits = ("mango", "guava", "pineapple", "apple", "banana", "cherry")

(orange, *middle, kiwi) = fruits

print(orange)  # Output: mango
print(middle)  # Output: ['guava', 'pineapple', 'apple', 'banana']

print(kiwi)  # Output: cherry