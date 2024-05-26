import csv 
import math 

class Asset:
    def __init__(self, current_price, price_projections):
        self.current_price = current_price
        self.price_projections = price_projections

        with open('ai-model/entry.csv', mode ='r') as file:
            csvFile = csv.reader(file)
            next(csvFile) # header 
            self.Address, self.BldgType, self.YearBuilt, self.GrLivArea, self.BedroomAbvGr, self.FullBath = next(csvFile)
    
    def __repr__(self):
        return f"Asset(address={self.Address}, current_price={self.current_price}, predicted_price={self.price_projections}, building_type={self.BldgType}, year_built={self.YearBuilt}, square_ft={self.GrLivArea}, bedrooms={self.BedroomAbvGr}, bathrooms={self.FullBath})"

    def get_current_price(self):
        return self.current_price

    def get_price_projections(self): 
        return self.price_projections
    
    def to_dict(self):
        return {"address": self.Address, "current_price": self.current_price, "building_type": self.BldgType, "year_built": self.YearBuilt, "square_ft": self.GrLivArea, "bedrooms": self.BedroomAbvGr, "bathrooms": self.FullBath}
    

class Portfolio:
    assets = []
    cached = []

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return f"Portfolio(email={self.email}, assets={Portfolio.assets})"
        
    def add_asset_to_portfolio(asset):
        Portfolio.assets.append(asset)

    def add_asset_to_cached(asset):
        Portfolio.assets.append(asset)

    @staticmethod
    def pop_asset():
        if Portfolio.assets:
            return Portfolio.assets.pop()
        return None

    def to_dict(year): 
        asset_dict = []
        for asset in Portfolio.assets: 
            inner = dict()
            inner["property"] = asset.Address
            inner["current"] = "{:,}".format(math.ceil(int(float(asset.current_price))))
            inner["predicted"] = "{:,}".format(math.ceil(int(float(asset.price_projections[2024 + int(year)]))))
            change = math.ceil((int(asset.price_projections[2024 + int(year)]) - int(float(asset.current_price))) / int(float(asset.current_price)) * 100)
            inner["change"] = change
            asset_dict.append(inner)
        return asset_dict

    def get_assets():
        return Portfolio.assets

    def get_total_current_value(self):
        return math.ceil(sum(asset.get_current_price() for asset in self.assets))

    def get_total_predicted_value(self):
        return math.ceil(sum(asset.get_predicted_price() for asset in self.assets))

    def authenticate(self, password):
        return self.password == password
