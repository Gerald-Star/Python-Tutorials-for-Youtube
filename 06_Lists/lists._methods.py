
# ? Lists Examples

# * List is a collection which is ordered and changeable. Allows duplicate members.
#  * Example 1: Create a list

myFavFruits = ["orange", "mango", "cherry"]
print(myFavFruits)  # Output: ['orange', 'mango', 'cherry']


print()
# * List items are indexed, the first item has index [0], the second item has index [1], and so on.
# * Example 2: Access items in a list
myFavFruits1 = ["blueberry", "mango", "cherry"]
print(myFavFruits1[0])  # Output: blueberry
print(myFavFruits1[1])  # Output: mango
print(myFavFruits1[2])  # Output: cherry
print(myFavFruits1[-1])  # Output: cherry
print(myFavFruits1[-2])  # Output: mango
print(myFavFruits1[-3])  # Output: blueberry

# * Example 3: Change the value of a list item by adding another list
myFavFruits2 = ["blueberry", "mango", "cherry"]
myFavFruits2[0] = "orange"
print(myFavFruits2)  # Output: ['orange', 'mango', 'cherry']

# * Example 4: Loop through a list
myFavFruits3 = ["blueberry", "mango", "cherry"]
for x in myFavFruits3:
    print(x)
# Output:
# blueberry
# mango
# cherry

# * Example 5: Change the value of a List item by removing another list
myFavFruits4 = ["kiwi", "mango", "pineapple"]
myFavFruits4.remove("kiwi")
print(myFavFruits4)  # Output: ['mango', 'pineapple']


print()
# * Example 7: Check if an item exists in a list
myFavFruits5 = ["kiwi", "mango", "pineapple"]
if "mango" in myFavFruits5:
    print("Yes, 'mango' is in the fruits list")
# Output: Yes, 'mango' is in the fruits list

# * Example 8: Check the length of a list
myFavFruits6 = ["kiwi", "mango", "pineapple"]
print(len(myFavFruits6))  # Output: 3


# * Example 9: List allows duplicate values
myFavFruits7 = ["kiwi", "mango", "pineapple", "mango"]
print(myFavFruits7)  # Output: ['kiwi', 'mango', 'pineapple', 'mango']
list_index = myFavFruits7[1]
print(list_index)  # Output: 1
# mean mango is at index 1

print()

# * Example 10: List can contain different data types
myFavFruits8 = ["kiwi", 5, True, "mango", "pineapple"]
print(myFavFruits8)  # Output: ['kiwi', 5, True, 'mango', 'pineapple']

# * Example 11: List type of 
myFavFruits9 = ["kiwi", "mango", "pineapple"]
print(type(myFavFruits9))  # Output: <class 'list'>

# * Example 12: List constructor
myFavFruits10 = list(("kiwi", "mango", "pineapple"))  # note the double round-brackets
print(myFavFruits10)  # Output: ['kiwi', 'mango', 'pineapple']


# * Python List Methods

# * Example 1: append() method
# * Adds an element at the end of the list

myFavFruits11 = ["banana", "pawpaw", "pineapple"]

myFavFruits11.append("orange")
print(myFavFruits11)  # Output: ['kiwi', 'mango', 'pineapple', 'orange']

# Another append() method example

cars1 = ["Ford", "Volvo", "BMW"]
cars2 = ["Jeep", "Kia", "Honda"]
for x in cars2:
    cars1.append(x)
print(cars1)  # Output: ['Ford', 'Volvo', 'BMW', 'Jeep', 'Kia', 'Honda']

print()

# * Example 2: insert() method
# * Adds an element at the specified position
myFavFruits12 = ["banana", "pawpaw", "pineapple"]
myFavFruits12.insert(1, "orange")

print(myFavFruits12)  # Output: ['banana', 'orange', 'pawpaw', 'pineapple']

# * Example 3: remove() method
# * Removes the specified element
myFavFruits13 = ["banana", "pawpaw", "pineapple"]
myFavFruits13.remove("banana")

print(myFavFruits13)  # Output: ['pawpaw', 'pineapple']

# * Example 4: pop() method
# * Removes the specified index, (or the last item if index is not specified)
myFavFruits14 = ["banana", "pawpaw", "pineapple"]
myFavFruits14.pop()

print(myFavFruits14)  # Output: ['banana', 'pawpaw']


# * Example 5: del keyword
# * Removes the specified index
myFavFruits15 = ["banana", "pawpaw", "pineapple"]
del myFavFruits15[0]
print(myFavFruits15)  # Output: ['pawpaw', 'pineapple']

print()

# * Example 6: clear() method
# * Empties the list
myFavFruits16 = ["banana", "pawpaw", "pineapple"]
myFavFruits16.clear()
print(myFavFruits16)  # Output: []

# * Example 7: copy() method
# * Returns a copy of the list
myFavFruits17 = ["banana", "pawpaw", "pineapple"]
myFavFruits18 = myFavFruits17.copy()
print(myFavFruits18)  # Output: ['banana', 'pawpaw', 'pineapple']


# OR another format of using copy() method

myFavFruits17 = ["banana", "pawpaw", "pineapple"]
myFavFruits18 = list(myFavFruits17)
print(myFavFruits18)  # Output: ['banana', 'pawpaw', 'pineapple']


# * Example 8: count() method
# * Returns the number of elements with the specified value
myFavFruits19 = ["banana", "pawpaw", "pineapple"]
x = myFavFruits19.count("banana")
print(x)  # Output: 1

print()

# * Example 9: extend() method
# * Add the elements of a list (or any iterable), to the end of the current list
myFavFruits20 = ["banana", "pawpaw", "pineapple"]
myFavFruits21 = ["orange", "mango", "cherry"]
myFavFruits20.extend(myFavFruits21)
print(myFavFruits20) 
# Output: ['banana', 'pawpaw', 'pineapple', 'orange', 'mango', 'cherry']


# OR another format of using extend() method

car3 = ["Ford", "Volvo", "BMW"]
car4 = ["Jeep", "Kia", "Honda"]
car3 += car4
print(car3)  # Output: ['Ford', 'Volvo', 'BMW', 'Jeep', 'Kia', 'Honda']

print()

# * Example 10: index() method
# * Returns the index of the first element with the specified value
myFavFruits22 = ["banana", "pawpaw", "pineapple"]
x = myFavFruits22.index("pineapple")
print(x)  # Output: 2

# * Example 11: reverse() method
# * Reverses the order of the list
myFavFruits23 = ["banana", "pawpaw", "pineapple"]
myFavFruits23.reverse()
print(myFavFruits23)  # Output: ['pineapple', 'pawpaw', 'banana']

# * Example 12: sort() method
# * Sorts the list
myFavFruits24 = ["banana", "pawpaw", "pineapple"]
myFavFruits24.sort()
print(myFavFruits24)  # Output: ['banana', 'pawpaw', 'pineapple']


