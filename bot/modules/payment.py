from utils.whatsapp_api import send_message
from config import QIOSPAY_MERCHANT_CODE, QIOSPAY_API_KEY
import random

def handle(chat_id):
    nominal = random.randint(10000, 20000)
    qris_url = f"https://qiospay.id/qris?nominal={nominal}&merchant={QIOSPAY_MERCHANT_CODE}&apikey={QIOSPAY_API_KEY}"
    return send_message(chat_id, f"💳 Silakan bayar {nominal} ke QRIS berikut:\n{qris_url}\n\nSetelah transfer, ketik: *konfirmasi*")
  
