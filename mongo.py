from pymongo import MongoClient
from config import config
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(config["MONGO"])
db = client["BankApi"]