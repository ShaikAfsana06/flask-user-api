from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for users
users = {}

# Home route
@app.route('/')
def home():
    return {"message": "Welcome to User Management API"}

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET user by ID
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[user_id])

# POST new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or "id" not in data or "name" not in data or "email" not in data:
        return jsonify({"error": "Missing required fields: id, name, email"}), 400

    user_id = data["id"]
    if user_id in users:
        return jsonify({"error": "User already exists"}), 400

    users[user_id] = data
    return jsonify({"error": "User not found"}), 404

    users.pop(user_id)
    return jsonify({"message": "User deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)
