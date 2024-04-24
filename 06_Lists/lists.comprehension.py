
# * Example 13: List comprehension
# * List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# * Example 1: Create a new list using list comprehension
fruits1 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = [x for x in fruits1 if "a" in x]
print(newlist1)  # Output: ['apple', 'banana', 'mango']

# * Example 2: Create a new list using list comprehension
fruits_2 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist2 = [x for x in fruits_2]
print(newlist2)  # Output: ['apple', 'banana', 'cherry', 'kiwi', 'mango']

print()

# * Example 3: Create a new list using list comprehension
fruits_3 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist3 = [x for x in fruits_3 if x != "apple"]
print(newlist3)  # Output: ['banana', 'cherry', 'kiwi', 'mango']

# * Example 4: Create a new list using list comprehension
fruits_4 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist4 = [x for x in fruits_4 if x == "apple"]
print(newlist4)  # Output: ['apple']


# * Example 5: Create a new list using list comprehension
fruits_5 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist5 = [x.upper() for x in fruits_5]
print(newlist5)  # Output: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

print()

# * Example 6: Create a new list using list comprehension
fruits_6 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist6 = ['hello' for x in fruits_6]
print(newlist6)  # Output: ['hello', 'hello', 'hello', 'hello', 'hello']

# * Example 7: Create a new list using list comprehension
fruits_7 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist7 = [x if x != "banana" else "orange" for x in fruits_7]
print(newlist7)  # Output: ['apple', 'orange', 'cherry', 'kiwi', 'mango']

# * Example 8: Create a new list using list comprehension
fruits_8 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist8 = [x for x in fruits_8 if x != "banana"]
print(newlist8)  # Output: ['apple', 'cherry', 'kiwi', 'mango']


# * Example 9: Create a new list using list comprehension
fruits_9 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist9 = []
for x in fruits_9:
    if "a" in x:
        newlist9.append(x)
print(newlist9)  # Output: ['apple', 'banana', 'mango']

