from rubika_bot import Bot

TOKEN = "BJJAIF0JEDWPSZVCWUOSLABHINYJFZWCQVZVEYJJLDRVMXGINJHGUJASVIFEUMUN"

bot = Bot(TOKEN)

@bot.on_message()
def answer(message):
    bot.send_message(
        message.chat_id,
        "سلام 👋\nFFASHBot روشن است 🎮"
    )

print("FFASHBot Online")

bot.run()
