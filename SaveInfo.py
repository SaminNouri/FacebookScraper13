from pymongo import *

class SaveInfo:



    def saveToDataBase(self,users,cluster,database,collection):
        print(users[0])
        self.client=MongoClient(cluster)
        self.database=self.client[database]
        self.collection=self.database[collection]
        self.collection.insert_many(users)


