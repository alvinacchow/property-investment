import requests

def verify_address(street_number, street_name, city, state, zip_code):
    # Construct the URL with address parameters in the query string
    api_key = "OQutH9yb_CYfjFKHKEBlt0**nSAcwXpxhQ0PC2lXxuDAZ-**"
    url = f'https://property.melissadata.net/v4/WEB/LookupProperty?id={api_key}&t=Test&format=JSON&cols=&account=&addresskey=&a1={street_number}%20{street_name}&a2=&apn=&city={city}&country=&fips=&ff=&mak=&state={state}&postal={zip_code}'

    # Sending the request
    response = requests.get(url)

    # Parsing the JSON response
    result = response.json()
    #print(result)

    # Check if the address was verified successfully
    if result['TotalRecords'] > 0:
        return True
    else:
        return False

# Example usage
if __name__ == "__main__":
    #api_key = "EeiRZjnx_At1a7m_mJJDCZ**"
    street_number = "10956" #input("Enter the street number: ")
    street_name = "Fairbanks Way" #input("Enter the street name: ")
    city = "Culver City" #input("Enter the city: ")
    state = "CA" #input("Enter the state: ")
    zip_code = "90230" #input("Enter the ZIP code: ")

    is_valid = verify_address(street_number, street_name, city, state, zip_code)
    
    if is_valid:
        print("The address is valid.")
    else:
        print("The address is invalid.")
