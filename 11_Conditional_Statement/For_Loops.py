
# For Loops
# A for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.
# Iterating over a sequence is called traversal.
# Syntax
# for val in sequence:
#     # code block
#     # code block
#     # code block
# The code block inside the for loop will be executed for each element in the sequence.

# USE CASE: Using a for loop to print numbers from 1 to 5
# Initialize the variable
amount_sales = 1

# Using a for loop to print numbers from 1 to 5
for amount_sales in range(1, 6):
    print(amount_sales)
    

sales = [100, 200, 300, 400, 500]
for x in sales:
    print(x)
    
    # The for loop will iterate over the list sales and print each element in the list.


# Looping through a string

# A for loop can iterate over a string and print each character in the string.

# Example 2: Using a for loop to print each character in a string

# Initialize the string

name = "Alice"

# Using a for loop to print each character in the string

for char in name:
    print(char)
    # Output: A, l, i, c, e

print()      
# The range() function

# The range() function is used to generate a sequence of numbers.

# Syntax
# range(start, stop, step)
# The range() function generates a sequence of numbers starting from the start value, up to the stop value, incrementing by the step value.

# Example 1: Using the range() function to generate a sequence of numbers

# Generate a sequence of numbers from 0 to 4

for i in range(5):
    print(i)
    # Output: 0, 1, 2, 3, 4

# A for loop can iterate over a sequence of numbers using the range() function.

print()
#? THE BREAK STATEMENT IN A FOR LOOP

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]

for city in cities:
    print(city)
    if city == "Chicago":
        break
    # The break statement will terminate the loop when the value of city is equal to "Chicago".
    # The output will be New York, Los Angeles, Chicago.

print()        
# Existing the loop before the value of city is equal to "Chicago" using the break statement.


cities2 = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
for x in cities2:
  if x == "Chicago":
    break
  print(x)
  
  # The break statement will terminate the loop when the value of x is equal to "Chicago".
  
  
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
if "Chicago" in cities:
    print("Chicago is in the list of cities.")
    # Output: Chicago is in the list of cities.    
    

# The 

cities = ["New York", "Chicago", "Houston", "Phoenix"] 
for city in cities:
    if city == "Chicago":
      continue
    print("City.")
        

# Range() function with start and stop values

for i in range(2, 5):
    print(i)
    # Output: 2, 3, 4
    
for i in range(2, 10, 2):
    print(i)
    # Output: 2, 4, 6, 8
    
# Else statement in a for loop

for i in range(5):
  
  print(i)
else:
  print("The for loop is executed successfully") 
  
print()


# Break a loop when x is 3, then the else part will be executed.

for i in range(5):
  if i == 3:
    break
  print(i) 
  
# Nested for loop

fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "pink"]

for x in fruits:
  
  for y in colors:
    print(x, y)  
    
                    