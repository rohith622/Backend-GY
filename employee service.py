from flask import Flask, jsonify, request

app = Flask(__name__)


employees = [
    {"id": 1, "name": "Rohith", "position": "Developer", "salary": 50000},
    {"id": 2, "name": "Pavan", "position": "Tester", "salary": 40000}
]


@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)


@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    emp = next((e for e in employees if e["id"] == id), None)
    return jsonify(emp) if emp else jsonify({"message": "Employee not found"}), 404


@app.route('/employees', methods=['POST'])
def add_employee():
    new_emp = request.get_json()
    employees.append(new_emp)
    return jsonify({"message": "Employee added successfully", "employee": new_emp}), 201


@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    emp = next((e for e in employees if e["id"] == id), None)
    if emp:
        data = request.get_json()
        emp.update(data)
        return jsonify({"message": "Employee updated successfully", "employee": emp})
    else:
        return jsonify({"message": "Employee not found"}), 404


@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    global employees
    employees = [e for e in employees if e["id"] != id]
    return jsonify({"message": f"Employee with ID {id} deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
