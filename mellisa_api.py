import requests

def verify_address(street_number, street_name, city, state, zip_code):
    # Construct the URL with address parameters in the query string
    api_key = "MCyQtIXDDgCjb4K3S3qwcn**nSAcwXpxhQ0PC2lXxuDAZ-**"
    url = f'https://property.melissadata.net/v4/WEB/LookupProperty?id={api_key}&t=Test&format=JSON&cols=&account=&addresskey=&a1={street_number}%20{street_name}&a2=&apn=&city={city}&country=&fips=&ff=&mak=&state={state}&postal={zip_code}'

    # Sending the request
    response = requests.get(url)

    # Parsing the JSON response
    result = response.json()
    print(result)

    # Check if the address was verified successfully
    records = result.get('Records', [])
    if any('YS02' in record['Results'] for record in records) or any('YS07' in record['Results'] for record in records):
        return True
    else:
        return False

# Example usage
if __name__ == "__main__":
    street_number = "5050" #input("Enter the street number: ")
    street_name = "Banff Park" #input("Enter the street name: ")
    city = "Fremont" #input("Enter the city: ")
    state = "CA" #input("Enter the state: ")
    zip_code = "94538" #input("Enter the ZIP code: ")

    is_valid = verify_address(street_number, street_name, city, state, zip_code)
    
    if is_valid:
        print("The address is valid.")
    else:
        print("The address is invalid.")