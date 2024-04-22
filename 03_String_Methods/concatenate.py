
#? String Concatenation
"""
# To concatenate, or combine, two strings you can use the + operator.
# Example
# Merge variable a with variable b into variable c:
"""

a = "Long"
b = " walk to freedom"
c = a + b
print(c)

print()

#? String Concatenation examples
# You can also concatenate strings with other data types, such as numbers.
# Example:
d = "The answer is: "
e = 42
f = d + str(e)
print(f)

print()
# You can also use the += operator to concatenate strings.
# Example:
g = "Bigger"
h = "World"
g += h
print(g)

#? Using the + operator
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe


print()
#? Using the str.join() method
"""
# The join() method takes all items in an iterable and joins 
# them into one string.
"""
words = ["Hello", "world", "!"]
sentence = " ".join(words)
print(sentence)  # Output: Hello world !

print()
#? Using f-strings
"""
# f-strings are string literals that have an f at the beginning 
# and curly braces containing expressions that will be replaced with their values.
"""

first_name = "Merry"
last_name = "Making"
full_name = f"{first_name} {last_name}"
print(full_name)  # Output: John Doe

print()
#? Using the .format() method
"""
The .format() method formats the specified values 
and inserts them inside the string's placeholder.
"""

first_name = "John"
last_name = "Doe"
full_name = "{} {}".format(first_name, last_name)
print(full_name)  # Output: John Doe

print()
#? Using string concatenation within a loop

"""
A loop is a sequence of instructions that is continually 
repeated until a certain condition is reached.
"""
numbers = [1, 2, 3, 4, 5]
result = ""
for num in numbers:
    result += str(num)
print(result)  # Output: 12345
