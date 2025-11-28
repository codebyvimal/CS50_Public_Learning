import requests
import sys

if len(sys.argv) != 2:
    print("Missing command-line argument")
try:
    x = float(sys.argv[1])
except ValueError:
    sys.exit

try:
    request = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=9691c15b2661636d8a6a75ed71d21f6a5e27a7148e5c2d371b99050e6ffb0570")
except requests.RequestException:
    print("Error")

y = request.json()
cost = float(y["data"]["priceUsd"])

final = cost*x
print(f"${final:,.4f}")
