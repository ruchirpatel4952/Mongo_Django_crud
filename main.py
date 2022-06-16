import pymongo
ConnectionString = "mongodb+srv://ruchir:RucHIR%40007@cluster0.zwyzu.mongodb.net/test"
#how to connect
# if __name__ == '__main__':
#     # client = pymongo.MongoClient('mongodb://localhost:27017/')
#     client = pymongo.MongoClient(ConnectionString)
#     db = client['test-database']
#     # collection = db['test-collection']
#     # print(collection)
#     posts = db.posts
#     post_id = posts.insert_one({"p":1}).inserted_id
#     print(post_id)

#insert document
def insertDocument():
    studentInfo = {
        "name": "Drake",
        "section": 2,
        "maths_marks": 35,
        "sst_marks": 79
    }
    student_id = collections.insert_one(studentInfo).inserted_id
    print(f"Student with id {student_id} has been created")

def readDocument():
    myStudents = collections.find({"percentage":99.99})
    print(myStudents)
    for student in myStudents:
        print(student)

def updateDocuments():
    collections.update_one({"section": 1}, {'$inc': {'section': 100}})
    collections.update_many({}, {'$inc': {'section': 100}})


def deleteDocuments():
    r = collections.delete_one({"section": 101})
    print(r.deleted_count)
    r = collections.delete_many({})
    print(r.deleted_count)
    collections.update_many({})


# create a db for school
if __name__ == '__main__':
    # creating connection
    client = pymongo.MongoClient(ConnectionString)
    db = client['unacademy']
    collections = db.class_1
    # insertDocument()
    readDocument()



