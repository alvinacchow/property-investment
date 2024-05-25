import requests
import json
import pandas as pd 
import matplotlib.pyplot as plt 
from keys import Key



def getPropertyInfo(address: str) -> json:
    url = "https://api.rentcast.io/v1/properties"
    headers = {
        "accept": "application/json",
        "X-Api-Key": Key.rentcast_key2
    }
    params = {"address": address}
    response = requests.get(url, headers=headers, params=params)
    return json.response()

def processPropertyInfo(response: json): 
    last_sale_date = response[0]["lastSaleDate"]
    last_sale_price = response[0]["lastSalePrice"]
    tax_assessments = response[0]["taxAssessments"]


def readFilePropertyInfo():
    with open("data/alvina-home.json") as file:
        data = json.load(file)
        last_sale_date = data[0]["lastSaleDate"]
        last_sale_price = data[0]["lastSalePrice"]
        tax_assessments = data[0]["taxAssessments"]
        # print(last_sale_date)
        # print(last_sale_price)
        # print(tax_assessments)
        return last_sale_date, last_sale_price, tax_assessments

def makeGraph(tax_assessments: json): 
    # {'2021': {'value': 1041898, 'land': 520949, 'improvements': 520949}, 
    #  '2022': {'value': 1062734, 'land': 531367, 'improvements': 531367}, 
    #  '2023': {'value': 1083988, 'land': 541994, 'improvements': 541994}}
    years = list(tax_assessments.keys())
    values = [tax_assessments[year]["value"] for year in years]

    plt.plot(years, values, marker='o')
    plt.title('Price')
    plt.xlabel('Year')
    plt.ylabel('Assessment Value')
    plt.yticks(values, [format(value, ',') for value in values])
    plt.savefig('plot.png')
    # plt.show()
    # fig, ax = plt.subplots()
    # s.plot.bar()
    # fig.savefig('plot.png')



# def getMarketValue():
#     url = "https://api.rentcast.io/v1/avm/value"
#     headers = {"accept": "application/json",
#             "X-Api-Key": keys.key1
#             }
#     params = {}
#     response = requests.get(url, headers=headers)
#     print(response.text)

if __name__ == '__main__':
    last_sale_date, last_sale_price, tax_assessments = readFilePropertyInfo()
    print(makeGraph(tax_assessments))