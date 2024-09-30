import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["user_database"]
collection = db["users"]

def get_users():
    users = list(collection.find({}))
    for user in users:
        user['_id'] = str(user['_id'])
    return users

def get_user_by_id(user_id):
    user = collection.find_one({'_id': ObjectId(user_id)})
    if user:
        user['_id'] = str(user['_id'])
        return user
    return None

def create_user(data):
    new_user = {
        "username": data["username"],
        "password": data["password"],
        "roles": data["roles"],
        "preferences": {"timezone": data["preferences"]["timezone"]},
        "active": data.get("active", True),
        "created_ts": data["created_ts"]
    }
    result = collection.insert_one(new_user)
    return {"inserted_id": str(result.inserted_id)}

def update_user(user_id, data):
    update_data = {"$set": data}
    collection.update_one({"_id": ObjectId(user_id)}, update_data)
    return {"message": "Usuário atualizado"}

def delete_user(user_id):
    collection.delete_one({"_id": ObjectId(user_id)})
    return {"message": "Usuário deletado"}
