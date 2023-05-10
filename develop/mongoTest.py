from pymongo import MongoClient
import datetime
import pprint
from bson.objectid import ObjectId

def main():

    client = MongoClient("mongodb+srv://alsrhks2508:rlaalsrhks2508@mymongodbcluster1.960mxpd.mongodb.net/?retryWrites=true&w=majority")

    db = client['testDB']
    print(db)

    # collection 접근 -> posts 라는 콜랙션에 접근
    posts = db.posts

    #post_id = posts.insert_one(post).inserted_id


    pprint.pprint(posts.find_one({"_id" : ObjectId('642ee2adbe776cb67dd387ad') }))
    #pprint.pprint(posts.find_one({"author" : "Kim"}))

    #for post in posts.find({"author":"Lee"}):
       #pprint.pprint(post)




if __name__ == "__main__":
    main()