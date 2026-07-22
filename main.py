from flask import Flask, request
import os

app = Flask(__name__)

TOKEN = os.getenv("BOT_TOKEN")

print("Token Loaded:", TOKEN is not None)

players = []

@app.route("/")
def home():
    return "FFASH Bot Online"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    print("NEW UPDATE:", data)

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
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
