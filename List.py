#A list is a collection which is ordered and changable. Allows duplicate members(basically likean array)

#Create a list

numbers = [1, 2, 3, 4, 5]
fruits = ["oranges", "Grapes", "Pears", "apples"]

#OR you can use a contstructor

numbers2 = list((1, 2, 3, 4, 5, 6))

#Get the value
# REMEMBER LISTS ARE ZERO(0) BASED

print(fruits[1])

#get length

print(len(fruits))

#Append to list
fruits.append("manges")


#Remove from list
fruits.remove("Grapes")

#insert into position
fruits.insert(2, "strawberries")

#remove from certain positions
fruits.pop(2)

#Reverse list
fruits.reverse()

#Sort list
fruits.sort()

#Reverse Sort
fruits.sort(reverse = True)

#Change a value
fruits[0]= 'BlueBerries'

print(fruits)
