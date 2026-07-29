import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import quote


def buscar_precos():

    produtos = [
        "Samsung Galaxy S25 FE preço",
        "POCO X8 Pro Max preço"
    ]

    resultados = []

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for produto in produtos:

        url = "https://www.google.com/search?q=" + quote(produto)

        resposta = requests.get(
            url,
            headers=headers,
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


        precos = re.findall(
            r"R\$ ?\d{1,4}(?:\.\d{3})?(?:,\d{2})?",
            texto
        )


        print(texto[:1000])
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

                "nome": produto.replace(" preço", ""),

                "preco": float(preco),

                "loja": "Pesquisa Google",

                "link": url

            })


    return resultados
