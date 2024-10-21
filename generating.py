import requests
import json
from config import MOCKAROO_API_URL

response = requests.get(MOCKAROO_API_URL)

if response.status_code == 200:
    # write
    data = response.json()
    with open("generated_data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
else:
    print(f"Error: {response.status_code}, {response.text}")
