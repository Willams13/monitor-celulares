from config import TARGET_PRICE
from stores import buscar_precos
from telegram_bot import enviar_mensagem


produtos = buscar_precos()


for produto in produtos:

    nome = produto["nome"]
    preco = produto["preco"]
    loja = produto["loja"]
    link = produto["link"]


    if preco <= TARGET_PRICE:

        mensagem = f"""
🚨 PREÇO ALVO ATINGIDO! 🚨

📱 {nome}

💰 R$ {preco}

🎯 Seu limite: R$ {TARGET_PRICE}

🏪 {loja}

🔗 {link}
"""

    else:

        mensagem = f"""
🟡 Promoção encontrada!

📱 {nome}

💰 R$ {preco}

🎯 Preço alvo: R$ {TARGET_PRICE}

🏪 {loja}

🔗 {link}
"""


    enviar_mensagem(mensagem)
