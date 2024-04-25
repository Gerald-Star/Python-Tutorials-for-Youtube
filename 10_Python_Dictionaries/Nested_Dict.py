


#* Example 10: Nested Dictionaries

# A dictionary can also contain many dictionaries, this is called nested dictionaries.

# Create a dictionary that contain three dictionaries

myFamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

print(myFamily)  # Output: {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

print()
#* More Example Nested Dictionaries

# Create a dictionary that contain three dictionaries

myFamily1 = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

child1 = myFamily1["child1"]
child2 = myFamily1["child2"]
child3 = myFamily1["child3"]

print(child1)  # Output: {'name': 'Emil', 'year': 2004}
print(child2)  # Output: {'name': 'Tobias', 'year': 2007}
print(child3)  # Output: {'name': 'Linus', 'year': 2011}

# Access Items in Nested Dictionaries

# Access the child1 dictionary of the myFamily dictionary

myFamily2 = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

child1 = myFamily2["child1"]["name"]

print(child1)  # Output: Emil


print()
#* Loop through a nested dictionary

# Loop through the child dictionaries of the myFamily dictionary

myFamily3 = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

for x in myFamily3:
    print(myFamily3[x]["name"])
    # Output:
    # Emil
    # Tobias
    # Linus
    
    
print()    


# Check if Key Exists

# Check if "child1" is present in the myFamily dictionary

myFamily4 = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

if "child1" in myFamily4:
    print("Yes, 'child1' is one of the keys in the myFamily4 dictionary")
    # Output: Yes, 'child1' is one of the keys in the myFamily4 dictionary

# Example 11: The dict() Constructor

# It is also possible to use the dict() constructor to make a new dictionary.

# Create a dictionary using the dict() constructor

myFavFruits17 = dict(fruits="apple", vegetables="carrot", juice="orange")

print(myFavFruits17)  # Output: {'fruits': 'apple', 'vegetables': 'carrot', 'juice': 'orange'}


print()
# Example 12: Dictionary Methods

# Python has a set of built-in methods that you can use on dictionaries.

# clear() Method
# The clear() method removes all the elements from a dictionary.

myFavFruits18 = {
    "fruits": "apple",
    "vegetables": "carrot",
    "juice": "orange"
}

myFavFruits18.clear()

print(myFavFruits18)  # Output: {}


  
        
    
        
    
