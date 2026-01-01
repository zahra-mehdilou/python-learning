import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
response = requests.get(url)
data = response.json()
price = data["bitcoin"]["usd"]
print("current price is:", price)
if price<100000:
    print("Time to buy")
    type(price)

