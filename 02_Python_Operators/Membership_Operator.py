
#? What is Python Membership Operator?
"""
  Python membership operators are used to test whether a value 
  is included in a sequence or not.
  Two membership operators are available in Python:
  #? in: Returns True if a value is found in the sequence.
  #? not in: Returns True if a value is not found in the sequence.
"""

# Example code for membership operators
# Using the in operator with strings and lists- 
# y in x
x = [1, 2, 3, 4, 5]
x = [1, 2, 3, 4, 5]
y = 3
print(y in x)  # Output: True (3 is present in the list x)

# Using the in operator with strings
name = "Alice"
print("A" in name)  # Output: True ('A' is present in the string name)



# Using the not in operator with strings and lists
# y not in x
x = [1, 2, 3, 4, 5]
y = 6
print(y not in x)  # Output: True (6 is not present in the list x)

# Using the not in operator with strings
student = "Bob"
print("A" not in student)  # Output: True ('A' is not present in the string student)



