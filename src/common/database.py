import os

import pymongo



class Database(object):
    URI = "mongodb+srv://yuqian:mm13679097617@microblog.mhgtu.mongodb.net/test?authSource=admin&replicaSet=atlas-d1z9s7-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client["microblog"]

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection, query):
        return Database.DATABASE[collection].remove(query)
