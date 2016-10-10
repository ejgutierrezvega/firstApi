from pymongo import MongoClient
from pymongo import errors
from bson import json_util
from customexception import myexception
import logging

class MongoRepository:

    #create repository client.
    def __init__(self, db, collection):
        self.dbname = db
        self.collectionname = collection

    def InsertItem(self, item):
        db = self.getmongodb()
        collection = db.get_collection(self.collectionname)
        result = collection.insert_one(item)
        return result.inserted_id

    def FindCollectionById(self, id):
        db = self.getmongodb()
        collection = db.get_collection(self.collectionname)
        cursor = collection.find({"restaurant_id": id})
        for document in cursor:
            return document
    
    def mongoclient(self):
        client = MongoClient("mongodb://localhost:27017")
        try:        
            client.is_mongos()
        except errors.ConnectionFailure, e:
            raise myexception.MyException("Custom exception: Could not connect to server: %s" % e, 'ERR-REPO-001')
        except errors.ServerSelectionTimeoutError, e:
            raise myexception.MyException("Custom exception: Could not connect to server: %s" % e, 'ERR-REPO-001')
        except:
            raise myexception.MyException("Custom exception: Could not connect to server", 'ERR-REPO-001')
        return client
        
    def getmongodb(self):
        client = self.mongoclient()
        return client[self.dbname]