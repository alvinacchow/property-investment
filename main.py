from flask import Flask, render_template, request, jsonify
from melissa_api import verify_address

app = Flask(__name__)

@app.route("/")
def hello_world():
    #return render_template("index.html")
    return render_template("portfolio.html")

@app.route("/verify-address", methods=["POST"])
def verify_address_route():
    data = request.get_json()
    address = data.get("address")

    if address:
        is_valid = verify_address(address)
        return jsonify({"is_valid": is_valid})
    else:
        return jsonify({"error": "Address not provided"}), 400

if __name__ == '__main__':
    app.run(debug = True)
    