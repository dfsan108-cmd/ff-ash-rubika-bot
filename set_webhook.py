import os
import requests

TOKEN = os.getenv("BOT_TOKEN")

url = f"https://botapi.rubika.ir/v3/{TOKEN}/updateBotEndpoint"

data = {
    "url": "https://ff-ash-rubika-bot-2.onrender.com/webhook"
}

response = requests.post(
    url,
    headers={"Content-Type": "application/json"},
    json=data
)

print(response.status_code)
print(response.text)
