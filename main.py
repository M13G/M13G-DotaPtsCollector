import json

f = open("api_key.json",)
data = json.load(f)
print(data["api_key"])