##A class is used to create object, an ojbect has properties and methods( basically just functions)

#Create a class

class User:
    #Constructor ( A function that runs when you instantiate an object from a class )
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    #Methods within our class
    def greeting(self):
        hi = "Hy, my name is " + self.name + " and i am "+ str(self.age) + " yeaars old"
        return hi
    def has_Earth_Day(self):
        self.age +=1

        
##Extand class
class Customer(User):
    #Constructor 
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_Balance(self, balance):
        self.balance = balance

    def greeting(self):
        hi = "Hy, my name is " + self.name + " and i am "+ str(self.age) + " years old, and my balance is" + str(self.balance)
        return hi
# initialise user object

brad = User("Thembekile Mkhombo", "thembekile47@gmail.com", 22)

janet = Customer("Janet Johnson", "janet@gmail.com", 90)
janet.greeting()

janet.set_Balance(9000)

# Accessing properties

print(brad.has_Earth_Day())
print(brad.greeting())
print(janet.greeting())
