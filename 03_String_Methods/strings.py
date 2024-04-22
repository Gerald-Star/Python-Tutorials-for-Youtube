


#? Creating Strings literals with the print() function

print("Hello, World!") # Single quotes
print('Hello, World!') # Double quotes
print("""Hello, World!""") # Triple quotes
print('''Hello, World!''') # Triple quotes

print()

# Multiple lines string
preach1 = """The greatest glory in living lies not 
in never falling, but in rising every time we fall."""
print(preach1)

print()

preach2 = '''The greatest glory in living lies not 
in never falling, but in rising every time we fall.'''
print(preach2)

print()
#? Strings can be concatenated using the + operator.
str1 = "Hello, " + "World!"
print(str1)

print()
#? Strings can be repeated using the * operator.
str2 = "Counting, " * 3
print(str2)

print()
#? Strings can be formatted using the format() method.
str3 = "Counting, {}".format("Numbers!")
print(str3)

#? Strings can be compared using the comparison operators.
print("Hello" == "Hello") # True

print('Many' == 'Customers') # False

print('Hello' == 'hello') # False

print('Hello' != 'hello') # True

print('Hello' < 'hello') # True

print('Hello' > 'hello') # False

print(10 == 10) # True

print(10 != 10) # False

print(10 < 5) # False

#? Strings have many built-in methods for manipulation.
str5 = "Hello, World!"
print(str5.upper())

print()

str6 = "Many, Students!"
print(str6.lower())

print()

str7 = "Better, World!"
print(str7.split())

print()

str8 = "Be, Fair!"
print(str8.strip())

#? Creating Strings literals with the str() function
str9 = str(10)
print(str9)

str10 = str(3.14)
print(str10)
