from pymongo import MongoClient
from bson import json_util

#create repository client.
client = MongoClient("mongodb://localhost:27017")

#select db to work with.
dbname = 'test'
#one way to open a DB. 
#db = client.test
db = client[dbname]

collectionname = 'restaurants'
dbrestaurants = db[collectionname]


def insertToRestaurants(item):
    result = dbrestaurants.insert_one(item)
    print(result.inserted_id)

def queryRestaurantByRestaurantId(id):
    cursor = db.restaurants.find({"restaurant_id": id})
    print type(cursor)
    for document in cursor:
        return document
        