from flask import Blueprint, request, jsonify
from mongo import db
from middleware import jwtMiddleware
from datetime import datetime, timedelta
import random

money = Blueprint("money", __name__)

@money.post("/work")
@jwtMiddleware
def earn(username, currentUser=None, userId=None, *args, **kwargs):
    user = db.users.find_one({ "username": username })
    cooldowns = {}
    currentTime = datetime.now()
    cooldownTime = cooldowns.get(str(user["_id"]))

    if cooldownTime is None or currentTime >= cooldownTime:
        cooldowns[str(user["_id"])] = currentTime + timedelta(hours=24)
        reward = random.randint(100, 300)
        db.users.updateOne({})
        print(f"You earned ${reward}"), 200
    else:
        remainingTime = cooldownTime - currentTime
        print(f"You can work in {remainingTime} again"), 429
        
    