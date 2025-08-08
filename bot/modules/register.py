from utils.whatsapp_api import send_message
from database.models import save_user

def handle(chat_id):
    save_user(chat_id)
    return send_message(chat_id, "✅ Pendaftaran berhasil. Ketik *produk* untuk melihat daftar game.")
  
