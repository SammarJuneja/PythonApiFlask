from flask import Flask, jsonify
from routes.auth import auth
from routes.general import general
from mongo import db

app = Flask(__name__)
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(general, url_prefix="/general")

@app.get("/")
def root():
    return "<h1>This is the Bank api made with python</h1>"

if __name__ == "__main__":
  app.run(debug=True)
