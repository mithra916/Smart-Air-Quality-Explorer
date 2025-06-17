import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://padmavathi:c0NlD8R64FP3aZrp@cluster0.rg1orey.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["air_quality"]
collection = db["sensor"]

# Load data into a pandas DataFrame
data = list(collection.find())
df = pd.DataFrame(data)

# Print summary or do analysis
print(df.head())
print("\nAverage AQI:", df["AQI Value"].mean())

# Filter example: show only 'Unhealthy' countries
unhealthy = df[df["Status"] == "Unhealthy"]
print("\nUnhealthy Countries:\n", unhealthy[["Country", "AQI Value"]])
