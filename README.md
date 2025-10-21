# === app.py ===
from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    if not data:
        return "No data", 400
    message = data.get('message', 'No message received')
    send_telegram(message)
    return "Sent", 200

def send_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
    requests.post(url, json=payload)

@app.route('/')
def index():
    return "TradingView Telegram Bot is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
