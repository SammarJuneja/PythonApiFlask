import os
from flask import Flask
from pymongo import MongoClient, errors
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

MONGO = os.getenv("MONGO_URI")
client = MongoClient(MONGO)
db = client.get_database()

@app.get("/")
def route():
    return "<h1>This is the Bank api made with python </h1>"
    
@app.get("/test/<user>")
def test(user):
    return f"<h2>{user}</h2>"
    
if __name__ == "__main__":
  app.run(debug=True)