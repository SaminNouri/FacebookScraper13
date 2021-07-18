from pymongo import *

class SaveInfo:



    def saveToDataBase(self,users,cluster,database,collection):

        self.client=MongoClient(cluster)
        self.database=self.client[database]
        self.collection=self.database[collection]
        self.collection.insert_many(users)


