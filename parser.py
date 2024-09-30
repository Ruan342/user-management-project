import json
import pymongo
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["user_database"]
collection = db["users"]

def parse_user_data(data):
    roles = []
    if data.get("is_user_admin"):
        roles.append("admin")
    if data.get("is_user_manager"):
        roles.append("manager")
    if data.get("is_user_tester"):
        roles.append("tester")
    user = {
        "username": data["user"],
        "password": data["password"],
        "roles": roles,
        "preferences": {"timezone": data["user_timezone"]},
        "active": data["is_user_active"],
        "created_ts": datetime.strptime(data["created_at"], "%Y-%m-%dT%H:%M:%SZ").timestamp()
    }
    return user

with open('udata.json') as f:
    data = json.load(f)

for user_data in data["users"]:
    user = parse_user_data(user_data)
    collection.insert_one(user)

print("Dados inseridos no MongoDB.")
