import os
import time
from threading import Thread
from flask import Flask
from rubika import Bot

app = Flask(__name__)

TOKEN = os.environ.get("TOKEN")

if not TOKEN:
    raise Exception("TOKEN not found")

bot = Bot(TOKEN)


@app.route("/")
def home():
    return "FFASHBot Online"


def run_rubika():
    print("FFASHBot Started")

    @bot.on_message()
    def handler(message):
        try:
            text = message.text

            if text == "/start":
                bot.send_message(
                    message.chat_id,
                    "سلام 👋\n🎮 FFASHBot فعال شد"
                )

            elif text == "سلام":
                bot.send_message(
                    message.chat_id,
                    "سلام 👋\nخوش آمدی"
                )

            elif text == "تورنومنت":
                bot.send_message(
                    message.chat_id,
                    "🎮 FF ASH Tournament\nثبت‌نام به‌زودی..."
                )

        except Exception as e:
            print("ERROR:", e)

    bot.run()


if __name__ == "__main__":
    Thread(target=run_rubika).start()

    port = int(os.environ.get("PORT", 10000))

    app.run(
        host="0.0.0.0",
        port=port
    )
