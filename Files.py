## Python has functions for creating, reading, updating and deleting files
# Open a file ( Or writing to a file )

myFile = open("MyFile.txt", 'w')

## Get info from file

print("Name", myFile.name)
print("is_closed", myFile.closed)
print("Opening_mode", myFile.mode)

# write to file

myFile.write("I love python")
myFile.write(" Javascripth")

myFile.close()

##Append to file

myFile = open("myFile.txt", "a")

myFile.write(" i Also like PHP")

myFile.close()


## Read from file

myFile = open("myFile.txt", "r")

text = myFile.read(100)

print(text)
