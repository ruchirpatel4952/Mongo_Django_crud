import pymongo
ConnectionString = "mongodb+srv://ruchir:RucHIR%40007@cluster0.zwyzu.mongodb.net/test"
#how to connect
if __name__ == '__main__':
    # client = pymongo.MongoClient('mongodb://localhost:27017/')
    client = pymongo.MongoClient(ConnectionString)
    db = client['test-database']
    # collection = db['test-collection']
    # print(collection)
    posts = db.posts
    post_id = posts.insert_one({"p":1}).inserted_id
    print(post_id)


