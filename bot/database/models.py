import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "db.sqlite3")

def connect():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = connect()
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (chat_id TEXT PRIMARY KEY)")
    c.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY AUTOINCREMENT, chat_id TEXT, kode TEXT, user_id TEXT, status TEXT)")
    conn.commit()
    conn.close()

def save_user(chat_id):
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users (chat_id) VALUES (?)", (chat_id,))
    conn.commit()
    conn.close()

def save_order(chat_id, kode, user_id):
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO orders (chat_id, kode, user_id, status) VALUES (?, ?, ?, 'pending')", (chat_id, kode, user_id))
    conn.commit()
    conn.close()

init_db()
