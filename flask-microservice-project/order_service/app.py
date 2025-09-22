from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated in-memory DB
orders = {}

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    order_id = str(len(orders) + 1)
    orders[order_id] = data
    return jsonify({"id": order_id, "order": data}), 201

@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    order = orders.get(order_id)
    if order:
        return jsonify({"id": order_id, "order": order})
    return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

