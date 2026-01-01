import requests
import time

while True:
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    price = float(data["bitcoin"]["usd"])
    print("current price is:", price)
    if price<=80000:
        print("Time to buy")
    elif 80000<price<90000:
        print("Wait!")
    elif price>=90000:
        break
    time.sleep(600)
