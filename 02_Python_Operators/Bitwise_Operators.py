
# Bitwise operators are used to compare (binary) numbers:
# & : Bitwise AND
# | : Bitwise OR
# ^ : Bitwise XOR
# ~ : Bitwise NOT
# << : Bitwise left shift
# >> : Bitwise right shift

# Example code for bitwise operators

#? Bitwise & AND operator
# Returns 1 if both bits are 1, otherwise 0
x = 10  # Binary: 1010
y = 4   # Binary: 0100
print(x & y)  # Output: 0 (0000)

#? Example code for bitwise OR operator
# Returns 1 if one of the bits is 1, otherwise 0

#? Example code for bitwise OR operator
x = 5 # Binary: 0101
y = 3 # Binary: 0011
print(x | y)  # Output: 7 (0111)
# means 0101 | 0011 = 0111


x = 10  # Binary: 1010
y = 2   # Binary: 0010
print(x | y)  # Output: 10 (1010)
# means 1010 | 0010 = 1010


#? Example code for bitwise XOR operator
# Returns 1 if one of the bits is 1, but not both
x = 10  # Binary: 1010
y = 4   # Binary: 0100
print(x ^ y)  # Output: 14 (1110)
# means 1010 ^ 0100 = 1110

#? Example code for bitwise NOT operator
# Inverts all the bits
x = 10  # Binary: 1010
print(~x)  # Output: -11 (-(1011))


#? Example code for bitwise left shift operator
# Shifts the bits to the left by a certain number of positions
x = 10  # Binary: 1010
print(x << 2)  # Output: 40 (101000)


#? Example code for bitwise right shift operator
# Shifts the bits to the right by a certain number of positions
x = 10  # Binary: 1010
print(x >> 1)  # Output: 5 (0101)