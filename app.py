from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS  # To allow frontend to access backend

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ad_vijithkumarjr@11",
    database="testdb"
)
cursor = conn.cursor()
# Create login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    query = "SELECT * FROM users WHERE name = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    if user:
        return jsonify({"message": f"Welcome, {username}!"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401
def signin():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    query = "INSERT INTO users(name,password) values(%s,%s)"
    cursor.execute(query,(username,password))
    user = cursor.fetchone()
    if user:
        return jsonify({"message": f"Hi, {username}!"})
    else:
        return jsonify({"message" : "oops 404"}),401
if __name__ == '__main__':
    app.run(debug=True)
