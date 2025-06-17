from pymongo import MongoClient

# Use your actual connection string here
uri = "mongodb+srv://padmavathi:c0NlD8R64FP3aZrp@cluster0.rg1orey.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

try:
    # Print database names
    print("Connected successfully! Databases:")
    print(client.list_database_names())
except Exception as e:
    print("Connection failed:", e)
