

# Arbitrary Arguments, *args
"""
If you do not know how many arguments will be passed into your function,
add a * before the parameter name in the function definition.
This way, the function will receive a tuple of arguments, and you can access 
the items accordingly.

  
"""


def myStudent_names(*kids):
  # print("The eldest child is " + kids[2])
  print(f"The youngest child is {kids[2]}")


myStudent_names("Alice", "Bob", "Charlie")
# Output: The youngest child is Charlie

print()

# ? Keyword Arguments

"""
You can also send arguments with the key = value syntax.
This way the order of the arguments does not matter.

"""


def myPupils_names(child3, child2, child1):
  print("The youngest child is " + child3)


myPupils_names(child1="Alice", child2="Bob", child3="Charlie")

# Use f'string to format the output


def myPupils_names_(child3, child2, child1):
  print(f"The youngest child is {child3}")


myPupils_names_(child1="Alice", child2="Bob", child3="Charlie")


#? Arbitrary Keyword Arguments, **kwargs

"""
If you do not know how many keyword arguments that will be passed into your function,
add two asterisk: ** before the parameter name in the function definition.
This way, the function will receive a dictionary of arguments, and you can access the items accordingly.

"""
# * Use the **kwargs parameter to pass a dictionary as an argument into a function.


def myFunction3(**cat):
  print("His pet name is " + cat["pet_name"])


myFunction3(fname="Tobias", pet_name="Oso")


#? Use **kwargs to pass a list as an argument into a function.
"""

def myFunction4(**cat):
  print("His pet names are " + cat["pet_names"])
  
myFunction4(fname = "Tobias", pet_names = ["Oso", "Tino"])
"""

#! Can only concatenate str (not "list") to str



#? Default Parameter Value

"""
If we call the function without argument, it uses the default value:

"""

def myFavorite_food(food = "pizza"):
  print(f"My favorite food is {food}")
  
myFavorite_food("sushi")  # Output: My favorite food is sushi
myFavorite_food()  # Output: My favorite food is pizza
myFavorite_food("pasta")  # Output: My favorite food is pasta
myFavorite_food("burger")  # Output: My favorite food is burger

# means that if you do not provide an argument, it will use the default value.

print()
# Return Values in Functions

"""
To let a function return a value, use the return statement:

"""

def myFunction5(x):
  return 2 * x
print(myFunction5(3))  # Output: 15
print(myFunction5(5))  # Output: 25
print(myFunction5(9))  # Output: 45

  
# Pass Statement in Functions

"""
The pass statement is a null statement that does nothing when executed.
You use the pass statement to write empty functions to avoid getting an error.

""" 

def myFunction6():
  pass

 
