import os
from dotenv import load_dotenv

load_dotenv()

MONGO = os.getenv("MONGO_URI")
JWT_SECRET = os.getenv("SECRET_KEY")

config = {
    "MONGO": MONGO,
    "JWT_SECRET": JWT_SECRET
}