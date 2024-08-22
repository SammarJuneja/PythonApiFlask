from functools import wraps
from flask import Flask, request, jsonify
import jwt
from config import config

app = Flask(__name__)

def jwtMiddleware(f):
    @wraps(f)
    def main(*args, **kwargs):
        token = None
        if ("Authorization") in request.headers:
            token = request.headers["Authorization"]

        if not token:
            return jsonify({ "error": "Token is missing" }), 401
        
        try:
            data = jwt.decode(token, config["JWT_SECRET"], algorithms=["HS256"])
            currentUser = data["username"]
        except:
            return jsonify({ "error": "Token is invalid" })
        
        return f(currentUser, *args, **kwargs)
    
    return main