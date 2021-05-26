# String in pyhton are surrounded by either single or double quotes, Here a look atsome string methods and string methods

name = " Thembekile"
age = 21

## concatnate
print("Hello, my name is " + name + " and i and" +str(age)) #any other variable would have to be casted to a string

"""
A better way to use variables in strings

"""
f = 111
#String Formatting

#Arguments by position
#print('My name is {name} and I am {age} years old' .format(name = name, age =age))

#F-Strings (only available in python 3.6+)
#print(f'Hello my name is {name} and i am {age} years old')

#StringMethods

s = 'Hello world'

#Capitalize
print(s.capitalize())

# Here are someother methods

#Make all upper case
s.upper()

#Mkae all lower case
s.lower()

#Swap case
s.swapcase()

#Getslength but not only for string for basically every variable
len(s) # Can be used for any datatype

#Replace word
s.replace("world", 4) #replaces world from the string with everyone

#Count
sub = 'h'
s.count(sub) #Counts the number of H's in the string

#Starts with
s.startswith("hello")  #Returns a true or false bool

#Ends with
s.endswith("d") #same as above

#Split into a list
s.split() #Its gonna take our string and turn it into an array

#Find position
s.find('r')

#is all alphanumeric
s.isalnum()

#is all alphabetic
s.isalpha

#is all numeric
s.isnumeric()
