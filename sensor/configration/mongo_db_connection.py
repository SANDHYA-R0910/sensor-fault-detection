import pymongo
from sensor.constant.database import DATABASE_NAME
# from sensor.constant.env_variable import MONGODB_URL_KEY
import certifi
# import os
ca = certifi.where()

class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:

            if MongoDBClient.client is None:
                mongo_db_url = "mongodb+srv://sandhyarsanju:Govusandy0992@cluster0.urwewbm.mongodb.net/test?retryWrites=true&w=majority"
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e







# Alternate way to connect to Mongo

# from pymongo import MongoClient

# # Replace these values with your actual MongoDB connection string
# connection_string = "mongodb+srv://sandhyarsanju:Govusandy0992@cluster0.urwewbm.mongodb.net/test?retryWrites=true&w=majority"

# try:
#     # Connect to MongoDB
#     client = MongoClient(connection_string)

#     # Access a specific database
#     db = client.test

#     # Access a specific collection within the database
#     collection = db.my_collection

#     # Example query
#     result = collection.find_one()

#     print("Successfully connected to MongoDB")
# except Exception as e:
#     print("Error connecting to MongoDB:", e)
