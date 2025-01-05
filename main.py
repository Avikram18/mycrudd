from flask import Flask, jsonify, request

app = Flask(__name__)

Employees = [
    {"id": 1, "name": "name1", "post": "SWE"},
    {"id": 2, "name": "name2", "post": "TL"},
    {"id": 3, "name": "name3", "post": "PM"}
]

# Display all employees
@app.route('/employees', methods=["GET"])
def get_employees():
    return jsonify(Employees),200

# Fetch employee based on ID or name using query parameters
@app.route('/employees/search', methods=["GET"])
def search_employee():
    emp_id = request.args.get("id", type=int)
    emp_name = request.args.get("name")
    for emp in Employees:
        if emp_id and emp["id"] == emp_id:
            return jsonify(emp),200
        if emp_name and emp["name"].lower() == emp_name.lower():
            return jsonify(emp),200
        
    return jsonify({"error": "employee not found"}), 404

# Create a new employee
@app.route('/employees', methods=["POST"])
def create_employee():
    if not request.json or "name" not in request.json or "post" not in request.json:
        return jsonify({"error": "Invalid data"}), 400

    new_id = max(emp["id"] for emp in Employees) + 1
    new_employee = {
        "id": new_id,
        "name": request.json["name"],
        "post": request.json["post"]
    }
    Employees.append(new_employee)
    return jsonify(new_employee), 200

# Update an existing employee
@app.route('/employees/<int:emp_id>', methods=["PUT"])
def update_employee(emp_id):
    for emp in Employees:
        if emp["id"] == emp_id:
            emp["name"] = request.json.get("name", emp["name"])
            emp["post"] = request.json.get("post", emp["post"])
            return jsonify(emp),200
    
    return jsonify({"error": "employee not found"}), 404

# Delete an employee
@app.route('/employees/<int:emp_id>', methods=["DELETE"])
def delete_employee(emp_id):
    for emp in Employees:
        if emp["id"] == emp_id:
            Employees.remove(emp)
            return jsonify({"success": "employee deleted"}), 200
    return jsonify({"error": "employee not found"}), 404

# Running Flask
if __name__ == '__main__':
    app.run(debug=True)
