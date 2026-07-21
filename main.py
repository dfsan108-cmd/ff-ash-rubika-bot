import os
import time
from threading import Thread
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "FFASHBot Online"

def run_bot():
    print("FFASHBot Ready")
    while True:
        time.sleep(60)

if __name__ == "__main__":
    Thread(target=run_bot).start()

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
