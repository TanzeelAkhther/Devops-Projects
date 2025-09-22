from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

USER_SERVICE = "http://user_service:5001"
ORDER_SERVICE = "http://order_service:5002"

@app.route('/users', methods=['POST'])
def create_user():
    resp = requests.post(f"{USER_SERVICE}/users", json=request.json)
    return jsonify(resp.json()), resp.status_code

@app.route('/orders', methods=['POST'])
def create_order():
    resp = requests.post(f"{ORDER_SERVICE}/orders", json=request.json)
    return jsonify(resp.json()), resp.status_code

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    resp = requests.get(f"{USER_SERVICE}/users/{user_id}")
    return jsonify(resp.json()), resp.status_code

@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    resp = requests.get(f"{ORDER_SERVICE}/orders/{order_id}")
    return jsonify(resp.json()), resp.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

