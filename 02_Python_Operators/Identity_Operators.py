"""
Python identity operators are used to compare the memory locations of two objects. There are two identity operators in Python:

#? is: Returns True if both operands are the same object.
#? is not: Returns True if both operands are not the same object.
"""

# Example code for identity operators

# Define two variables
x = 5
y = 5

# Check if x and y refer to the same object
if x is y:
  print("x and y refer to the same object")

# Check if x and y refer to different objects
if x is not y:
  print("x and y refer to different objects")

print()  
#? Using is operator:  

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)  # Output: False (x and y are different objects even though they have the same content)
print(x is z)  # Output: True (x and z reference the same object)
print(x == y)  # Output: True (x and y have the same content, equals value)

print()
# ? Using is not operator:

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is not y)  # Output: True (x and y are different objects)
print(x is not z)  # Output: False (x and z reference the same object)


# 
# ? Using identity operators with None:

x = None
y = None

print(x is None)    # Output: True
print(y is not None)  # Output: False

#? Using identity operators with integers

a = 10
b = 10
c = 20

print(a is b)   # Output: True (a and b reference the same object)
print(a is not c)  # Output: True (a and c are different objects)

#? Using identity operators with strings:

s1 = "hello"
s2 = "hello"
s3 = "world"

print(s1 is s2)   # Output: True (s1 and s2 reference the same object)
print(s1 is not s3)  # Output: True (s1 and s3 are different objects)
  