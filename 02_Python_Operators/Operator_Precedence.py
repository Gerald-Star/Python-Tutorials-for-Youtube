
# What is operator precedence in Python?
"""
  Operator precedence determines the grouping of terms in an expression.
  This affects how an expression is evaluated.
  Certain operators have higher precedence than others; for example, 
  the multiplication operator has higher precedence than the addition operator.
  
  For example, x = 5 + 2 * 3 will be evaluated as x = 5 + (2*3) = 11, not x = (5+2)*3 = 21.
  Here is a precedence table for Python operators:
  
  Operator	Description
  ()	Parentheses
  **	Exponent
  +x, -x, ~x	Unary plus, Unary minus, Bitwise NOT
  *, /, //, %	Multiplication, Division, Floor division, Modulus
  +, -	Addition, Subtraction
  <<, >>	Bitwise shift operators
  &	Bitwise AND
  ^	Bitwise XOR
  |	Bitwise OR
  in, not in, is, is not, <, <=, >, >=, !=, ==	Comparisons, Identity, Membership operators
  not	Logical NOT
  and	Logical AND
  or	Logical OR
  =, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, <<=, >>=	Assignment operators
  Note: Operators in the same box have the same precedence.
"""

# Example code for operator precedence
# Example 1: Operator precedence

x = 5 + 2 * 3
print(x)  # Output: 11 (5 + 6)
# means 5 + (2*3) = 11

# Example 2: Operator precedence
x = 5 + 2 * 3 ** 2
print(x)  # Output: 23 (5 + 2*9)
# means 5 + (2*(3**2)) = 23

# Example 3: Operator precedence
x = (5 + 2) * 3
print(x)  # Output: 21 ((5+2)*3)
# means (5+2)*3 = 21

# Example 4: Operator precedence
x = 5 + 2 * 3 // 2
print(x)  # Output: 8 (5 + 3)
# means 5 + (2*3//2) = 8

# Example 5: Operator precedence

x = 5 + 2 * 3 // 2 ** 2
print(x)  # Output: 6 (5 + 2)
# means 5 + (2*3//2**2) = 6

# Example 6: Operator precedence
x = 5 + 2 * 3 // 2 ** 2 - 1
print(x)  # Output: 5 (5 + 1)
# means 5 + (2*3//2**2) - 1 = 5

# Example 7: Operator precedence with == and !=
x = 5 == 5 != 6
print(x)  # Output: True
# means 5 == 5 and 5 != 6 = True

print()

# Example 8: Operator precedence with comparison operators
# == and !=

x = 5 == 4 != 6
print(x)  # Output: False
# means 5 == 4 and 4 != 6 = False



# Example 8: Operator precedence with in and not in
z = 5 in [1, 2, 3, 4, 5]
print(z)  # Output: True


# Example 9: Operator precedence with not in
z = 5 not in [1, 2, 3, 4, 5]
print(z)  # Output: False