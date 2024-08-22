from flask import Blueprint, request, jsonify
from mongo import db
from middleware import jwtMiddleware

general = Blueprint("general", __name__)

@general.get("/user/<username>")
@jwtMiddleware
def user(username, currentUser=None, *args, **kwargs):
   user = db.users.find_one({ "username": username })
   if not username:
      return jsonify({ "error": "Username was not provided" }), 404
   elif not user:
      return jsonify({ "error": "User was not found" }), 404
   else:
      return jsonify({ "user": user })
   
@general.get("/balance/<username>")
@jwtMiddleware
def balance(username, currentUser=None, *args, **kwargs):
   user = db.users.find_one({ "username": username })
   if not user:
      return jsonify({ "error": "User was not found" }), 404
   else:
      return jsonify({ "balance": user["balance"] })
   
@general.post("/sendmoney")
@jwtMiddleware
def send(currentUser=None):
   data = request.get_json()

   if "username" not in data:
     return jsonify({ "error": "Please specify the username"}), 500
   
   username = data["username"]

   if "amount" not in data:
     return jsonify({ "error": "Please fill an amount" }), 500
   
   amount = data["amount"]
   
   if amount <= 0:
       return jsonify({ "error": "You don't have anough money" }), 500
   
   user = db.users.find_one({ "username": username })
   if not user:
      return jsonify({ "error": "User was not found" }), 404
   else:
      db.users.update_one({ "_id": user._id }, { "$inc": { "balance": amount } })
      return jsonify({ "success": f"Successfully sent money to {username}" }), 200