import requests

API_KEY = 'fca_live_8oKV0CoJ9uEtJ7toFrAX5MrCaCltuCAn9O5e8QW4'

# Correcting the URL string and variable name
Base_Url = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "EUR", "CAD", "AUD", "CNY" ]

def convert_currency(base):

    # Correcting the currency parameter
    currencies = ",".join(CURRENCIES)
    url = f"{Base_Url}&base_currency={base}&currencies={currencies}"

    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print(e)
        return None
    
while True:
    cur=input("Please enter The Currency Rate you want to convert").upper()
    val=int(input("Please enter amount that you want to convert"))

    if cur=="Q":
        break
    
    data=convert_currency(cur)

    if not data:
      continue

    del data[cur]
    for ticker , value in data.items():
        print(f"{val} {cur} = {val * value} {ticker}")
