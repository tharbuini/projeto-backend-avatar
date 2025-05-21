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
        personagem["aliados"] = personagem.pop("allies", [])
        personagem["inimigos"] = personagem.pop("enemies", [])
        personagem["nome"] = tradutor.translate(personagem.pop("name", ""), src="en", dest="pt").text
        personagem["aliados"] = [tradutor.translate(a, src="en", dest="pt").text for a in personagem["aliados"]]
        personagem["inimigos"] = [tradutor.translate(i, src="en", dest="pt").text for i in personagem["inimigos"]]
        if "affiliation" in personagem:
            personagem["afiliacao"] = tradutor.translate(personagem.pop("affiliation", ""), src="en", dest="pt").text.capitalize()
        else:
            personagem["afiliacao"] = "Desconhecida"

    return render(request, "index.html", {'personagens': lista_personagens})
    
    # JSON PURO -> return JsonResponse(personagens, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})