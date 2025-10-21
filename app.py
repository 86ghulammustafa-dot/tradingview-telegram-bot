from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ TradingView Telegram Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received:", data)
    return {"status": "ok"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
