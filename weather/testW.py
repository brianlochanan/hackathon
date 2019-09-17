import requests
import json

params = (
    ('locatie', 'Utrecht'),
    ('key', '85c9b987c6'),
)

response = requests.get('https://meteoserver.nl/api/uurverwachting.php', params=params)
content = response.content

file = open("weather.txt", "w+")
file.write(str(response.content)[2:-1])
with open('Weather.json', 'w', encoding='utf-8') as f:
    json.dump(content.decode("utf-8"), f, ensure_ascii=False, indent=4)


# NB. Original query string below. It seems impossible to parse and reproduce query strings 100% accurately so the
# one below is given in case the reproduced version is not "correct". response = requests.get(
# 'https://meteoserver.nl/api/liveweer.php?lat=52.1052957&long=5.1806729&key=efef8e8a12', headers=headers,
# cookies=cookies)


