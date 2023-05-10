from pymongo import MongoClient
import datetime
import pprint
from bson.objectid import ObjectId

class Databass():
    def __init__(self):
        self.uri = "mongodb+srv://alsrhks2508:rlaalsrhks2508@mymongodbcluster1.960mxpd.mongodb.net/?retryWrites=true&w=majority"
        self.client = MongoClient(self.uri)
        self.db = self.client['the_teamPlay']
        print(self.db)
        self._login = False

    def input_data(self, collection, dct):
        target_col = self.db[collection]
        dct["date"] = datetime.datetime.utcnow()
        dct_id = target_col.insert_one(dct).inserted_id
        print('input data in db(id) : ', dct_id)
        return
    
    def get_data_id(self, collection, ID):
        try:
            target_col = self.db[collection]
            data = target_col.find_one({"ID": ID})
            return data
        except:
            return -1

    def get_data(self, collection, id):
        try:
            target_col = self.db[collection]
            data = target_col.find_one({"_id": id})
            return data
        except:
            return None

"""
def main():
    db = Databass()
    id = ObjectId('645bc392a0db139e5c1669ae')
    data = db.get_data('user_data', id)
    pprint.pprint(data)




if __name__ == "__main__":
    main()

"""