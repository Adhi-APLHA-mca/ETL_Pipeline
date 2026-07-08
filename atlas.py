from pymongo import MongoClient
uri = "mongodb+srv://adhityanmudlayar27_db_user:sbBkZBURscRUjl3O@cluster0.fyilg95.mongodb.net/?appName=Cluster0"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)