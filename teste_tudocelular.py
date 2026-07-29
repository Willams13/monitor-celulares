from playwright.sync_api import sync_playwright


url = "https://www.tudocelular.com/Samsung/precos/n10155/Samsung-Galaxy-S25-FE.html"


with sync_playwright() as p:

    navegador = p.chromium.launch(headless=True)

    pagina = navegador.new_page()

    pagina.goto(url, timeout=60000)

    texto = pagina.text_content("body")

    print(texto[:2000])

    navegador.close()
