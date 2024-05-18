import random
import requests

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def coin():
    return random.choice(["Орел","Решка"])

def get_price_history():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1"
    response = requests.get(url)
    data = response.json()
    prices = data["prices"]
    return [price[1] for price in prices]
