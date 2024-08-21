from functools import wraps
from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)