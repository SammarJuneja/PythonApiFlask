import os
from flask import Flask, request
from pymongo import MongoClient
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

MONGO = os.getenv("MONGO_URI")
client = MongoClient(MONGO)
db = client["BankApi"]

@app.get("/")
def root():
    return "<h1>This is the Bank api made with python </h1>"
    
@app.post("/create-user")
def createUser():
   data = request.json
   db.insert_one(data)
    
if __name__ == "__main__":
  app.run(debug=True)