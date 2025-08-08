from utils.whatsapp_api import send_message
from database.models import save_order

def handle(chat_id, text):
    try:
        _, kode, user_id = text.split()
        save_order(chat_id, kode, user_id)
        return send_message(chat_id, f"📝 Pesanan dengan kode *{kode}* untuk ID *{user_id}* dicatat. Ketik *bayar* untuk lanjut.")
    except:
        return send_message(chat_id, "❌ Format salah. Ketik: *pesan [kode] [user_id]*")
