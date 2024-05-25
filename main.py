from flask import Flask, render_template, request, jsonify
from email_validation import validate_email  # Ensure this import matches the filename of your validate_email function

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/validate_email", methods=["POST"])
def validate_user_email():
    data = request.get_json()
    email = data.get("email")
    is_valid = validate_email(email)
    return jsonify({"validated": is_valid})

if __name__ == "__main__":
    app.run(debug=True)