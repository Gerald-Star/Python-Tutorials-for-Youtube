"""
Assignment operators are used to assign values to variables. 
They can be used to perform various operations such as 
addition, subtraction, multiplication, division, etc., while assigning the result to a variable.
"""

# = : Assigns the value on the right to the variable on the left.
x = 10
y = 5

print(x)  # Output: 10


  
#? Addition assignment operator
# += : Adds the value on the right to the variable on the left
x += y  
x += 5
print(x)  # Output: 15 (10 + 5 = 15)
print("Result:", x)

#? Subtraction assignment operator
# -= : Subtracts the value on the right from the variable on the left
x -= y  
x -= 3
print(x)  # Output: 12 (15 - 3 = 12)
print("Result:", x)

#? Multiplication assignment operator
# *= : Multiplies the value on the right with the variable on the left
x *= y
x *= 2
print(x)  # Output: 24 (12 * 2 = 24)
print("Result:", x)
 
#? Division assignment operator
# /= : Divides the variable on the left by the value on the right

x /= y
x /= 5
print(x)  # Output: 4.8 (24 / 5 = 4.8)
print("Result:", x)   


#? Module assignment operator
# %= : Computes the modulus of the variable on the left with the value on the right.
x %= 2
print(x)  # Output: 0.8 (4.8 % 2 = 0.8)
print("Result:", x)


print()

# ? Floor division assignment operator
x // y
x //= 2
print(x)  # Output: 0.0 (0.8 // 2 = 0.0)
print("Result:", x)


# ? Exponentiation assignment operator 
# **= : Raises the variable on the left to the power of the value on the right.
x **= y
x **= 3  
print(x)  # Output: 0.0 (0.0 ** 3 = 0.0)
print("Result:", x) 


# ? Bitwise assignment operators
#  <<= Bitwise operators perform operations on binary representations of integers,
# Performs a bitwise left shift of the variable on the left by the value on the right.

x = 10
x <<= 2
print(x)  # Output: 40 (10 << 2 = 40)
print("Result:", x)

print()

# ? Bitwise right shift of the variable on the left by the value on the right.
  
# >>= : Performs a bitwise right shift of the variable on the left by the value on the right.
x = 5
x >>= 3
print(x)  # Output: 0 (5 >> 3 = 0)


# &= : Performs a bitwise AND operation between the variable on the left and the value on the right.
x &= 4
print(x)  # Output: 0 (1 & 4 = 0)


# |= : Performs a bitwise OR operation between the variable on the left and the value on the right.  
x |= 2
print(x)  # Output: 2 (0 | 2 = 2)
# means 0 | 2 = 2

# ^= : Performs a bitwise XOR operation between the variable on the left and the value on the right.
x ^= 1 
print(x)  # Output: 3 (2 ^ 1 = 3)

x ^= 2
print(x)  # Output: 1 (3 ^ 2 = 1)


# Feel free to modify this function and experiment with different assignment operator types!

