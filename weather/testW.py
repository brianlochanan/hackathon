import requests
import json

params = (
    ('locatie', 'Utrecht'),
    ('key', '85c9b987c6'),
)

response = requests.get('https://meteoserver.nl/api/uurverwachting.php', params=params)
content = response.content

response10 = requests.get('https://meteoserver.nl/api/uurverwachting_gfs.php', params=params)
content10 = response10.content

# file = open("weather.txt", "w+")
# file.write(str(response.content)[2:-1])
# with open('Weather.json', 'w', encoding='utf-8') as f:
#     json.dump(content.decode("utf-8"), f, ensure_ascii=False, indent=4)

# generates a str file
file = open("weather.txt", "w+")
file.write(str(response.content)[2:-1])

file2 = open("weather10.txt", "w+")
file2.write(str(response10.content)[2:-1])

# generates a json file
with open('Weather.json', 'w', encoding='utf-8') as f:
    json.dump(content.decode("utf-8"), f, ensure_ascii=False, indent=4)

with open('Weather10.json', 'w', encoding='utf-8') as f:
    json.dump(content10.decode("utf-8"), f, ensure_ascii=False, indent=4)
