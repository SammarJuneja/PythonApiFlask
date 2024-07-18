import os
import re
from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from pymongo.errors import OperationFailure
import bcrypt
import jwt
import datetime
from dotenv import load_dotenv

auth = Blueprint("auth", __name__)
load_dotenv()

MONGO = os.getenv("MONGO_URI")
JWT_SECRET = os.getenv("SECRET_KEY")
client = MongoClient(MONGO)
db = client["BankApi"]

@auth.post("/create-account")
def createAccount():
   data = request.get_json()

   emailRegex = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$')
   passwordRegex = re.compile(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
   
   if not data:
     return jsonify({ "error": "No data was provided" })
     
   username = data["username"]

   if "username" not in data:
      return jsonify({ "error": "Userame is missing" }), 404
      
   email = data["email"]

   emailExist = db.users.find_one({ "email": email })

   if emailExist:
      return jsonify({ "error": "User with provided email already exists" }), 500
      
   if "email" not in data:
      return jsonify({ "error": "Email is missing" }), 404
      
   if not emailRegex.match(email):
      return jsonify({ "error": "Please enter a valid email" })
      
   password = data["password"]
      
   if "password" not in data:
      return jsonify({ "error": "Password is missing" }), 404
   
   if not passwordRegex.match(password):
      return jsonify({ "error": "Password must atleast be 8 characters long and should contain One uppercase ltter and a symbol" })
   
   byte = password.encode("utf-8")
   salt = bcrypt.gensalt()
   hashedPass = bcrypt.hashpw(byte, salt)
      
   try:
     db.users.insert_one({
       "username": username,
       "email": email,
       "password": hashedPass
     })
     return jsonify({ "message": f"Your bank account is created with username {username}"}), 200
   except OperationFailure as e:
     return jsonify({ "message": f"Failed to create account {e}"})

@auth.post("/login")
def login():
   data = request.get_json()
   passwordRegex = re.compile(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
   
   if not data:
     return jsonify({ "error": "No data was provided" })
   
   username = data["username"]

   if "username" not in data:
      return jsonify({ "error": "Userame is missing" }), 404
   
   password = data["password"]
      
   if "password" not in data:
      return jsonify({ "error": "Password is missing" }), 404
   
   if not passwordRegex.match(password):
      return jsonify({ "error": "Password must atleast be 8 characters long and should contain One uppercase ltter and a symbol" })
   
   userExist = db.users.find_one({ "username": username })
   print(userExist)
   passw = userExist["password"]

   if not userExist:
      return jsonify({ "error": "User not found" }), 404
   
   byte = password.encode("utf-8")
   decodedPass = bcrypt.checkpw(byte, password)

   if not decodedPass:
      return jsonify({ "error": "You entered wrong password" })
   
   token = jwt.encode({
      "username": username
   }, JWT_SECRET, algorithm="HS256")
   return jsonify({ "token": token, "success": "You login successfully" })