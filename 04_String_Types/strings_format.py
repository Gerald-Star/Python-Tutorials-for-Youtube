
#? F-Strings
# You cannot format a string with a number and a string using the + operator.
# !year = 1992
# !format_string = "The answer is: " + year
# !print(format_string) # TypeError: can only concatenate str (not "int") to str


# F-strings are string literals that have an f at the beginning 
# and curly braces {} containing expressions that will be replaced with their values.

# f-strings are incredibly versatile and make string formatting in Python more readable and intuitive. 
# They're widely used in Python 3.6 and later versions.

# ? Example 1
year = 1992
format_string = f"The answer is: {year}"
print(format_string) # The answer is: 1992

print()

price = 100
quantity = 5
total = price * quantity
print(f"The total price is: {total}")

print()

# ? Example 2
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Alice and I am 30 years old.

#? Expressions inside f-strings
x = 10
y = 20
print(f"The sum of {x} and {y} is {x + y}.")
# Output: The sum of 10 and 20 is 30.


#? Formatting numbers inside f-strings
radius = 5
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area}.")
# Output: The area of a circle with radius 5 is 78.5.

pi = 3.14159
print(f"Value of pi: {pi:.2f}")
# Output: Value of pi: 3.14


# ? Using f-strings with dictionaries
person = {'name': 'Bob', 'age': 25}
print(f"Name: {person['name']}, Age: {person['age']}")
# Output: Name: Bob, Age: 25

print()
# ? Using f-strings with functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
# Output: Hello, Alice!

print()

# ? Using f-strings with conditional statements
num = 10
print(f"The number {num} is {'even' if num % 2 == 0 else 'odd'}.")
# Output: The number 10 is even.

print()

#? Using f-strings with loops
numbers = [1, 2, 3, 4, 5]
result = ""
for num in numbers:
    result += f"{num} "
print(result)

print()

# Using f-strings with math operations
number_strings1 = ["1", "2", "3", "4", "5"]
total = 0
for num in number_strings1:
    total += int(num)
print(f"The sum of {', '.join(number_strings1)} is {total}.")

print()

number_strings2 = f"The price is {20 * 10} dollars."
print(number_strings2)

number_strings3 = f"The price is {20 * 10:.2f} dollars."
print(number_strings3)

print()

student1 = "My name is {fname}, I 'm {age} years old".format(fname = "Alice", age = 25)
print(student1)

print()
student2 = "My name is {0}, I 'm {1} years old".format("Alice", 25)
print(student2)

print()
student3 = "My name is {}, I 'm {} years old".format("Alice", 25)
print(student3)