from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="db",            # service name defined in docker-compose
        user="root",
        password="rootpass",
        database="flaskdb"
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT message FROM greetings LIMIT 1;")
    result = cursor.fetchone()
    conn.close()
    return jsonify({"message": result[0] if result else "No message"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
