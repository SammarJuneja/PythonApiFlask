import os
import re
from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.errors import OperationFailure
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

MONGO = os.getenv("MONGO_URI")
client = MongoClient(MONGO)
db = client["BankApi"]

@app.get("/")
def root():
    return "<h1>This is the Bank api made with python</h1>"
    
@app.post("/create-user")
def createUser():
   data = request.get_json()

   emailRegex = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$')
   passwordRegex = re.compile(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
   
   if not data:
     return jsonify({ "error": "No data was provided" })
     
     username = data["username"]

   if "username" not in data:
      return jsonify({ "error": "Userame is missing" }), 404
      
      email = data["email"]
      
   if "email" not in data:
      return jsonify({ "error": "Email is missing" }), 404
      
   if not emailRegex.match(email):
      return jsonify({ "error": "Please enter a valid email" })
      
      password = data["password"]
      
   if "password" not in data:
      return jsonify({ "error": "Password is missing" }), 404
   
   if not passwordRegex.match(password):
      return jsonify({ "error": "Password must atleast be 8 characters long and should contain One uppercase ltter and a symbol" })
      
   try:
     db.users.insert_one({
       "username": username,
       "email": email,
       "password": password
     })
     return jsonify({ "message": f"Your bank account is created with username {username}"})
     
   except OperationFailure as e:
     return jsonify({ "message": f"Failed to create account {e}"})
    
if __name__ == "__main__":
  app.run(debug=True)
