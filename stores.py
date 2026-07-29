import requests


def buscar_precos():

    url = "https://api.mercadolibre.com/sites/MLB/search"

    parametros = {
        "q": "Samsung Galaxy S25 FE",
        "limit": 5
    }

    resposta = requests.get(
        url,
        params=parametros,
        timeout=10
    )

    print("Status:", resposta.status_code)
    print("Resposta:", resposta.text[:500])

    return []
