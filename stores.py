import requests
from bs4 import BeautifulSoup


def buscar_precos():

    links = [
        "https://www.tudocelular.com/Samsung/fichas-tecnicas/n10155/Samsung-Galaxy-S25-FE.htm",
        "https://www.tudocelular.com/Poco/fichas-tecnicas/n10349/Poco-X8-Pro-Max.html"
    ]

    for link in links:

        resposta = requests.get(
            link,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=10
        )

        soup = BeautifulSoup(
            resposta.text,
            "html.parser"
        )

        texto = soup.get_text(
            " ",
            strip=True
        )

        print("LINK:", link)
        print(texto[:1000])
        print("------------------------")


    return []
