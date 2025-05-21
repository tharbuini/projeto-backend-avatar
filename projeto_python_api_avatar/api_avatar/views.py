from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
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

    paginador = Paginator(lista_personagens, 9)
    numero_pagina = request.GET.get("page")
    pagina_obj = paginador.get_page(numero_pagina)
    
    return render(request, "index.html", {'pagina_obj': pagina_obj})
