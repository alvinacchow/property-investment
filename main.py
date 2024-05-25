import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load login credentials from a JSON file
with open('login_data.json', 'r') as file:
    login_data = json.load(file)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.json.get("email")
    print(email)

    # Check if the provided email exists in the login data
    if any(user["email"] == email for user in login_data):
        print('true')
        return jsonify({"success": True, "message": "Email validated"})
    else:
        print('false')
        return jsonify({"success": False, "message": "Email not validated"})


if __name__ == "__main__":
    app.run(debug=True)
