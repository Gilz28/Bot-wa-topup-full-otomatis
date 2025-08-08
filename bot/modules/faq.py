from utils.whatsapp_api import send_message

def handle(chat_id):
    return send_message(chat_id, """ℹ️ *FAQ / Bantuan:*
1. Ketik *daftar* untuk registrasi
2. Ketik *produk* untuk lihat produk game
3. Ketik *pesan [kode] [user_id]* untuk pesan
4. Ketik *bayar* untuk dapatkan QRIS
5. Ketik *faq* untuk bantuan""")
  
