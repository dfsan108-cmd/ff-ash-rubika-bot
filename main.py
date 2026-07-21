import requests
import time

TOKEN = "BJJAIF0JEDWPSZVCWUOSLABHINYJFZWCQVZVEYJJLDRVMXGINJHGUJASVIFEUMUN"

def send_message(chat_id, text):
    url = f"https://botapi.rubika.ir/v3/{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": chat_id,
        "text": text
    })

offset = 0

while True:
    url = f"https://botapi.rubika.ir/v3/{TOKEN}/getUpdates"
    r = requests.get(url, params={"offset": offset})
print(r.text)
data = r.json()

    for update in data.get("data", {}).get("updates", []):
        offset = update["update_id"] + 1

        message = update.get("message")
        if message:
            text = message.get("text")
            chat_id = message["chat_id"]

            if text == "/start":
                send_message(
                    chat_id,
                    "🎮 سلام\nبه ربات FF ASH Tournament خوش آمدید!"
                )

    time.sleep(2)
