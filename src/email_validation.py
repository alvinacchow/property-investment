import requests
from src.keys import Key
def validate_email(email):
    api_key = Key.melissa_key
    url = f"https://globalemail.melissadata.net/v4/WEB/GlobalEmail/doGlobalEmail?&id={api_key}&opt=VerifyMailbox:Express,DomainCorrection:OFF,TimeToWait:25&format=json&email={email}"

    response = requests.get(url)
    
    if response.text:
        try:
            result = response.json()
            print(f'{result}\n\n\n') #debug
            records = result.get('Records', [])
            if records:
                record = records[0]
                results_codes = record.get('Results', '')
                if 'ES01' in results_codes:
                    return True  # Email is valid
                else:
                    print(f"Email validation failed with codes: {results_codes}")
                    return False
        except ValueError as e:
            print("Error decoding JSON:", e)
            return False
    else:
        print("Empty response received.")
        return False







