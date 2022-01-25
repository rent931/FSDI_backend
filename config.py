import pymongo

mongo_url = "mongodb+srv://school:zGd63HnlmPEjMfBT@cluster0.zeswa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongo_url)

db = client.get_database("Renteria")