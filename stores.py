from duckduckgo_search import DDGS


def buscar_precos():

    resultados = []

    with DDGS() as ddgs:

        pesquisa = ddgs.text(
            "Samsung Galaxy S25 FE preço Brasil",
            max_results=5
        )

        for item in pesquisa:

            resultados.append({
                "nome": item["title"],
                "preco": 9999,
                "loja": "Teste",
                "link": item["href"]
            })


    return resultados
