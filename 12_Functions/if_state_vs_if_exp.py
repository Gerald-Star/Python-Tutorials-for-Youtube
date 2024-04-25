

# The difference between an if statement and an if expression is that an if statement is a block of code that is executed if a condition is true, while an if expression is a single line of code that returns a value based on a condition. If expressions are more concise and can be used in places where a statement is not allowed, such as inside a list comprehension or a lambda function.

# In the example above, the if statement in the greet_user_6 function is replaced with an if expression, which makes the code more concise and easier to read. Similarly, the if statement in the greet_user_9 function is replaced with an if expression, which also improves the readability of the code.

# Overall, if expressions are a useful feature in Python that can help make your code more concise and readable. They are especially useful in situations where you need to return a value based on a condition, such as in the examples above.

# In the example above, the if statement in the greet_user_6 function is replaced with an if expression, which makes the code more concise and easier to read. Similarly, the if statement in the greet_user_9 function is replaced with an if expression, which also improves the readability of the code.


#? Example of if statement

def greet_user_5(name):
  return f"My name is, {name}!"

def greet_user_6(name):
  #message = greet_user_5(name)
  #return message
  
  return greet_user_5(name) # replace with expression

print(greet_user_6("Bob"))  # Output: Hello, Bob!


#? Example of If statement in a function
def myCar(car):
  if car == "Toyota":
    return "I drive a Toyota"
  else:
    return "I drive a Honda"
  
print(myCar("Toyota"))  # Output: I drive a Toyota

#? Example of if expression

def myCar_name(car_name):
  return "I drive a Kia" if car_name == "Kia" else "I drive a Honda"

print(myCar_name("Kia"))  # Output: I drive a Kia

# Note: The if expression is more concise and easier to read than the if statement. 
# It can be used in situations where you need to return a value based on a condition, such as in the examples above.


# If expression in a list

def even_numbers(numbers):
  return [num for num in numbers if num % 2 == 0]

print(even_numbers([1, 2, 3, 4, 5, 6]))  # Output: [2, 4, 6]


def odd_numbers(numbers):
  return [num for num in numbers if num % 2 != 0]

print(odd_numbers([1, 2, 3, 4, 5, 6]))  # Output: [1, 3, 5]

print()

def grocery_lists(items):
  return [item for item in items if item in ["apple", "banana", "orange"]]

print(grocery_lists(["apple", "banana", "orange", "grapes"])) 
# Output: ['apple', 'banana', 'orange']


# use if statement for the grocery_lists function

def grocery_fruits(items):
  grocery_fruits = []
  for item in items:
    if item in ["apple", "banana", "orange"]:
      grocery_fruits.append(item)
  return grocery_fruits

print(grocery_fruits(["apple", "banana", "orange", "grapes"]))

print()

andrew = "Andrew"

print([letter for letter in andrew if letter in "aeiou"])

# Output: ['A', 'e', 'o']

print()

def vowels(word):
  return [letter for letter in word if letter in "aeiou"]


print(vowels("Andrew"))  # Output: ['A', 'e', 'o']



# If expression in a lambda function

add = lambda x, y: x + y if x > 0 and y > 0 else "Invalid input"

print(add(2, 3))  # Output: 5

print(add(-2, 3))  # Output: Invalid input

# Note: The if expression in the lambda function is more concise and easier to read than using an if statement.



