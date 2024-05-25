class Asset:
    def __init__(self, current_price, predicted_price):
        self.current_price = current_price
        self.predicted_price = predicted_price

    def __repr__(self):
        return f"Asset(current_price={self.current_price}, predicted_price={self.predicted_price})"

    def get_current_price(self):
        return self.current_price

    def get_predicted_price(self):
        return self.predicted_price

    def set_current_price(self, price):
        self.current_price = price

    def set_predicted_price(self, price):
        self.predicted_price = price

class Portfolio:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.assets = []

    def __repr__(self):
        return f"Portfolio(email={self.email}, assets={self.assets})"

    def add_asset(self, asset):
        self.assets.append(asset)

    def remove_asset(self, asset):
        if asset in self.assets:
            self.assets.remove(asset)

    def get_assets(self):
        return self.assets

    def get_total_current_value(self):
        return sum(asset.get_current_price() for asset in self.assets)

    def get_total_predicted_value(self):
        return sum(asset.get_predicted_price() for asset in self.assets)

    def authenticate(self, password):
        return self.password == password

# Example Usage
if __name__ == "__main__":
    asset1 = Asset(current_price=100, predicted_price=150)
    asset2 = Asset(current_price=200, predicted_price=250)

    # Create a portfolio
    portfolio = Portfolio(email="example@example.com", password="securepassword")

    # Add assets to the portfolio
    portfolio.add_asset(asset1)
    portfolio.add_asset(asset2)

    # Print the portfolio
    print(portfolio)

    # Get total current value of the portfolio
    print(f"Total current value: {portfolio.get_total_current_value()}")

    # Get total predicted value of the portfolio
    print(f"Total predicted value: {portfolio.get_total_predicted_value()}")
