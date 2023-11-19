from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (in-memory)
data = [
    {"id": 1, "name": "Product A", "price": 10.99},
    {"id": 2, "name": "Product B", "price": 19.99}
]

# GET request to retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(data)

# POST request to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    new_product = request.get_json()
    data.append(new_product)
    return jsonify(new_product), 201

if __name__ == '__main__':
    app.run()
