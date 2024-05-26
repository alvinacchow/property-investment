import requests
import json
import matplotlib.pyplot as plt 
import csv 
import os 

from keys import Key
from prediction import make_prediction


def search_from_api(address: str):
    city = address.split(",")[1].strip()
    getSaleListings(city = city, input_file = None)
    write_test_file(address = address, input_file = None)
    make_prediction(city)

    
def getSaleListings(*, city: str, input_file = None):
    field_names = ["Id", "BldgType", "YearBuilt", "GrLivArea", "BedroomAbvGr", "FullBath"]
    filename = f'ai-model/{city}-listings.csv'

    if os.path.exists(filename):
        return

    with open(filename, 'w', newline='') as csvfile:
        if input_file is not None:
            with open(input_file) as file:
                data = json.load(file)
        else:
            url = "https://api.rentcast.io/v1/listings/sale"
            headers = {
                "accept": "application/json",
                "X-Api-Key": Key.rentcast_key1
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
            Address = address
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
        
        Address = address
        BldgType = data[0].get("propertyType", "")
        YearBuilt = data[0].get("yearBuilt", 0)
        GrLivArea = data[0].get("squareFootage", 0)
        BedroomAbvGr = data[0].get("bedrooms", 0)
        FullBath = data[0].get("bathrooms", 0)

    return Address,BldgType,YearBuilt,GrLivArea,BedroomAbvGr,FullBath
  
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
    else: 
        url = f'https://property.melissadata.net/v4/WEB/LookupDeeds/?id={Key.melissa_key}&format=JSON&ff={address}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            sales = []
            for record in data['Records']:
                year = record['DocInfo']['RecordingDate'][:4]
                amount = float(record['TxAmtInfo']['TransferAmount'])
                sales.append({"year": year, "amount": amount})

    return sales



if __name__ == '__main__':
    # search_from_api("4126 1st Avenue NW, Seattle, WA 98107")
    readFilePropertyInfo(address="4126 1st Avenue NW, Seattle, WA 98107", input_file=None)