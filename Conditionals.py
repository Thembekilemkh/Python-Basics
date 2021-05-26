# If / else conditionals are used to decide to do something based on whether something is true or false

x = 10
y = 10

## Comparison operators ( ==, !=, >, <, >=, <= ), used to compare values


#Create a simple if statement
if x > y:
    print( str(x) + " is greater than " + str(y))

#create a simple if/else statement

if x < y:
    print( str(x) + " is greater than " + str(y))
else:
    print( " y is not greater than x " )

#Create a else if statement using the elif key word

if x < y:
    print( str(x) + " is greater than " + str(y))
elif x == y:
    print( "x and y are eqaul" )
else:
    print( " y is not greater than x " )

##NESTED IF STATEMENTS

if x > 2:
    if x <= 10:
        print( "x is greater than 2 and less than or equal to 10" )

#Logical operators ( and, or, not ) are literally typed out like so ...

if x > 2 and x < 10 or x == 10:
    print( "x is greater than 2 and less than or equal to 10, again" )

# Membership operators ( in, not, not in ) - used to test if a sequence is presented in an object

numbers = [ 1, 2, 3, 4, 5 ]

#IN
if 3 in numbers:
    print( "Good man" )

#NOT IN
if 6 not in numbers:
    print( "Good man" )
