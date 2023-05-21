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
    
    def get_data_list(self, collection, type = None):
        target_col = self.db[collection]
        try:
            cursor = target_col.find({'type': type})
            result = list(cursor)
        except:
            cursor = target_col.find()
            result = list(cursor)
        return result 

    def get_data_list2(self, collection, index):
        target_col = self.db[collection]
        try:
            cursor = target_col.find({'index': index})
            result = list(cursor)
        except:
            cursor = target_col.find()
            result = list(cursor)
        return result 
    
    def get_data_id(self, collection, ID):
        try:
            target_col = self.db[collection]
            data = target_col.find_one({"ID": ID})
            return data
        except Exception as e:
            print("Error :", str(e))
            return -1

    def get_data_index(self, collection, index):
        try:
            target_col = self.db[collection]
            data = target_col.find_one({"index": index})
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

    def get_data_nick_name(self, collection, nn):
        try:
            target_col = self.db[collection]
            data = target_col.find_one({"nick_name": nn})
            return data
        except:
            return None
        
    def update_data(self, collection, id, key, data):
        try:
            print("target :", key)
            target_col = self.db[collection]
            target_col.update_one({"_id" : id}, {"$set" : { key : data }})
        except Exception as e:
            print("Error :", str(e))
            return 
        
    def get_data_name(self, collection, name):
        try:
            target_col = self.db[collection]
            data = target_col.find_one({"name": name})
            return data
        except:
            return -1
        
    def update_join_data(self, collection, id, key, data):
        try:
            print("target :", key)
            target_col = self.db[collection]
            target_col.update_one({"_id" : id}, {"$set" : { key : data }})
        except Exception as e:
            print("Error :", str(e))
            return 

    def get_size_col(self, collection):
        count = 0
        try:
            target_col = self.db[collection]
            count = target_col.count_documents({})
        except:
            count = -1
        return count
    
    def delete_data(self, collection, key, value):
        try:
            target_col = self.db[collection]
            filter = {key : value}
            target_col.delete_one(filter)
        except Exception as e:
            print("Error :", str(e))
            return 
        

"""
def main():
    db = Databass()
    id = ObjectId('645bc392a0db139e5c1669ae')
    data = db.get_data('user_data', id)
    pprint.pprint(data)




if __name__ == "__main__":
    main()

"""