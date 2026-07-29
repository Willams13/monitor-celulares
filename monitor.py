from config import TARGET_PRICE
from stores import buscar_precos
from telegram_bot import enviar_mensagem


try:
    produtos = buscar_precos()

except Exception as erro:

    enviar_mensagem(
        f"❌ Erro na busca:\n\n{erro}"
    )

    produtos = []


if not produtos:

    enviar_mensagem(
        "⚠️ Monitor executado.\n\nNenhuma oferta encontrada nesta verificação."
    )


for produto in produtos:

    nome = produto.get("nome", "Produto")
    preco = produto.get("preco", 0)
    loja = produto.get("loja", "Não informado")
    link = produto.get("link", "")


    if preco <= TARGET_PRICE:

        mensagem = f"""
🚨 PREÇO ALVO ATINGIDO! 🚨

📱 {nome}

💰 R$ {preco:.2f}

🎯 Limite: R$ {TARGET_PRICE}

🏪 {loja}

🔗 {link}
"""

    else:

        mensagem = f"""
🟡 Promoção encontrada!

📱 {nome}

💰 R$ {preco:.2f}

🎯 Preço alvo: R$ {TARGET_PRICE}

🏪 {loja}

🔗 {link}
"""


    enviar_mensagem(mensagem)
