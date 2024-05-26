from src.classes import Asset, Portfolio
import csv
import matplotlib
import matplotlib.pyplot as plt 
matplotlib.use('agg')

def makeGraph(history: list[dict]): 
    history = [entry for entry in history if entry['amount'] > 0]
    
    years = [int(entry['year']) for entry in history]
    values = [entry['amount'] for entry in history]

    plt.plot(years, values, color='mediumpurple', marker='o')
    plt.plot(years[years.index(2024):], values[years.index(2024):], marker='o', color='forestgreen', label='From 2024')
    plt.title('Property Sale Prices Over Time')
    plt.xlabel('Year')
    plt.ylabel('Sale Price ($)')
    plt.xticks(years, [format(int(year), 'd') for year in years])
    plt.yticks(values, [format(int(value), ',d') for value in values])
    plt.savefig('static/plot.png')
    

def get_prediction():
    with open('ai-model/prediction.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        next(csvFile)
        line = next(csvFile)
        return line[1]

def calculate_projections(current_price) -> dict:
    price = int(float(current_price))
    price_dict = {}
    for i in range(5, 30, 5):
        price_dict[2024 + i] = int(float(price * 1.04**5))
        price = int(float(price * 1.04**5))
    return price_dict

def preprocessing():
    current_price = get_prediction()
    property = Asset(current_price, calculate_projections(current_price))
    return property

def addToPortfolio(property):
    Portfolio.add_asset(property)
   
