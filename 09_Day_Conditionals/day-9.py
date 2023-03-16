a = 3
if a > 0:
    print('A is a positive number')

# If Else
# syntax
"""
if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions
"""
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

"""py
# syntax
if condition:
    code
elif condition:
    code
else:
    code
"""
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

# Nested Conditions

"""
# syntax
if condition:
    code
    if condition:
    code
"""
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

# If Condition and Logical Operators
"""
# syntax
if condition and condition:
    code
"""

a = 0
if a > 0 and a % 2 == 0:
    print('A is an even and positive integer')
elif a > 0 and a % 2 != 0:
    print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

# If and Or Logical Operators
# syntax
"""
if condition or condition:
    code
"""
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access granted!')
else:
    print('Access denied!')
