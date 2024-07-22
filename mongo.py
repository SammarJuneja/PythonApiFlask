from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO = os.getenv("MONGO_URI")
JWT_SECRET = os.getenv("SECRET_KEY")
client = MongoClient(MONGO)
db = client["BankApi"]
