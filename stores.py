from duckduckgo_search import DDGS
import re


def buscar_precos():

    produtos = [
        "Samsung Galaxy S25 FE preço",
        "POCO X8 Pro Max preço"
    ]

    resultados = []


    for produto in produtos:

        with DDGS() as ddgs:

            pesquisas = ddgs.text(
                produto,
                max_results=5
            )


            for resultado in pesquisas:

                texto = resultado.get("title", "") + " " + resultado.get("body", "")

                precos = re.findall(
                    r"R\$ ?\d{1,4}(?:\.\d{3})?(?:,\d{2})?",
                    texto
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

                        "nome": produto.replace(" preço", ""),

                        "preco": float(preco),

                        "loja": resultado.get("title", "Loja encontrada"),

                        "link": resultado.get("href", "")

                    })

                    break


    return resultados
