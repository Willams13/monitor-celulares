import requests


def buscar_precos():

    url = "https://api.mercadolibre.com/sites/MLB/search"

    params = {
        "q": "celular samsung",
        "limit": 3
    }

    resposta = requests.get(
        url,
        params=params,
        timeout=10
    )

    print("Status:", resposta.status_code)
    print("Resposta:", resposta.text[:1000])

    return []
