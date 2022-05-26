import requests
import json

# r = requests.get("https://api.postcodes.io/postcodes/SE12 0NB")

headers = {"Content-Type": "application/json"}
dict_of_postcodes = {"postcodes": ["OX49 5NU", "M32 0JG", "NE30 1DP"]}
data = json.dumps(dict_of_postcodes)

r = requests.post(
    url="https://api.postcodes.io/postcodes",
    headers=headers,
    data=data,
)
#print(r.json())

d = r.json()
for i in range(0, 3):
    postcode = d["result"][i]["result"]["postcode"]
    region = d["result"][i]["result"]["region"]
    parliamentary_constituency = d["result"][i]["result"]["parliamentary_constituency"]
    print(postcode)
    print(region)
    print(parliamentary_constituency)


