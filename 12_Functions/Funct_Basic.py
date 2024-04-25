
#? The def keyword is used to define a function in Python

#? The return statement is used to exit a function and return a value.

# ? Function Parameters
# You can pass data, known as arguments, into a function.
# A parameter is a variable that is used to define a function.

# ? Function Arguments
# An argument is a value that is passed into a function when it is called.
# Arguments are specified inside the parentheses when calling a function.
# You can add as many arguments as you want, just separate them with a comma.



#? Example 1: Creating a function
# Create a function named greet_user that prints a greeting message.
# Call the function to execute the code block inside the function.
# Define a function named greet_user
def greet_user():
  print("Hello, welcome to Python Functions!")
  
greet_user()  # Calling a function


#? Example 1: Passing a parameter and argument into a function

# Create a function named greet_user that takes a parameter named name.
# Call the function with the argument "Alice".

def greet_user_1(name):
  print(f"Hello, {name}!")

greet_user_1("Alice")


#? Another Example

def myPlanet(planet):
  print(f"My favourite planet is {planet}")
  
myPlanet("Mars")  # Output: My favourite planet is Mars



#? Example 2: Passing multiple arguments into a function
# Using the format() method to insert the arguments into the string.

def myFunction(fname, lname):
  #print(fname + " " + lname)
  print(f"{fname} {lname}")
  
myFunction("Alice", "Bob")  # Output: Alice Bob


print()

#? Example 3: Passing a list as an argument into a function

def myMeal_Plan(food):
  for x in food:
    print(x)
    
fruits = ["apple", "banana", "cherry"]
myMeal_Plan(fruits)  # Output: apple, banana, cherry


#? Example 4: Passing a dictionary as an argument into a function

def myMeal_Plan_2(food):
  
  for x in food:
    print(x)
    
fruit_plan = { "name": "apple", "color": "red" }
myMeal_Plan_2(fruit_plan)  # Output: name, color



#? Different ways to call a function

# You can call a function multiple times.
# Call a function multiple times with different arguments.

def st_names(name):
  print(f"Hello, {name}!")
  
st_names("Oge")  # Output: Hello, Alice!

st_names("Bob")  # Output: Hello, Bob!

st_names("Charlie")  # Output: Hello, Charlie!

print()

#? You can call a function inside another function.

# Example 1

def greet_user_3(name):
  return f"Hello, {name}!"

def greet_user_4(name):
  return greet_user_3(name)

print(greet_user_4("Alice"))  # Output: Hello, Alice!

print()

#? Example 2

def greet_user_5(name):
  return f"My name is, {name}!"

def greet_user_6(name):
  #message = greet_user_5(name)
  #return message
  
  return greet_user_5(name) # replace with expression

print(greet_user_6("Bob"))  # Output: Hello, Bob!


# You can call a function inside a loop.

def greet_user_7(name):
  return f"Hello, {name}!"

students = ["Alice", "Bob", "Charlie"]

for student in students:
  print(greet_user_7(student))  # Output: Hello, Alice! Hello, Bob! Hello, Charlie!
  
print()  
  
# You can call a function inside a conditional statement.

def greet_user_8(greeting):
  return f"Hello, {greeting}!"

def greet_user_9(greeting):
  
  #if name == "Alice":
    #return greet_user_8(greeting)
  #else:
    #return "Hello, Stranger!"
# replace with if expression

  return greet_user_8(greeting) if greeting == "friend" else "Hello, Stranger!"   
print(greet_user_9("friend"))  # Output: Hello, friend!
 

print()
#? Default Arguments

# You can specify a default value for an argument when defining a function.
# If the function is called without an argument, the default value will be used.
# The default value is specified after the parameter name, separated by an equal sign.
# You can have multiple default arguments, but they must be specified after non-default arguments.

def greet_user_2(name="Elena"):
  print(f"Hello, {name}!")
  
greet_user_2()  # Calling a function without an argument

print()

#? Arguments

# You can pass a list as an argument into a function.

def myFunction1(food):
  for x in food:
    print(x)
    
fruits = ["apple", "banana", "cherry"]
myFunction1(fruits)  # Output: apple, banana, cherry

# You can pass a dictionary as an argument into a function.
# You can pass a tuple as an argument into a function.
# You can pass a set as an argument into a function.

# Syntax

def myFunction2(city1, city2):
  #print(fname + " " + lname)
  print(f"{city1}  {city2}") # Output: calling function with two arguments / expression
  
myFunction2("Austria", "England")  # Output: calling function with two arguments





