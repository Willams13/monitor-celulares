import requests


def buscar_precos():

    produtos = [
        "Samsung Galaxy S25 FE",
        "POCO X8 Pro Max"
    ]

    resultados = []


    for produto in produtos:

        url = "https://api.mercadolibre.com/sites/MLB/search"

        parametros = {
            "q": produto,
            "limit": 5
        }


        resposta = requests.get(
            url,
            params=parametros,
            timeout=10
        )


        dados = resposta.json()


        for item in dados.get("results", []):

            resultados.append({

                "nome": item["title"],

                "preco": item["price"],

                "loja": "Mercado Livre",

                "link": item["permalink"]

            })


    return resultados
