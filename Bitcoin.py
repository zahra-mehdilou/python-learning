import requests
import time

while True:
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    price = float(data["bitcoin"]["usd"])
    print("current price is:", price)
    if price<950000:
        print("Time to buy")
    else:
        print("Wait!")
    time.sleep(600)

