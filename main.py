import os
from flask import Flask, request, jsonify
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
   data = request.get_json()
   # if not data or "username" not in data:
   #    return jsonify({ "error": "Userame is missing" }), 404
   # elif username in request.form:
   #    username = data["username"]
   db.users.insert_one(data)
   return jsonify({ "message": f"Your bank account is created with username {username}"})
    
if __name__ == "__main__":
  app.run(debug=True)