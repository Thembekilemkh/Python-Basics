# A function is a block of code which only runs when it is called. In python, we do not use curly braces we use indentation tabs or spaces


# Create a function


def sayHello( name ):
    print( "Hello "+ name )

name = "Thembekile Mkhombo"
sayHello( name )

# Return value

x = 9
y = 8

def getPum( num1, num2 ):
    total = num1 + num2
    num1 = num2 * 2
    return total



print( getPum( x, y ) )


# A lambda function is a small anonymous function. ( same as arrow functions )
# This is a function and its return value is stored in the get sum variable

getSum = lambda num1, num2 :  num1 + num2

print( getSum( 6, 6 ) )


