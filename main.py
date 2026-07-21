import os
import time
from threading import Thread
from flask import Flask
import rubika
print(dir(rubika))
app = Flask(__name__)

@app.route("/")
def home():
    return "FFASHBot Online"

def run_rubika():
    print("Rubika bot starting...")
    while True:
        time.sleep(60)

if __name__ == "__main__":
    Thread(target=run_rubika).start()

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
