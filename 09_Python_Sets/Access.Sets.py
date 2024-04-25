

# Access Sets Items

# You cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

# Example 1: Loop through the set items

myFavFruits1 = {"apple", "banana", "cherry"}
for x in myFavFruits1:
    print(x)
# Output:
# cherry
# apple
# banana

# Check if "banana" is present in the set
myFavFruits2 = {"apple", "banana", "cherry"}
print("banana" in myFavFruits2)  # Output: True

# Not in Items
# To determine if a specified item is NOT present in a set use the not in keyword.

# Example: Check if "orange" is NOT present in the set:

myFavFruits3 = {"apple", "banana", "cherry"}
print("orange" not in myFavFruits3)  # Output: True

# Change Items

# Once a set is created, you cannot change its items, but you can add new items.

# Add Items
# To add one item to a set use the add() method.

# To add more than one item to a set use the update() method.

# Example 3: Change items in a set

# Add an item to a set

myFavFruits4 = {"apple", "banana", "cherry"}

myFavFruits4.add("orange")

print(myFavFruits4)  # Output: {'apple', 'banana', 'cherry', 'orange'}

# Add multiple items to a set

myFavFruits5 = {"apple", "banana", "cherry"}

myFavFruits5.update(["orange", "mango", "grapes"])

print(myFavFruits5)  # Output: {'apple', 'banana', 'cherry', 'grapes', 'mango', 'orange'}


print()
# Remove Items

# To remove an item in a set, use the remove(), or the discard() method.

# Example 4: Remove items from a set

myFavFruits6 = {"apple", "banana", "cherry"}

myFavFruits6.remove("banana")

print(myFavFruits6)  # Output: {'apple', 'cherry'}