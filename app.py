from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route('/')
def home():
    return "TradingView Telegram Bot is running!"

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    message = data.get('message', 'No message received')
    if BOT_TOKEN and CHAT_ID:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message}
        requests.post(url, json=payload)
    return "Alert sent", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
