#import os
from pymongo import MongoClient
import config from config
from dotenv import load_dotenv

load_dotenv()

#MONGO = os.getenv("MONGO_URI")
client = MongoClient(config.MONGO)
db = client["BankApi"]
