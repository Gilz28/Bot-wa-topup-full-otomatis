import requests
from config import CHAT_API_URL, CHAT_API_TOKEN

def get_messages():
    url = f"{CHAT_API_URL}/messages?token={CHAT_API_TOKEN}"
    res = requests.get(url).json()
    return res.get("messages", [])

def send_message(chat_id, text):
    url = f"{CHAT_API_URL}/sendMessage?token={CHAT_API_TOKEN}"
    data = {"chatId": chat_id, "body": text}
    return requests.post(url, json=data).json()
