from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import sys

print("🔥 Python file is running")

app = Flask(__name__)
CORS(app)

print("🔄 Attempting MySQL connection...")

# -------- MYSQL CONNECTION --------
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="NITHISHELANGo@06",
        database="health_app",
        use_pure=True
    )
    print("✅ MySQL connected successfully")
except Exception as e:
    print("❌ MySQL connection failed")
    print(e)
    sys.exit(1)

# -------- HOME ROUTE --------
@app.route("/")
def home():
    return "Flask + MySQL is running!"

# -------- LOGIN API --------
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    mobile = data.get("mobile")

    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE mobile=%s", (mobile,))
    user = cursor.fetchone()
    cursor.close()

    if user:
        return jsonify({"status": "success", "user": user})
    else:
        return jsonify({"status": "fail", "message": "User not found"})

# -------- REGISTER API --------
@app.route("/register", methods=["POST"])
def register():
    data = request.json

    try:
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO users 
            (name, mobile, email, age, weight, height, bmi, bmi_suggestion, body_type, exercise_level)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
            data.get("name"),
            data.get("mobile"),
            data.get("email"),
            data.get("age"),
            data.get("weight"),
            data.get("height"),
            data.get("bmi"),
            data.get("bmiSuggestion"),
            data.get("bodyType"),
            data.get("exercise")
        ))

        db.commit()
        cursor.close()

        return jsonify({
            "status": "success",
            "message": "Registration successful"
        })

    except Exception as e:
        print("❌ Registration error:", e)
        return jsonify({
            "status": "fail",
            "message": "Registration failed"
        }), 500

# -------- SAVE MEAL API --------
@app.route("/save-meal", methods=["POST"])
def save_meal():
    data = request.json

    try:
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO favorite_meals (user_mobile, meal_name)
            VALUES (%s, %s)
        """, (
            data.get("mobile"),
            data.get("meal")
        ))

        db.commit()
        cursor.close()

        return jsonify({
            "status": "success",
            "message": "Meal saved"
        })

    except Exception as e:
        print("❌ Save meal error:", e)
        return jsonify({
            "status": "fail",
            "message": "Failed to save meal"
        }), 500

# -------- START SERVER --------
if __name__ == "__main__":
    print("🚀 Starting Flask server...")
    app.run(host="127.0.0.1", port=5000, debug=True)
