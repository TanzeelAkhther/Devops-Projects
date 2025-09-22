from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated in-memory DB
users = {}

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = str(len(users) + 1)
    users[user_id] = data
    return jsonify({"id": user_id, "user": data}), 201

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({"id": user_id, "user": user})
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
