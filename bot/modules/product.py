import requests
from utils.whatsapp_api import send_message
from config import REQUIME_API_KEY

def handle(chat_id):
    url = f"https://api.requime.com/product?api_key={REQUIME_API_KEY}"
    res = requests.get(url).json()

    if res["status"] != "success":
        return send_message(chat_id, "Gagal mengambil produk.")

    msg = "*🎮 Daftar Produk Game:*\n\n"
    for p in res["data"][:10]:  # Batasi 10 produk dulu
        msg += f"• {p['brand']} ({p['code']}) - {p['name']}\n"

    msg += "\nKetik: *pesan [kode] [user_id]*\nContoh: pesan ML001 123456789"
    return send_message(chat_id, msg)
