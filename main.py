from rubika import Bot

TOKEN = "BJJAIF0JEDWPSZVCWUOSLABHINYJFZWCQVZVEYJJLDRVMXGINJHGUJASVIFEUMUN"

bot = Bot(TOKEN)

@bot.on_message()
def handler(bot, message):
    if message.text == "/start":
        bot.send_message(
            message.chat_id,
            "🎮 سلام\nبه ربات FF ASH Tournament خوش آمدید"
        )

bot.run()
