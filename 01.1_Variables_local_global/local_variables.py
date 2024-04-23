
#?What is a local variable?

# A variable declared inside a function is called a local variable.
# Local variables are accessible only inside the function in which they are declared.
# Local variables are created when the function is called and destroyed when the function exits.
# Local variables are not accessible outside the function.
# Local variables have a local scope.
# Local variables can have the same name in different functions because they are not in the same scope.

#? Example: Local Variables

def calculate_sum(a, b):
  # Define a local variable 'result'
  result = a + b
  print("The sum is:", result)

# Call the function and pass two numbers
calculate_sum(5, 10)

#! Accessing the local variable 'result' outside the function will raise an error
#! print(result) # NameError: name 'result' is not defined

# Example 2: Local Variables
def sum(x, y):
  sum = x + y
  return sum
  print(sum(5, 2))
  
  
  