
# What is Python Dictionaries?

# Example 1: Create a dictionary
# A dictionary is a collection of items that are unordered, changeable, and indexed.

myFavFruits = {
    "fruits": "apple",
    "vegetables": "carrot",
    "juice": "orange"
}

print(myFavFruits)  # Output: {'fruits': 'apple', 'vegetables': 'carrot', 'juice': 'orange'}


# Example 2: Access items in a dictionary
# You can access the items of a dictionary by referring to its key name, inside square brackets.

# Access the items of a dictionary
myFavFruits1 = {
    "fruits": "apple",
    "vegetables": "carrot",
    "juice": "orange"
}

x = myFavFruits1["fruits"]
y = myFavFruits1["vegetables"]

print(x)  # Output: apple
print(y)  # Output: carrot

# Access the items of a dictionary using the get() method

myFavFruits2 = {
    "fruits": "apple",
    "vegetables": "carrot",
    "juice": "orange"
}

x = myFavFruits2.get("juice")

print(x)  # Output: orange

# Example 3: Change items in a dictionary

# Change the value of a specific item by referring to its key name

myFavFruits3 = {
    "fruits": "apple",
    "vegetables": "carrot",
    "juice": "orange"
}

myFavFruits3["juice"] = "mango"

print(myFavFruits3)  # Output: {'fruits': 'apple', 'vegetables': 'carrot', 'juice': 'mango'}


print()


# Example 4: Loop through a dictionary

# Loop through a dictionary
myFavFruits4 = {
    "fruits": "apple",
    "vegetables": "carrot",
    "juice": "orange"
}

for x in myFavFruits4:
    print(x)
    # Output:
    # fruits
    # vegetables
    # juice
    
# Loop through a dictionary

myFavFruits5 = {
    "fruits": "apple",
    "vegetables": "carrot",
    "juice": "orange"
}

for x in myFavFruits5:
    print(myFavFruits5[x])
    # Output:
    # apple
    # carrot
    # orange
    

print()  

  
# Example 5: Check if Key Exists

# Check if "juice" is present in the dictionary

myFavFruits6 = {
    "fruits": "apple",
    "vegetables": "carrot",
    "juice": "orange"
}

if "juice" in myFavFruits6:
    print("Yes, 'juice' is one of the keys in the myFavFruits6 dictionary")
    # Output: Yes, 'juice' is one of the keys in the myFavFruits6 dictionary
    
# Example 6: Check the length of a dictionary

# Check the length of a dictionary

myFavFruits7 = {
    "fruits": "apple",
    "vegetables": "carrot",
    "juice": "orange"
}

print(len(myFavFruits7))  # Output: 3

# Example 7: Adding items to a dictionary

# Adding an item to the dictionary is done by using a new index key and assigning a value to it.

# Add an item to a dictionary

myFavFruits8 = {
    "fruits": "apple",
    "vegetables": "carrot",
    "juice": "orange"
}

myFavFruits8["color"] = "red"

print(myFavFruits8)  # Output: {'fruits': 'apple', 'vegetables': 'carrot', 'juice': 'orange', 'color': 'red'}

# Example 8: Remove items from a dictionary

# Remove an item from a dictionary

myFavFruits9 = {
    "fruits": "apple",
    "vegetables": "carrot",
    "juice": "orange"
}

myFavFruits9.pop("juice")

print(myFavFruits9)  # Output: {'fruits': 'apple', 'vegetables': 'carrot'}

# Remove the last item from a dictionary using the popitem() method

myFavFruits10 = {
    "fruits": "apple",
    "vegetables": "carrot",
    "juice": "orange"
}

myFavFruits10.popitem()

print(myFavFruits10)  # Output: {'fruits': 'apple', 'vegetables': 'carrot'}

# Remove an item from a dictionary using the del keyword

myFavFruits11 = {
    "fruits": "apple",
    "vegetables": "carrot",
    "juice": "orange"
}

del myFavFruits11["juice"]

print(myFavFruits11)  # Output: {'fruits': 'apple', 'vegetables': 'carrot'}


print()
# Clear a dictionary using the clear() method

myFavFruits12 = {
    "fruits": "apple",
    "vegetables": "carrot",
    "juice": "orange"
}

myFavFruits12.clear()

print(myFavFruits12)  # Output: {}

# Example 9: Copy a dictionary

# Copy a dictionary using the copy() method

myFavFruits13 = {
    "fruits": "apple",
    "vegetables": "carrot",
    "juice": "orange"
}

myFavFruits14 = myFavFruits13.copy()

print(myFavFruits14)  # Output: {'fruits': 'apple', 'vegetables': 'carrot', 'juice': 'orange'}

# Copy a dictionary using the dict() method

myFavFruits15 = {
    "fruits": "apple",
    "vegetables": "carrot",
    "juice": "orange"
}

myFavFruits16 = dict(myFavFruits15)

print(myFavFruits16)  # Output: {'fruits': 'apple', 'vegetables': 'carrot', 'juice': 'orange'}


