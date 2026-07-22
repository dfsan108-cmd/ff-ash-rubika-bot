import os
from flask import Flask
import rubika_bot

app = Flask(__name__)

@app.route("/")
def home():
    return "FFASHBot Online"

print(dir(rubika_bot))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
