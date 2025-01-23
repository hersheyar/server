import os
import pymongo
import certifi
from dotenv import load_dotenv

load_dotenv()

# TODO: make sure to run  $env:MONGODB_PASS="Password here" each session
# TODO: run this to view it echo $env:MONGODB_PASS

mongo_password = os.getenv("MONGODB_PASS")
# mongo db connection string
con_string = f"mongodb+srv://hersheyar:{mongo_password}@cluster0.6eigk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(con_string, tlsCAFile = certifi.where())
# TODO: Add db name in the ""
products_db = client.get_database("ProductsData")
coupons_db = client.get_database("CouponsData")