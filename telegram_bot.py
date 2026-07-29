import requests
import os


TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def enviar_mensagem(texto):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    dados = {
        "chat_id": CHAT_ID,
        "text": texto
    }

    requests.post(url, json=dados)
