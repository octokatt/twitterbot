import requests
response = requests.get("https://api.weather.gov/points/45.6763,-122.5416")

results = response.json()

print(response)
print(results)