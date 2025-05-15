import requests

r = requests.get('https://last-airbender-api.fly.dev/api/v1/characters')

print(r.json())