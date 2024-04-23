
#?  what is python escape characters
"""
Escape characters are characters that are generally used to perform 
certain tasks and their usage in code directs the compiler to take a suitable
action mapped to that character.
"""

#? Types of Escape characters in Python
"""
Escape characters in Python include:
- \n: Newline
- \t: Tab
- \": Double quote
- \': Single quote
- \\: Backslash
- \r: Carriage return
- \b: Backspace
- \f: Form feed
- \v: Vertical tab
"""

# Example 1: Newline
print("Hello\nworld!")
# Output:
# Hello
# world!

# Example 2: Insert a tab newline character between two words
print("Hello\tworld!")
# Output: Hello    world!

# Example 3: Double quote
print("This is a backslash: \\")
# Output: This is a backslash: \
  
# Example 4: Single quote  
print('It\'s a beautiful day.')
# Output: It's a beautiful day.
  

# Example 5: Double quote
print("She said, \"Hello!\"")
# Output: She said, "Hello!"

print()

escape_string = "We are learning \"Python\" programming."
print(escape_string)

print()

# Raw Strings (r"..."): Treats backslashes as 
# literal characters and doesn't escape them.
print(r"Newline: \n Tab: \t")
# Output: Newline: \n Tab: \t
