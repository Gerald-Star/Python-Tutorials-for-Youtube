
# Logical operators are used to combine multiple conditions in an expression. 
# They are used to evaluate whether a given condition is true or false. 
# There are three logical operators in Python:
#? and, or, and not.

#? Logical AND operator RETURNS True if both statements are true
x = 5
y = 10

if x > 0 and y > 0:
  print("Both x and y are greater than 0")
else:
  print("Either x or y is not greater than 0")

print()  
#? Logical OR operator RETURNS True if one of the statements is true
if x > 0 or y > 0:
  print("Either x or y is greater than 0")

print()  
#? Logical NOT operator RETURNS True if the statement is false


x = 5
y = 10

# Using and operator with non-boolean values
result = x < y and x * 2 == y
print("Result:", result)
# Output: Result: True


name = "Alice"
age = 25

# Using or operator with non-boolean values
result = name == "Alice" or age > 30
print("Result:", result)
# Output: Result: True


flag = True

# Using not operator with boolean values
result = not flag
print("Result:", result)
# Output: Result: False


x = 15
y = 20
z = 25

# Combining multiple logical operators
result = x < y and y < z or x == z
print("Result:", result)
# Output: Result: True


x = 10
y = 20
z = 30

# Using logical operators in if statements
if x < y and y < z:
    print("Both conditions are true.")
else:
    print("At least one condition is false.")
# Output: Both conditions are true.
  