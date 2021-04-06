'''
 This is a multiline comment
'''

"""
VARIABLES RULES:
    - Variables are case sensitive ( Always watch your cases)
    - Must start with a letter or a underscore
    - Can have numbers but must not start with one
"""

x = 1               # no semi colon required & no declaration required
y = 2.5             # float
name = "Thembekile" # String
is_cool = True      # Boolen



## Multiple assignment

a, b, surname, is_hot = (1, 3.8, 'Mkhombo', False) # Has to be put in paranthesis

## Basic Math
z = b + y

##Checking Variable types
print(type(is_hot))
print('i am', is_hot, "and i am ", z," years old")

#Casting (Changing a variable type from one data type to another)

b = bool(b)

print(type(b))
print(b)
