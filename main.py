from flask import Flask, render_template, request, jsonify
from melissa_api import verify_address
import json


app = Flask(__name__)

with open('login_data.json', 'r') as file:
   login_data = json.load(file)


@app.route("/")
def index():
   return render_template("index.html")

@app.route("/portfolio")
def portfolio():
   return render_template("portfolio.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.json.get("email")
    print(email)
    
    if any(user["email"] == email for user in login_data):
        print('true')
        return jsonify({"success": True, "message": "Email validated"})
    else:
        print('false')
        return jsonify({"success": False, "message": "Email not validated"})

@app.route("/verify-address", methods=["POST"])
def verify_address_route():
    data = request.get_json()
    address = data.get("address")

    if address:
        is_valid = verify_address(address)
        if is_valid:
            return jsonify({"success": True, "message": "Address validated"})
        else:
            return jsonify({"success": False, "message": "Address not validated"})
    else:
        return jsonify({"error": "Address not provided"}), 400

if __name__ == '__main__':
    app.run(debug = True)