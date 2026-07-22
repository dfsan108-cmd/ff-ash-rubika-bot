from flask import Flask, request
import os

app = Flask(__name__)

players = []

@app.route("/")
def home():
    return "FFASH Bot Online"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    print("NEW UPDATE:", data)

    players.append(data)

    return {"status": "ok"}

@app.route("/players")
def show_players():
    return {"count": len(players), "players": players}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
