import requests
import json
import pandas as pd 
import matplotlib.pyplot as plt 
from keys import Key
import csv 


def search(address: str):
    city = address.split(",")[1].strip()
    getSaleListings(city = city, input_file = None)
    write_test_file(address = address, input_file = None)
    
def getSaleListings(*, city: str, input_file = None):
    field_names = ["Id", "BldgType", "YearBuilt", "GrLivArea", "BedroomAbvGr", "FullBath"]
    with open('ai-model/city-listings.csv', 'w', newline='') as csvfile: 
        if input_file is not None:
            with open(input_file) as file:
                data = json.load(file)
        else:
            url = "https://api.rentcast.io/v1/listings/sale"
            headers = {
                "accept": "application/json",
                "X-Api-Key": Key.rentcast_key2
            }
            params = {"city": city}
            response = requests.get(url, headers=headers, params=params)  
            data = response.json()
  
        index = 1
        field_names = ["Id", "BldgType", "YearBuilt", "GrLivArea", "BedroomAbvGr", "FullBath", "SalePrice"]
        
        writer = csv.writer(csvfile)
        writer.writerow(field_names)
        for property in data:
            if property["propertyType"].lower() == "land":
                continue 

            fields = []
            fields.extend((index, property.get("propertyType", ""), property.get("yearBuilt", 0), property.get("squareFootage"), property.get("bedrooms", 0), property.get("bathrooms", 0), property.get("price", 0)))
            writer.writerow(fields)
            index += 1

def write_test_file(*, address: str, input_file = None):
    data = [1]
    data = getPropertyDetails(address = address, input_file = input_file)
    # Define the field names
    field_names = ["Id", "BldgType", "YearBuilt", "GrLivArea", "BedroomAbvGr", "FullBath"]
    
    # Write data to CSV file
    with open('ai-model/entry.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(field_names)
        writer.writerow(data)
        
def getPropertyDetails(*, address: str, input_file = None):
    if input_file is not None:
        with open(input_file) as file:
            data = json.load(file)
            Id = 1
            BldgType = data[0].get("propertyType", "")
            YearBuilt = data[0].get("yearBuilt", 0)
            GrLivArea = data[0].get("squareFootage", 0)
            BedroomAbvGr = data[0].get("bedrooms", 0)
            FullBath = data[0].get("bathrooms", 0)
    else: 
        url = "https://api.rentcast.io/v1/properties"
        headers = {
            "accept": "application/json",
            "X-Api-Key": Key.rentcast_key2
        }
        params = {"address": address}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        
        Id = 1
        BldgType = data[0].get("propertyType", "")
        YearBuilt = data[0].get("yearBuilt", 0)
        GrLivArea = data[0].get("squareFootage", 0)
        BedroomAbvGr = data[0].get("bedrooms", 0)
        FullBath = data[0].get("bathrooms", 0)

    return Id,BldgType,YearBuilt,GrLivArea,BedroomAbvGr,FullBath
    
def readFilePropertyInfo(*, address: str, input_file = None) -> list[dict]:
    # melissa api 
    if input_file is not None: 
        with open(input_file) as file:
            data = json.load(file)
            sales = []
            for record in data['Records']:
                year = record['DocInfo']['RecordingDate'][:4]
                amount = float(record['TxAmtInfo']['TransferAmount'])
                sales.append({"year": year, "amount": amount})
            return sales
    else: 
        pass 
        ### TODO: add API entry point ###

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
