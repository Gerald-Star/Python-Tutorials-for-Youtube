
# what is Boolean?
"""
Boolean is a data type that has only two possible values: True or False.
You can compare two values using comparison operators to get a Boolean result.
"""

x = 5
y = 10

result = x < y
print(result)  # Output: True
result = x > y
print(result)  # Output: False
result = x == y
print(result)  # Output: False
result = x <= y
print(result)  # Output: True
result = x >= y
print(result)  # Output: False
result = x != y
print(result)  # Output: True
result = not result
print(result)  # Output: False

# Boolean in an if statement can return True or False

if result:
  print("Result is True")
else:
  print("Result is False")
  
a = 100
b = 40

if a > b:
  print("a is greater than b")

print()  

# Boolean in an if-else statement can return True or False
a = 40
b = 400
if a > b:
  print("a is greater than b")
else:
  print("a is not greater than b")  

print()  

# Boolean in a for loop can return True or False
a = 100
b = 40
for i in range(5):
  if a > b:
    print("a is greater than b")
  else:
    print("a is not greater than b")  
    
print()
  
# Boolean in a while loop can return True or False
a = 100
b = 40
i = 0
while i < 5:
  if a > b:
    print("a is greater than b")
  else:
    print("a is not greater than b")
  i += 1
  

# Use the bool() function to get the boolean value of an object.
print()
print(bool(5))  # Output: True
print(bool(0))  # Output: False
print(bool("Hello"))  # Output: True

#? Boolean Operators
# Python provides the following boolean operators:
# and: Returns True if both statements are true
# or: Returns True if one of the statements is true
# not: Reverse the result, returns False if the result is true

X = "Greetings"
y = 10

print(X == "Greetings" and y == 10)  # Output: True

print()

X = "Greetings"
y = 10

print(X == "Hello" and y == 6)  # Output: False

# The or operator returns True if one of the statements is true.
print()
X = "Greetings"
y = 10
print(X == "Hello" or y == 10)  # Output: True

# The not operator returns False if the result is true.
print()
X = "Greetings"
y = 10
print(not(X == "Hello" and y == 6))  # Output: True


#? Short-circuit Evaluation
# Python uses short-circuit evaluation to evaluate boolean expressions.
# In a boolean expression, the evaluation stops as soon as the result is known.
# For the and operator, if the first expression is False, the result is False.
# For the or operator, if the first expression is True, the result is True.

print()
X = 5
y = 10
z = 15

result = X < y and y < z
print(result)  # Output: True

result = X < y and y > z
print(result)  # Output: False

# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

print()
print(bool("Hello"))  # Output: True
print(bool(15))  # Output: True
print(bool(["apple", "banana", "cherry"]))  # Output: True


# Some Values are False
# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None.
# And of course the value False evaluates to False.

print()

print(bool(False))  # Output: False
print(bool(None))  # Output: False
print(bool(None))  # Output: False
print(bool(0))  # Output: False
print(bool(""))  # Output: False
print(bool(""))  # Output: False
print(bool([]))  # Output: False
print(bool({}))  # Output: False


# Using _len_() function to test if an object is empty or not returns 0 or False
print()

class myclass():
  def __len__(self):
    return 0
  
myobj = myclass()
print(bool(myobj))  # Output: False

print()
# You can create functions that return a boolean value.
def my_function1():
  return True
print(my_function1())  # Output: True

# To print yes if the function returns True, you can use an if statement.

def my_function2():
  return True

if my_function2():
  print("Yes") # Output: Yes
else:
  print("No") 

print()

# To print no if the function returns False, you can use an if statement.
def my_function3():
  return False

if my_function3():
  print("Yes")
else:
  print("No") # Output: No
  
  
# using isinstance() function to check if an object is an instance of a class

y = 10
print(isinstance(y, int))  # Output: True, it is an integer
  