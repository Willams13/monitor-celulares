import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import quote


def buscar_precos():

    produtos = [
        "Samsung Galaxy S25 FE",
        "POCO X8 Pro Max"
    ]

    resultados = []

    for produto in produtos:

        url = "https://www.google.com/search?tbm=shop&q=" + quote(produto)

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        resposta = requests.get(url, headers=headers)

        soup = BeautifulSoup(resposta.text, "lxml")


        textos = soup.get_text(" ", strip=True)

        precos = re.findall(
            r"R\$ ?\d{1,4}(?:\.\d{3})?,?\d{0,2}",
            textos
        )


        if precos:

            preco_texto = precos[0]

            preco = (
                preco_texto
                .replace("R$", "")
                .replace(".", "")
                .replace(",", ".")
                .strip()
            )

            resultados.append({
                "nome": produto,
                "preco": float(preco),
                "loja": "Google Shopping",
                "link": url
            })


    return resultados
