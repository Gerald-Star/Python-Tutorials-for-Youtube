

#? what is python variable?

# A variable is a container for storing data values.
# A variable is a name that refers to a value.
# A variable is a reference to a memory location.
# A variable is created when a value is assigned to it.
# A variable is destroyed when it goes out of scope.
# A variable can be reassigned to a new value.
# A variable can be of different types.

# ~ Path: Basic_Syntax/variable.py
# Path: Basic_Syntax/variable.py

#? Python Variable Naming Conventions
#! Variable names must start with a letter or an underscore
#! Variable names cannot start with a number
#! Variable names can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#! Variable names are case-sensitive (age, Age and AGE are three different variables)
#! Variable names should be descriptive and meaningful (name, age, salary)
#! Variable names should be in lowercase with words separated by underscores (first_name, last_name)
#! Variable names should not be a reserved keyword (class, def, if, else, while, for)
#! Variable names should not contain special characters (!, @, #, $, %, ^, &, *)
#! Variable names should not contain spaces

#? python uses assignment operator = to assign values to variables

# Declare and initialize variables
name = "John" #  creates a string
age = 25 # creates an integer 
is_student = True # creates a boolean variable
salary = 2500.50 # creates a floating point number


#? Declare variables without initialization

address = None # None is a special constant in Python 
#that represents the absence of a value
phone_number = "" # empty string

#? Declare multiple variables in a single line
x, y, z = 1, 2, 3 # x = 1, y = 2, z = 3

#? Declare variables with the same value
a = b = c = 10 # a = 10, b = 10, c = 10

#?  Declare variables with different types and print values
greeting = "Hello" # string
count = 5 # integer
pi = 3.14 # float

print('greeting')
print('count')
print('pi')

# Deleting variables
# You can delete a variable using the del keyword

friend = "Ole"
print(friend) # Output: John

#del friend
#print(friend)

#? Print the type of a variable

print(type(greeting)) # Output: <class 'str'>
print(type(count)) # Output: <class 'int'>
print(type(pi)) # Output: <class 'float'>

#? Casting Python Variables

x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0

print('x =', x)
print('y =', y)
print('z =', z)

#? Case Sensitive Variables
#! Variable names are case-sensitive - Age and age are different variables

age = 25
Age = 50
print('age =', age)
print('Age =', Age)

# Variable Combination
# You can combine variables using the + operator
# The + operator is used to concatenate strings and add numbers
# The + operator can be used to combine two or more variables

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print('full_name =', full_name)

# Example 2
a = 10
b = 20
c = a + b
print(c)
print('c =', c)
print('c =', c, 'USD')


# ? Invalid Variable Names
# Variable names cannot start with a number
# Variable names cannot contain special characters
# Invalid Variable Names
# Variable names cannot start with a number
# Variable names cannot contain special characters

#! Example of invalid variable names
#! 1name = "John"  # Invalid: starts with a number
#! $price = 10.99  # Invalid: contains a special character $
#! my-variable = 5  # Invalid: contains a special character -
#! class = "Math"  # Invalid: reserved keyword used as a variable name
