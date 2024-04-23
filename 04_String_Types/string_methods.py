
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
# ? String Methods

#? The upper() method converts all characters in a string to uppercase.
str5 = "hello, world!"
print(str5.upper())

print()

#? The lower() method converts all characters in a string to lowercase.

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

#? String count method
"""
The count() method returns the number of times a specified value appears 
in a string.
"""
str11 = "I love fruits, I can eat fruits all day!"
print(str11.count("fruits")) # 2

str13 = "I love fruits, I can eat fruit all day!"
print(str13.count("fruits")) # 1

str12 = "I love fruits, I can eat fruit all day!"
count_string = str12.count('mangoes')
print(count_string)


# String index() method

string_index1 = "I love fruits, I can eat fruits all day!"
check_index1 = string_index1.index("day")
print(check_index1)

string_index2 = "Loving my life!"
check_index2 = string_index2.index("Loving")
print(check_index2)

string_index3 = "Loving my life!"
check_index3 = string_index3.index("v")
print(check_index3)


# The first occurrence of the specified value is returned.
string_index4 = "Loving my life!"
check_index4 = string_index4.index("i", 3, 6)
print(check_index4)