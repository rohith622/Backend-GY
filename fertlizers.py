from flask import Flask, jsonify, request

app = Flask(__name__)


fertilizers = [
    {"id": 1, "name": "Urea", "quantity": 50, "price": 700},
    {"id": 2, "name": "DAP", "quantity": 30, "price": 1200}
]


@app.route('/fertilizers', methods=['GET'])
def get_fertilizers():
    return jsonify(fertilizers)


@app.route('/fertilizers', methods=['POST'])
def add_fertilizer():
    new_fertilizer = request.get_json()
    fertilizers.append(new_fertilizer)
    return jsonify({"message": "Fertilizer added successfully!", "data": new_fertilizer}), 201


@app.route('/fertilizers/<int:id>', methods=['PUT'])
def update_fertilizer(id):
    for fert in fertilizers:
        if fert["id"] == id:
            fert.update(request.get_json())
            return jsonify({"message": "Fertilizer updated successfully!", "data": fert})
    return jsonify({"message": "Fertilizer not found"}), 404


@app.route('/fertilizers/<int:id>', methods=['DELETE'])
def delete_fertilizer(id):
    for fert in fertilizers:
        if fert["id"] == id:
            fertilizers.remove(fert)
            return jsonify({"message": "Fertilizer deleted successfully!"})
    return jsonify({"message": "Fertilizer not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
