from pymongo import MongoClient
from config import config

client = MongoClient(config["MONGO"])
db = client["BankApi"]