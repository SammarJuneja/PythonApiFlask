from flask import Blueprint, request, jsonify
from mongo import db
from pymongo.errors import OperationFailure
from config import config

general = Blueprint("general", __name__)

@general.get("/user/<id>")
def user(id):
   user = db.users.find_one({ "_id": id })
   if not id:
      return jsonify({ "error": "Id was not provided" }), 404
   elif not user:
      return jsonify({ "error": "User was not found" }), 404
   else:
      return jsonify({ "user": user })
   
@general.get("/balance/<id>")
def balance(id):
   user = db.users.find_one({ "_id": id })
   if not user:
      return jsonify({ "error": "User was not found" }), 404
   else:
<<<<<<< HEAD
      return jsonify({ "balance": user["balance"] })
   
@general.post("/sendmoney")
def send():
   data = request.get_json()

   username = data["id"]

   if username not in data:
     return jsonify({ "error": "Please specify the username"}), 500
   
   amount = data["amount"]

   if amount not in data:
     return jsonify({ "error": "Please fill an amount" }), 500
   elif amount <= 0:
       return jsonify({ "error": "You don't have anough money" }), 500
   
   user = db.users.find_one({ "username": username })
   if not user:
      return jsonify({ "error": "User was not found" }), 404
   else:
      db.users.update_one(
         {
            "_id": user._id
         }, {
            "$inc": {
              " balance": amount
            }
            }
      )
      return jsonify({ "success": f"Successfully sent money to {username}" }), 200
=======
      return jsonify({ "user": user })
>>>>>>> 826670b65e97c548a5cff3e965c5914ad7370258
