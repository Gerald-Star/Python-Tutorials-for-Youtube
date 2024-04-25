
#? While Loops
# A while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition.
# The while loop can be terminated when a certain condition is met.

# Syntax

# while condition:
#     # code block
#     # code block
#     # code block

# The code block inside the while loop will be executed as long as the condition is True.

# Example 1: Using a while loop to print numbers from 1 to 5

# Initialize the variable

amount_sales = 1

# Using a while loop to print numbers from 1 to 5

while amount_sales <= 5:
  print(amount_sales)
  amount_sales += 1
  
print()  

# Break Statement in While Loop

# The break statement is used to exit a loop when a certain condition is met.

# Example 2: Using a while loop with a break statement  

i = 1

while i <= 10:
  print(i)
  if i == 4:
    break
  i += 1
  
print()

i = 1
while i <= 10:
  print(i)
  i += 1
  if i == 4:
    break

  # The break statement will terminate the loop when i is equal to 4.
  # The output will be 1, 2, 3, 4.
  
  
print()  

#? The continue statement is used to skip the rest of the code inside a loop for the current iteration only.
# The loop does not terminate but continues with the next iteration.

# Example 3: Using a while loop with a continue statement

i = 0

while i < 5:
  i += 1
  if i == 3:
    continue
  print(i)
    
print()

# The else statement is used to execute a block of code when the condition of the while loop is False.

# Example 4: Using a while loop with an else statement

i = 1

while i <= 5:
  print(i)
  i += 1
else:
  print("The while loop is executed successfully")    

print()  

i = 1

while i < 7:
  print(i)
  i += 2
else:
  print("The while loop is executed successfully")  