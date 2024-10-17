from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json

# see example_secrets.json for reference
with open("secrets.json","r") as file:
    data = json.loads(file.read())

username = (data)["mongoUsername"]
password = (data)["mongoPassword"]

uri = f"mongodb+srv://{username}:{password}@programatically.dbj2v.mongodb.net/?retryWrites=true&w=majority&appName=Programatically"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)