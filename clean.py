import pandas as pd
from pymongo import MongoClient

# STEP 1: Load the dataset
df = pd.read_csv("data_date.csv")  # Use your actual file name

# STEP 2: Clean the data
df.columns = df.columns.str.strip()  # Remove extra spaces in column names
df["AQI Value"] = pd.to_numeric(df["AQI Value"], errors="coerce")
df["AQI Value"].fillna(df["AQI Value"].mean(), inplace=True)
df["Country"] = df["Country"].str.strip()
df["Status"] = df["Status"].str.strip()
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# STEP 3: Save cleaned file
df.to_csv("cleaned_air_quality.csv", index=False)

# STEP 4: Upload to MongoDB Atlas
client = MongoClient("mongodb+srv://padmavathi:c0NlD8R64FP3aZrp@cluster0.rg1orey.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  
db = client["air_quality"]
collection = db["sensor"]

data = df.to_dict(orient="records")
collection.insert_many(data)

print("✅ Cleaned data inserted into MongoDB successfully!")
