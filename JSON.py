## JSON is commonly used with data API, here is how we parce JSON into a python dictinary
import requests
import json

#Create some sample JSON ( So we have some JSN to work with)
my_friend_id = 1 

result =  requests.get( "https://vasity-movers.firebaseio.com/" + str(my_friend_id) + ".json" )
## Parse this to a dictinary

user = json.loads( result.content.decode() )

print(user)
