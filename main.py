import os
from flask import Flask, request, jsonify
from routes.auth import auth
from mongo import db

app = Flask(__name__)
app.register_blueprint(auth, url_prefix="/auth")

@app.get("/")
def root():
    return "<h1>This is the Bank api made with python</h1>"
   
@app.get("/balance/<id>")
def balance(id):
   user = db.users.find_one({ "_id": id })
   if not user:
      return jsonify({ "error": "User was not found" }), 404
   else:
      return jsonify({ "user": user })

if __name__ == "__main__":
  app.run(debug=True)
