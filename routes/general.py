from flask import Blueprint, request, jsonify
from mongo import db
from pymongo.errors import OperationFailure
from config import config

general = Blueprint("general", __name__)

@general.get("/user/<id>")
def user(id):
   user = db.users.find_one({ "_id": ObjectId(id) })
   if not id:
      return jsonify({ "error": "Id was not provided" }), 404
   elif not user:
      return jsonify({ "error": "User was not found" }), 404
   else:
      return jsonify({ "user": user })
   
@general.get("/balance/<id>")
def balance(id):
   user = db.users.find_one({ "_id": ObjectId(id) })
   if not user:
      return jsonify({ "error": "User was not found" }), 404
   else:
      return jsonify({ "user": user })