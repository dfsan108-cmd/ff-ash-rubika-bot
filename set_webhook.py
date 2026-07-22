import os
import requests

TOKEN = os.getenv("BOT_TOKEN")

url = f"https://botapi.rubika.ir/v3/{TOKEN}/updateBotEndpoint"

data = {
    "url": "https://ff-ash-rubika-bot.onrender.com/webhook"
}

response = requests.post(url, json=data)

print(response.text)
