# A for loop is used for iteratiing over a sequence ( that is either a list, a tuple, a dictionary, a set or a string ).

# A simple forloop that loops over list

people = [ "Sindi", "Musa", "Vusi" ]

for person in people :
    print( "Current Person: " + person)

#Breakout of a loop

for person in people :
    if person == "Musa":
        break
    print( "Current Person: " + person)

#Continue a loop ( worksas a skip button )

for person in people :
    if person == "Musa":
        continue
    print( "Current Person: " + person)


people2 = ["Martha", "Straw", "Sedi", "Lelo"]
#Range

for i in range(len(people2)):
    print(people2[i])

##CUSTOM RANGES

for i in range(0, 11):
    print(" Numbers: " + str(i))


##whie loops
v = 0
while( v < 10):
    print(" Numbers (while): " + str(v))
    v =  v + 1
