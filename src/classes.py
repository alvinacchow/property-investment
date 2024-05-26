import csv 

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
    


class Portfolio:
    assets = []

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return f"Portfolio(email={self.email}, assets={Portfolio.assets})"
        
    def add_asset(asset):
        Portfolio.assets.append(asset)

    def remove_asset(self, asset):
        if asset in self.assets:
            self.assets.remove(asset)

    def to_dict(year): 
        asset_dict = []
        for asset in Portfolio.assets: 
            inner = dict()
            inner["property"] = asset.Address
            inner["current"] = asset.current_price
            inner["predicted"] = asset.price_projections[2024 + int(year)]
            inner["change"] = (asset.price_projections[2024 + int(year)] - asset.current_price) / asset.current_price * 100
            asset_dict.append(inner)
        return asset_dict

    def get_assets():
        return Portfolio.assets

    def get_total_current_value(self):
        return sum(asset.get_current_price() for asset in self.assets)

    def get_total_predicted_value(self):
        return sum(asset.get_predicted_price() for asset in self.assets)

    def authenticate(self, password):
        return self.password == password


if __name__ == '__main__':
    Portfolio.add_asset(Asset())
    Portfolio.to_dict()