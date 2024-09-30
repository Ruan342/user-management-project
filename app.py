from flask import Flask, jsonify, request
from mongodb import get_users, get_user_by_id, create_user, update_user, delete_user

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def users_list():
    users = get_users()
    return jsonify(users), 200

@app.route('/users/<id>', methods=['GET'])
def user_detail(id):
    user = get_user_by_id(id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "Usuário não encontrado"}), 404

@app.route('/users', methods=['POST'])
def create():
    data = request.json
    result = create_user(data)
    return jsonify(result), 201

@app.route('/users/<id>', methods=['PUT'])
def update(id):
    data = request.json
    result = update_user(id, data)
    return jsonify(result), 200

@app.route('/users/<id>', methods=['DELETE'])
def delete(id):
    result = delete_user(id)
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True)
