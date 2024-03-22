# install mongo cloud library
# pip install pymongo dnspython


from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime

uri = "mongodb+srv://user01:hpNLZngFLRbp8pBA@cluster0.9vqvhed.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# print("DatabaseName >> ", client.list_database_names())

# Send a ping to confirm a successful connection
# try:
#    client.admin.command('ping')
#    print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#    print(e)

db = client["myflexflowDB"]
# print("connectionName >> ", db.list_collection_names())

dbcollection = db.myflexflowCollection


todo1 = {"name": "partrick02", "text": "my second todo", "status": "open", "tags": [
    {"tag_name": "python", "category": "coding"}, {"tag_name": "MongoDB", "category": "database"}], "date": datetime.datetime.now()}

result = dbcollection.insert_one(todo1)

todo2 = [{"name": "partrick03", "text": "my second todo", "status": "open", "tags": [
    {"tag_name": "python", "category": "coding"}, {"tag_name": "MongoDB", "category": "database"}], "date": datetime.datetime.now()},
    {"name": "partrick04", "text": "my second todo", "status": "open", "tags": [
             {"tag_name": "python", "category": "coding"}, {"tag_name": "MongoDB", "category": "database"}], "date": datetime.datetime.now()},
    {"name": "partrick05", "text": "my second todo", "status": "open", "tags": [
             {"tag_name": "python", "category": "coding"}, {"tag_name": "MongoDB", "category": "database"}], "date": datetime.datetime.now()}]

result = dbcollection.insert_many(todo2)

# search result
result = dbcollection.find_one({'name': 'partrick03'})
print("search result >> ", result)

print("search by name and text > ", dbcollection.find_one(
    {'name': 'partrick03', "text": "my second todo"}))

print("search by tags > ", dbcollection.find_one(
    {'tags': 'python'}))


print("Search by ObjectID > ", dbcollection.find_one(
    {"_id": ObjectId("65fd44c488795b0a54cbd9cd")}))
