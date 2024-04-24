
# Logical operators are used to combine multiple conditions in an expression. 
# They are used to evaluate whether a given condition is true or false. 
# There are three logical operators in Python:

#? AND, OR, and NOT.

#? Logical AND operator 
# RETURNS True if both statements are true

#! Example 1
x = 5
y = 10

if x > 0 and y > 0:
  print("Both x and y are greater than 0")
else:
  print("Either x or y is not greater than 0")

print()  



#? Logical OR operator 
# RETURNS True if one of the statements is true

#! Example 1
if x > 0 or y > 0:
  print("Either x or y is greater than 0")
  
#! Example 2  
name = "Alice"
age = 25

# Using or operator with non-boolean values
result = name == "Alice" or age > 30
print("Result:", result) # Output: Result: True

print()  




#? Logical NOT operator 
# RETURNS True the statement is false

#! Example 1
x = 5
y = 10

# Using and operator with non-boolean values
result = x < y and x * 2 == y
print("Result:", result) # Output: Result: True


#! Example 2

flag = True

# Using not operator with boolean values
result = not flag
print("Result:", result)
# Output: Result: False



# ? Going Deeper: Combining multiple logical operators

# ! Example 1
x = 15
y = 20
z = 25

# Combining multiple logical operators






#? Using logical operators in if statements
# ! Example 1

  