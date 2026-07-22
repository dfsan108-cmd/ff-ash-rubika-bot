from flask import Flask, request
import os

app = Flask(__name__)

TOKEN = os.getenv("BOT_TOKEN")

print("Token Loaded:", TOKEN is not None)

players = []
from rubika_bot import Bot

bot = Bot(TOKEN)

@bot.on_message()
def handle_message(message):
    print("MESSAGE:", message)

    players.append({
        "message": message
    })
@app.route("/")
def home():
    return "FFASH Bot Online"

@app.route("/webhook", methods=["POST"])
def webhook():
    print("WEBHOOK CALLED")

    data = request.get_json()

    print("DATA:", data)

    if data:
        players.append(data)

    return "OK"

@app.route("/players")
def get_players():
    return {
        "تعداد": len(players),
        "بازیکنان": players
    }

if __name__ == "__main__":
    import threading

threading.Thread(target=bot.run).start()
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
