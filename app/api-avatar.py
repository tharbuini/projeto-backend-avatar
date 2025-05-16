import requests, json

r = requests.get('https://last-airbender-api.fly.dev/api/v1/characters')

print((json.dumps(r.json(), indent=4)))