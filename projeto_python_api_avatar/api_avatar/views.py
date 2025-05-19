from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests, json
from googletrans import Translator

def personagens(request):  
    api_url = 'https://last-airbender-api.fly.dev/api/v1/characters'
    lista_personagens = requests.get(api_url)
    lista_personagens = lista_personagens.json()
    tradutor = Translator()

    for personagem in lista_personagens:
        personagem["aliados"] = personagem.pop("allies")
        personagem["inimigos"] = personagem.pop("enemies")
        personagem["nome"] = personagem.pop("name")
        
        nome = personagem["nome"].strip()
        personagem["nome"] = tradutor.translate(nome, src="en", dest="pt").text
        aliados = personagem["aliados"]
        personagem["aliados"] = [
            tradutor.translate(aliado, src="en", dest="pt").text for aliado in aliados
        ]
        inimigos = personagem["inimigos"]
        personagem["inimigos"] = [
            tradutor.translate(inimigo, src="en", dest="pt").text for inimigo in inimigos
        ]
        
        if ("affiliation" in personagem):
            personagem["afiliacao"] = personagem.pop("affiliation")
            afiliacao = personagem["afiliacao"].strip().lower()
            personagem["afiliacao"] = tradutor.translate(afiliacao, src="en", dest="pt").text.capitalize()

    return render(request, "index.html", {'personagens': lista_personagens})
    
    # JSON PURO -> return JsonResponse(personagens, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})