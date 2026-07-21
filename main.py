from rubika import Bot

TOKEN = "BJJAIF0JEDWPSZVCWUOSLABHINYJFZWCQVZVEYJJLDRVMXGINJHGUJASVIFEUMUN"

bot = Bot(TOKEN)

@bot.on_message()
def start(bot, message):
    if message.text == "/start":
        bot.send_message(
            message.chat_id,
            "🎮 به ربات FF ASH Tournament خوش آمدید!"
        )

bot.run()
