# A tuple is a collection which is ordered and unchangeable. Allows duplicate members

#Create Tuple

fruits = (["Apples", 'Grapes', "Oranges"], ["Beetroot", "Cabbage", "Onion"])

print(fruits[1][0])
# A set is a collection which is unordered and unindexed, no duplicate members

# create a set

veggies = {"Beetroot", "Cabbage", "Onion"}

#Check if is in set

#print("Apples" in veggies)

#Add to set

#veggies.add("Brocolli")

#Remove from set
#veggies.remove("Onion")

#print(veggies)

#Clear set
veggies.clear()


#print("Here is a quick loop through our set")

for veg in veggies:
    print(veg+":  "+veggies)
