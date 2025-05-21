# 🌊 Projeto Django - Personagens de Avatar: A Lenda de Aang

Este é um projeto Django que consome a [API pública de Avatar](https://last-airbender-api.fly.dev/), traduz seus dados para o português e exibe uma lista paginada com os personagens da série *Avatar: A Lenda de Aang*.
#7DaysOfCode #Alura

## 📋 Funcionalidades

- Consumo da API de personagens do universo Avatar
- Tradução automática dos dados do inglês para o português usando `googletrans`
- Exibição dos personagens em um template estilizado com Bootstrap
- Paginação dos resultados para melhor navegação
- Template com tema visual inspirado em Avatar

## 🔧 Tecnologias utilizadas

- Python 3.x
- Django
- Bootstrap 5
- [googletrans](https://pypi.org/project/googletrans/) (tradução automática)
- HTML/CSS
- API externa: [Last Airbender API](https://last-airbender-api.fly.dev/)

## 🚀 Como executar o projeto

1. **Clone o repositório**:
    ```
    bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. **Crie e ative um ambiente virtual**:
    ```
    python -m venv venv
    venv\Scripts\activate   # Windows
    source venv/bin/activate  # Linux/macOS
    ```

3. **Instale as dependências**:
    ```
    pip install -r requirements.txt
    ```

4. **Execute o servidor Django**:
    ```
    python manage.py runserver
    ```

5. **Acesse no navegador**:
    ```
    http://localhost:8000/api_avatar
    ```

## 📦 Estrutura dos dados

Cada personagem exibido contém:
    Nome traduzido
    Afiliação
    Lista de aliados
    Lista de inimigos
    (opcional) Imagem do personagem

## ✅ Próximas melhorias
    Salvar os dados em um banco de dados com modelo Django
    Filtros de busca e categorias
    Melhor responsividade mobile

## 📄 Licença
    Este projeto é apenas para fins educacionais. Avatar: A Lenda de Aang pertence à Nickelodeon/Paramount.

Feito com 💙 por Thiago Henrique no desafio #7DaysOfCode da Alura.