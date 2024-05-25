import requests
import usaddress


def verify_address(address):
   try:
       # Parse the address string into components using usaddress
       parsed_address = usaddress.parse(address)
       street_number = ""
       street_name = ""
       city = ""
       state = ""
       zip_code = ""


       # Temporary variables to concatenate components
       temp_street_name = []


       # Extract relevant components from the parsed address
       for component in parsed_address:
           if component[1] == "AddressNumber":
               street_number = component[0]
           elif component[1] == "StreetName":
               temp_street_name.append(component[0])
           elif component[1] == "PlaceName":
               city = component[0]
           elif component[1] == "StateName":
               state = component[0]
           elif component[1] == "ZipCode":
               zip_code = component[0]


       # Concatenate components for the street name
       street_name = " ".join(temp_street_name)


       # Construct the URL with address parameters in the query string
       #api_key = "MCyQtIXDDgCjb4K3S3qwcn**nSAcwXpxhQ0PC2lXxuDAZ-**"
       url = f'https://property.melissadata.net/v4/WEB/LookupProperty?id={api_key}&t=Test&format=JSON&cols=&account=&addresskey=&a1={street_number}%20{street_name}&a2=&apn=&city={city}&country=&fips=&ff=&mak=&state={state}&postal={zip_code}'


       # Sending the request
       response = requests.get(url)


       # Check if the request was successful
       if response.status_code == 200:
           # Parsing the JSON response
           result = response.json()
           print(result)  # Print the response for debugging


           # Check if the address was verified successfully
           records = result.get('Records', [])
           if any('YS02' in record['Results'] for record in records) or any('YS07' in record['Results'] for record in records):
               return True
           else:
               return False
       else:
           print("Error:", response.status_code)
           return False
   except Exception as e:
       print("Error:", e)
       return False


# Example usage
if __name__ == "__main__":
   address = "5050 Banff Park Ct, Fremont, CA 94538"
   is_valid = verify_address(address)
  
   if is_valid:
       print("The address is valid.")
   else:
       print("The address is invalid.")
