import os
from pymongo import MongoClient

client = MongoClient()

from flask import Flask
app = Flask(__name__)

@app.get("/")
def route():
    return "<h1>This is the Bank api made with python </h1>"
    
@app.get("/test/:user")
def test():
    return f"<h2>{user}</h2>"