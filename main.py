import os
import time
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "FFASHBot Online"

def run_bot():
    while True:
        print("FFASHBot Online")
        time.sleep(60)

if __name__ == "__main__":
    from threading import Thread

    Thread(target=run_bot).start()

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
