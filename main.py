from flask import Flask, render_template, request, jsonify
from src.melissa_api import verify_address
from src.objects import preprocessing, makeGraph
from src.classes import Portfolio, Asset
from src.rent import search_from_api, readFilePropertyInfo

import json

app = Flask(__name__)

with open('dataCopy/login_data.json', 'r') as file:
   login_data = json.load(file)


@app.route("/")
def index():
   return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    year = request.args.get('years')
    if (year is None): year = 5
    assets_data = [Portfolio.to_dict(year)]
    return render_template("portfolio.html", assets=assets_data, year=year)

@app.route('/popAsset', methods=['POST'])
def pop_asset():
    popped_asset = Portfolio.pop_asset()
    Portfolio.add_asset_to_portfolio(popped_asset)
    return 'Asset popped successfully', 200

@app.route("/search")
def search():
    asset = preprocessing()
    Portfolio.add_asset_to_cached(asset)
    asset_dict = asset.to_dict()
    search_data = [asset_dict]
    history = sorted(readFilePropertyInfo(address=asset_dict["address"], input_file='dataCopy/deed-alvina-home.json'), key=lambda x: int(x['year']))
    history.append({'year': 2024, 'amount': int(float(asset.current_price))})
    for year, amount in asset.price_projections.items():
        history.append({'year': str(year), 'amount': amount})
    makeGraph(history)
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