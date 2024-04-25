
#? Example 1: Create a set
#* A set is a collection of items that are unordered and unindexed.
#* Sets are written with curly brackets.

myFavFruits = {"apple", "banana", "cherry"}
print(myFavFruits)  # Output: {'apple', 'banana', 'cherry'}

#* Example 2: Access items in a set

# You cannot access items in a set by referring to an index, since sets are unordered the items have no index.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

# Loop through the set items
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

#* Example 3: Change items in a set

# Once a set is created, you cannot change its items, but you can add new items.

# Add an item to a set
myFavFruits3 = {"apple", "banana", "cherry"}
myFavFruits3.add("orange")

print(myFavFruits3)  # Output: {'apple', 'banana', 'cherry', 'orange'}

# Add multiple items to a set
myFavFruits4 = {"apple", "banana", "cherry"}
myFavFruits4.update(["orange", "mango", "grapes"])

print(myFavFruits4)  # Output: {'apple', 'banana', 'cherry', 'grapes', 'mango', 'orange'}

#* Example 4: Remove items from a set

# Remove an item from a set
myFavFruits5 = {"apple", "banana", "cherry"}

myFavFruits5.remove("banana")

print(myFavFruits5)  # Output: {'apple', 'cherry'}

# Remove an item from a set using the discard() method


myFavFruits6 = {"apple", "banana", "cherry"}
myFavFruits6.discard("banana")
print(myFavFruits6)  # Output: {'apple', 'cherry'}

# Remove the last item from a set using the pop() method
myFavFruits7 = {"apple", "banana", "cherry"}
myFavFruits7.pop()
print(myFavFruits7)  # Output: {'banana', 'cherry'}

# Clear a set using the clear() method

myFavFruits8 = {"apple", "banana", "cherry"}
myFavFruits8.clear()
print(myFavFruits8)  # Output: set()

# Delete a set using the del keyword

myFavFruits9 = {"apple", "banana", "cherry"}
del myFavFruits9
# print(myFavFruits9)  # Output: NameError: name 'myFavFruits9' is not defined

#* Example 5: Join two sets

# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:

# The union() method returns a new set with all items from both sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)  # Output: {1, 2, 3, 'b', 'c', 'a'}

# The update() method inserts all the items from one set into another:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)  # Output: {1, 2, 3, 'b', 'c', 'a'}

print()

#* Example 6: The set() Constructor

# It is also possible to use the set() constructor to make a set.

myFavFruits10 = set(("apple", "banana", "cherry"))  # note the double round-brackets

print(myFavFruits10)  # Output: {'apple', 'banana', 'cherry'}


# add() Method

# The add() method adds an element to the set.

myFavFruits11 = {"apple", "banana", "cherry"}

myFavFruits11.add("orange")

print(myFavFruits11)  # Output: {'apple', 'banana', 'cherry', 'orange'}






