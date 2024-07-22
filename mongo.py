from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO = os.getenv("MONGO_URI")
client = MongoClient(MONGO)
db = client["BankApi"]
