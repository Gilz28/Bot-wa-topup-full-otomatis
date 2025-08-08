import time
import requests
from utils.whatsapp_api import get_messages, send_message
from modules import register, product, order, payment, faq

def handle_message(message):
    chat_id = message["chatId"]
    text = message["body"].strip().lower()

    if "daftar" in text:
        return register.handle(chat_id)
    elif "produk" in text or "game" in text:
        return product.handle(chat_id)
    elif "pesan" in text:
        return order.handle(chat_id, text)
    elif "bayar" in text:
        return payment.handle(chat_id)
    elif "faq" in text or "bantuan" in text:
        return faq.handle(chat_id)
    else:
        return send_message(chat_id, "Halo! Ketik *daftar*, *produk*, *pesan*, *bayar*, atau *faq* untuk memulai.")

def run():
    print("🤖 Bot berjalan...")
    last_seen = None

    while True:
        messages = get_messages()
        for msg in messages:
            if msg["_id"] != last_seen:
                handle_message(msg)
                last_seen = msg["_id"]
        time.sleep(3)

if __name__ == "__main__":
    run()
