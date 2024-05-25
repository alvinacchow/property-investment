from flask import Flask, render_template, request, jsonify
from melissa_api import verify_address
import json
<<<<<<< HEAD

app = Flask(__name__)

=======


app = Flask(__name__)


>>>>>>> 6f72f6b2e904d9df25ef7f4295af238d9a25eb10
with open('login_data.json', 'r') as file:
   login_data = json.load(file)


@app.route("/")
def index():
   return render_template("index.html")


@app.route("/portfolio")
def portfolio():
   return render_template("portfolio.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/login", methods=["POST"])
def login():
<<<<<<< HEAD
    email = request.json.get("email")
    print(email)
    
    if any(user["email"] == email for user in login_data):
        print('true')
        return jsonify({"success": True, "message": "Email validated"})
    else:
        print('false')
        return jsonify({"success": False, "message": "Email not validated"})
=======
   email = request.json.get("email")
   print(email)


   # Check if the provided email exists in the login data
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
>>>>>>> 6f72f6b2e904d9df25ef7f4295af238d9a25eb10

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

<<<<<<< HEAD
=======
if __name__ == '__main__':
   app.run(debug = True)
>>>>>>> 6f72f6b2e904d9df25ef7f4295af238d9a25eb10
