import requests
import json
import pandas as pd 
import matplotlib.pyplot as plt 
from keys import Key


def readFilePropertyInfo(input_file) -> list[dict]:
    # "data/alvina-home.json"
    with open(input_file) as file:
        data = json.load(file)
        sales = []
        for record in data['Records']:
            year = record['DocInfo']['RecordingDate'][:4]
            amount = float(record['TxAmtInfo']['TransferAmount'])
            sales.append({"year": year, "amount": amount})
        return sales
    
    
def makeGraph(history: list[dict]): 
    history = [entry for entry in history if entry['amount'] > 0]
    
    years = [int(entry['year']) for entry in history]
    values = [entry['amount'] for entry in history]

    plt.plot(years, values, marker='o')
    plt.title('Property Sale Prices Over Time')
    plt.xlabel('Year')
    plt.ylabel('Sale Price ($)')
    plt.xticks(years, [format(int(year), 'd') for year in years])
    plt.yticks(values, [format(int(value), ',d') for value in values])
    plt.savefig('static/plot.png')
    

if __name__ == '__main__':
    sales = readFilePropertyInfo("data/alvina-home.json")
    makeGraph(sales)