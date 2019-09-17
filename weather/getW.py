import json

with open("weather.txt") as f:
    data = json.load(f)
    print(data)

print(data['plaatsnaam'][0]["plaats"])


