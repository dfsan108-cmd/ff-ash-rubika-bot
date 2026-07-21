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

    print("STATUS:", r.status_code)
    print("TEXT:", r.text)

    time.sleep(10)

        
