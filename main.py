import requests

params = (
    ('locatie', 'Utrecht'),
    ('key', '9dc38406b2'),
)

response = requests.get('https://meteoserver.nl/api/uurverwachting.php', params=params)

print(response.content)