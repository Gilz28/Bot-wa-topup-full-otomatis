# Bot-wa-topup-full-otomatis
Ini adalah bot topup WhatsApp, full otomatis qris, intregasi dengan pg Qiospay dan api Requime, credit Gilz28
# Struktur Folder
📁 /wa-topup-bot/
├── bot/
│   ├── main.py
│   ├── config.py
│   ├── database/
│   ├── modules/
│   ├── templates/
│   └── utils/
├── requirements.txt
├── Procfile
# isi requirements.txt
requests
# Isi Procfile
worker: python bot/main.py
# buka terminal
cd path/ke/folder/wa-topup-bot
git init
git remote add origin https://github.com/Gilz28/Bot-wa-topup-full-otomatis.git
git add .
git commit -m "Upload full bot WhatsApp topup"
git push -u origin master
# Pterodactyl Setup
1.Masuk panel → Create server baru
2.Pilih egg: Python
3.Masukkan repo GitHub: https://github.com/Gilz28/Bot-wa-topup-full-otomatis.git
4.Start command: python bot/main.py
5.Jalankan server
# Konfigurasi Lingkungan
• API KEY Requime
• Merchant & API Key Qiospay
• Token Chat-API
