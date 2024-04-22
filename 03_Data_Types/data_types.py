
#? Primitive Data Types in Python

# Integers
x = 5
y = -10
print(x, y)
print(type(x), type(y))

# Floating-point numbers
pi = 3.14
e = 2.71828
print(pi, e)
print(type(pi), type(e))


# Complex numbers
z = 3 + 4j
print(z)
print(type(z))

# Strings
message = "Hello, World!"
name = 'Alice'
print(message, name)
print(type(message), type(name))


# Boolean
is_valid = True
has_finished = False
print(is_valid, has_finished)
print(type(is_valid), type(has_finished))

# NoneType
empty_variable = None
print(empty_variable)
print(type(empty_variable))

print()


 
#? Non-Primitive Data Types in Python

#? Lists
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
print(numbers, names)
print(type(numbers), type(names))

print()

#? Tuples
# Tuples (tuple): Tuples are similar to lists, but they are immutable,
# meaning their values cannot be changed after creation. 
# Tuples are defined using parentheses ().

coordinates = (10, 20)
colors = ("red", "green", "blue")
print(coordinates, colors)
print(type(coordinates), type(colors))

print()

#? Sets
# Sets (set): Sets are unordered collections of unique elements. 
# They are mutable, but unlike lists and tuples, they do not allow duplicate elements. 
# Sets are defined using curly braces {}.

fruits = {"apple", "banana", "orange"}
animals = {"cat", "dog", "elephant"}
print(fruits, animals)
print(type(fruits), type(animals))

print()

#? Dictionaries
# Dictionaries (dict): Dictionaries are unordered collections of key-value pairs. 
# Each key is unique and associated with a value. 
# Dictionaries are mutable and are defined using curly braces {}.

person = {"name": "Alice", "age": 25, "city": "New York"}
car = {"brand": "Tesla", "model": "Model 3", "year": 2022}
print(person, car)
print(type(person), type(car))


# Frozen Sets (frozenset): Frozen sets are similar to sets, but they are immutable, 
# meaning their elements cannot be changed after creation. 
# Frozen sets are defined using the frozenset() function.

my_frozenset = frozenset([1, 2, 3, 4, 5])
print(my_frozenset)
print(type(my_frozenset))