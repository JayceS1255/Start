import requests
import sys
import json
import re

def main():

    if len(sys.argv) == 2:
        try:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            bitcoin = response.json()
            #print(json.dumps(bitcoin, indent = 4))

            if  bool(re.match(r'\d+(\.\d+)?', sys.argv[1])):
                usd  = bitcoin ["bpi"]["USD"]["rate_float"]
                amount = usd * float(sys.argv[1])
                formatted_amount = '{:,.2f}'.format(amount)
                print(formatted_amount)
                
            else:
                print("Command-line argument is not a number")
                sys.exit()   
    
        except requests.RequestException:
            print("Error has occured")
            sys.exit()
    else:
        print("Missing command-line argument")

if __name__ == "__main__":
    main()

'''simplified version:
import sys
import requests
import re

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <number>")
        return

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        bitcoin = response.json()
    except requests.RequestException:
        print("Error occurred while fetching data from Coindesk API")
        return

    arg = sys.argv[1]
    if not re.match(r'^\d+(\.\d+)?$', arg):
        print("Command-line argument is not a valid number")
        return

    usd_rate = bitcoin.get("bpi", {}).get("USD", {}).get("rate_float") --- gets and checks if bpi is a thing is bpi is not in the api then it returns{}/ nothing
    if usd_rate is None:
        print("Failed to retrieve USD exchange rate")
        return

    amount = float(arg) * usd_rate
    formatted_amount = '{:,.2f}'.format(amount)
    print("Equivalent amount in USD:", formatted_amount)

if __name__ == "__main__":
    main()'''


