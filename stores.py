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

        url = "https://www.google.com/search?q=" + quote(produto + " preço")

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        resposta = requests.get(url, headers=headers)

        soup = BeautifulSoup(resposta.text, "html.parser")

        texto = soup.get_text(" ", strip=True)

        print("Produto pesquisado:", produto)
        print("Texto recebido:", texto[:300])


        precos = re.findall(
            r"R\$ ?\d{1,4}(?:\.\d{3})?(?:,\d{2})?",
            texto
        )


        print("Preços encontrados:", precos)


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
                "loja": "Pesquisa",
                "link": url
            })


    print("Total de ofertas:", len(resultados))

    return resultados
