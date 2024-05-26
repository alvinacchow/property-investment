from flask import Flask, render_template, request, jsonify
from melissa_api import verify_address
from src.objects import preprocessing
from src.classes import Portfolio, Asset
from src.rent import search_from_api

import json

app = Flask(__name__)

with open('login_data.json', 'r') as file:
   login_data = json.load(file)


@app.route("/")
def index():
   return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    year = request.args.get('years')
    if (year is None): year = 5
    # Portfolio.add_asset(Asset(1325529.0, {2024: 552340, 2029: 161708, 2034: 192105, 2039: 238700, 2044: 904393, 2049: 353638}))
    # Portfolio.add_asset(Asset(208164.42, {2024: 552340, 2029: 112708, 2034: 196105, 2039: 28720, 2044: 290393, 2049: 353338}))
    # Portfolio.add_asset(Asset(680422.56, {2024: 552340, 2029: 16708, 2034: 196215, 2039: 237200, 2044: 904393, 2049: 353638}))
    assets_data = [Portfolio.to_dict(year)]
    # print(assets_data)
    return render_template("portfolio.html", assets=assets_data, year=year)

@app.route("/search")
def search():
    asset = preprocessing()
    search_data = [asset.to_dict()]
    print(search_data)
    return render_template("search.html", asset = search_data).replace("HAI REPLACE ME",str(asset.to_dict()))

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
            search_from_api(address) 
            return jsonify({"success": True, "message": "Address validated"})
            
        else:
            return jsonify({"success": False, "message": "Address not validated"})
    else:
        return jsonify({"error": "Address not provided"}), 400

if __name__ == '__main__':
    app.run(debug = True)