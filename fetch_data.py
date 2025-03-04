import requests
import json

# URL of the API endpoint
api_url = "https://api.example.com/data"

# Fetch data from the API
response = requests.get(api_url)
data = response.json()

# Save data to a JSON file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Data fetched and saved to data.json")
