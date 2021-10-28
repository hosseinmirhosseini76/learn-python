# ! Python Arithmetic Operators
a = 10
b = 20
# print(a + b)  # Addition
# print(a - b)  # Subtraction
# print(a * b)  # Multiplication
# print(a / b)  # Division
# print(a % b)  # Modulus
# print(a ** b)  # Exponent
# print(9 // 2)  # Floor Division

# ! Python Comparison Operators
# print(a == b)
# print(a != b)
# # print(a <> b) # Python version 3.9 does not support <>, use != instead
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)

# ! Python Assignment Operators
'''
=
+= Add AND
-= Subtract AND
*= Multiply AND
/= Divide AND
%= Modulus AND
**= Exponent AND
//= Floor Division
'''

# ! Python Bitwise Operators
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

# c = a & b  # 12 = 0000 1100
# print("Line 1 - Value of c is ", c)

# c = a | b  # 61 = 0011 1101
# print("Line 2 - Value of c is ", c)

# c = a ^ b  # 49 = 0011 0001
# print("Line 3 - Value of c is ", c)

# c = ~a  # -61 = 1100 0011
# print("Line 4 - Value of c is ", c)

# c = a << 2  # 240 = 1111 0000
# print("Line 5 - Value of c is ", c)

# c = a >> 2  # 15 = 0000 1111
# print("Line 6 - Value of c is ", c)

# ! Python Logical Operators
# (a and b)
# (a or b)
# not(a and b)

# ! Python Membership Operators
a = 10
b = 20
list = [1, 2, 3, 4, 5];

if (a in list):
    print("Line 1 - a is available in the given list")
else:
    print("Line 1 - a is not available in the given list")

if (b not in list):
    print("Line 2 - b is not available in the given list")
else:
    print("Line 2 - b is available in the given list")

a = 2
if (a in list):
    print("Line 3 - a is available in the given list")
else:
    print("Line 3 - a is not available in the given list")

# ! Python Identity Operators
# * Identity operators compare the memory locations of two objects.
a = 20
b = 20

if (a is b):
    print("Line 1 - a and b have same identity")
else:
    print("Line 1 - a and b do not have same identity")

if (id(a) == id(b)):
    print("Line 2 - a and b have same identity")
else:
    print("Line 2 - a and b do not have same identity")

b = 30
if (a is b):
    print("Line 3 - a and b have same identity")
else:
    print("Line 3 - a and b do not have same identity")

if (a is not b):
    print("Line 4 - a and b do not have same identity")
else:
    print("Line 4 - a and b have same identity")


