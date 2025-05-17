import requests, json
from googletrans import Translator

personagens = requests.get('https://last-airbender-api.fly.dev/api/v1/characters')
personagens = personagens.json()
tradutor = Translator()

for personagem in personagens:
    nome = personagem["name"].strip()
    personagem["name"] = tradutor.translate(nome, src="en", dest="pt").text
    
    if ("affiliation" in personagem):
        afiliacao = personagem["affiliation"].strip().lower()
        personagem["affiliation"] = tradutor.translate(afiliacao, src="en", dest="pt").text.capitalize()


resposta_formatada = json.dumps(personagens, ensure_ascii=False, indent=4)
print(resposta_formatada)