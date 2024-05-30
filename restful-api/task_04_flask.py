#!/usr/bin/python3
'''4. Develop a Simple API using Python with Flask'''


from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
users = {
    "jane":
    {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john":
    {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def get_users(username):
    if username in users:
        return jsonify(users[username])


@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.get_json()
    username = user_data.get("username")
    if username in users:  # Check if username exists
        return jsonify({"error": "L'utilisateur existe déjà"})
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data})


if __name__ == "__main__":
    app.run()
