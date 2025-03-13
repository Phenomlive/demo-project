import os
import certifi
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from django.conf import settings

load_dotenv()

# Load MongoDB URI from environment variables (Best practice)
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

print(MONGO_URI, MONGO_DB_NAME)

# Establish connection
client = MongoClient(MONGO_URI, tlsCAFile=certifi.where(), server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. Successfully connected to MongoDB!")
except Exception as e:
    print(f"MongoDB Connection Error: {e}")

# Get database object
db = client[MONGO_DB_NAME]

# Function to return the DB instance
def get_db():
    return db
