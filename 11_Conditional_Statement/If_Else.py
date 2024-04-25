
# What is Conditional Statement in Python?

# In Python, a conditional statement is a statement that controls the flow of execution depending on some condition.

num = 5

if num > 0:
    print("The number is positive")
    
    # Output: The number is positive
    
# Example 2: If...else statement

# In this example, we use the if...else statement to check if a number is positive or negative.

num1 = 10
num2 = 5

if num1 > num2:
  print("num1 is greater than num2")


print()
num = -5

if num > 0:
  print("The number is positive")
else:
  print("The number is negative")
  
  # Output: The number is negative


print()  
# Example 3: If...elif...else statement

# In this example, we use the if...elif...else statement to check if a number is positive, negative, or zero.

num = 0

if num > 0:
  print("The number is positive")
elif num == 0:
  print("The number is zero")
else:
  print("The number is negative")
  
  # Output: The number is zero
  
  
num3 = 0
num4 = 5

if num3 > num4:
  print("num3 is greater than num4")
elif num3 == num4:
  print("num3 is equal to num4")
else:
  print("num3 is less than num4")
  
  # Output: num3 is less than num4
  
num5 = 10
num6 = 10

if num5 > num6:
  print("num5 is greater than num6")  
  
elif num5 != num6:
  print("num5 is not equal to num6")
  
else:
  print("num5 is equal to num6")
  
  # Output: num5 is equal to num6
  
  
  
print()  
# Nested if statement

# You can use an if...elif...else statement inside another if...elif...else statement. This is called a nested if statement.

# Example 4: Nested if statement

# In this example, we use a nested if statement to check if a number is positive, negative, or zero.

num = 0

if num >= 0:
  
  if num == 0:
    print("The number is zero")
  else:
    print("The number is positive")
    
else:
  print("The number is negative")
  
  # Output: The number is zero

print()
  
# Short Hand If

# If you have only one statement to execute, you can put it on the same line as the if statement.

# Example 5: Short Hand If

# In this example, we use the short hand if statement to check if a number is positive or negative.

num = 5

if num > 0: print("The number is positive")

# Output: The number is positive


print()

# Short Hand If...else

# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line.

# Example 6: Short Hand If...else

# In this example, we use the short hand if...else statement to check if a number is positive or negative.

num = 5

print("The number is positive") if num > 0 else print("The number is negative")

# Output: The number is positive


print()


# And

# The and keyword is a logical operator, and is used to combine conditional statements.

# Example 7: And

# In this example, we use the and keyword to combine two conditional statements.

num = 5

if num > 0 and num % 2 == 0:
  
  print("The number is positive and even")
  
else:
  
  print("The number is either negative or odd")
  
  #Output: The number is either negative or odd
  
  
print()

# Example: If a is greater than b, AND if c is greater than a, then print "Both conditions are True".

a = 300
b = 200
c = 700  

if a > b and c > a:
  print("Both conditions are True")
  
  # Output: Both conditions are True
  
  
print()

a = 100
b = 200
c = 700

if a > b != c > a:  
  print("Both conditions are True")
  
else:
    print("Both conditions are False")
    
    # Output: Both conditions are False
  
  
print() 
 
#? Or

# The or keyword is a logical operator, and is used to combine conditional statements.

num = 5

if num > 0 or num % 2 == 0:
  
  print("The number is either positive or even")
  
else:
  
  print("The number is negative and odd")
  
  # Output: The number is either positive or even
  
  
a = 300
b = 200
c = 700

if a > b or c > a:
  print("At least one of the conditions is True")
  
  # Output: At least one of the conditions is True
  
print()    
  
#? Not

# The not keyword is a logical operator, and is used to reverse the logical state of a conditional statement.

# Example 8: Not

# In this example, we use the not keyword to reverse the logical state of a conditional statement.


amount1 = 100
amount2 = 200

if not amount1 > amount2: 
  print("amount1 is greater than amount2")
  # Output: amount1 is greater than amount2
  
print()  

num = 5

if not num > 0:
  
  print("The number is negative")
  
else:
  print("The number is positive")
  
  # Output: The number is positive



  
