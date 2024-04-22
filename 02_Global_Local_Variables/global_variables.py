
#? Understand a function in Python
# A function is a block of code that performs a specific task.
# A function is a reusable piece of code that can be called multiple times.
# A function can take parameters and return values.


#? How to define a function in Python named 'greet'

# To define a function in Python, 
# use the 'def' keyword followed by the function name and parentheses().

#! def greet(arg):

  #? Function body here
  
  #! Call the function
#? great()

def greeting():
    print("Hello! Welcome to the Python world.")

# Calling the function
greeting()



#? What is a global variable?

# A variable declared outside a function is called a global variable.
# Global variables are accessible throughout the program.
# Global variables can be accessed and modified inside a function.
# Global variables have a global scope.
# Global variables can be accessed outside the function.
# Global variables can be accessed inside the function using the global keyword.
# Global variables can be modified inside the function using the global keyword.


#? Example 1: Access and Modify Global Variables
# To create a global variable, declare a variable outside the function.

global_var = 10

def my_function():
  # Access the global variable within a function
  print("Global variable value:", global_var) # Accessing global keyword variable

def another_function():
  # Modify the global variable within another function using the global keyword
  global global_var # global keyword
  global_var = 20

# Call the functions
my_function() # Output: Global variable value: 10
another_function() # Modify the global variable
my_function() # Output: Global variable value: 20

print()


#? Example 2: Access the global variable outside the function

# Global variable
global_var2 = 10

def my_function1():
    # Local variable
    local_var = 20
    print("Inside the function:")
    print("Local variable:", local_var)  # Accessing local variable
    print("Global variable:", global_var2)  # Accessing global variable

# Calling the function
my_function1() # Accessing local variable

# Accessing global variable outside the function
print("\nOutside the function:") # Accessing local variable
print("Global variable:", global_var2) # Accessing global variable


#? Example 3: Modify the global Keyword variable inside the function

# when you use the global keyword inside a function, the variable becomes global scope

# ? Example 3.1

def myFunc():
    global global_var3 # global variable
    global_var3 = 30
myFunc()
print(global_var3)    

print()


#? Example 3.2

def myFunc1():
    global global_var4 # global variable
    global_var4 = 'I am learning Python' # global variable
    
myFunc1()    
print('What am I learning:', global_var4)    


#? Example 4: Global variable inside a function

global_var5 = 50
global_var7 = 'easy'

def myFunc2():
  global global_var5 # global variable
  global global_var7 # global variable
  
  global_var5 = 100
  global_var6 = 200 # local variable and not global variable not declared as global
  global_var7 = 'not easy'

myFunc2()
print('Global variable:', global_var5)  
# print('Global variable:', global_var6) # NameError: name 'global_var6' is not defined
print('Learning Python is:', global_var7) 