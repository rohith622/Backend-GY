from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")  
db = client.companyDB
employees_collection = db.employees


@app.route('/employees', methods=['GET'])
def get_employees():
    
    employees = list(employees_collection.find({}, {"_id": 0}))
    return jsonify(employees)

if __name__ == '__main__':
    app.run(debug=True)
