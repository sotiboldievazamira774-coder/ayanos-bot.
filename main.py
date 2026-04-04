from dotenv import load_dotenv
import telebot 
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = 5221838264

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id == OWNER_ID:
        bot.send_message(message.chat.id, "👑 AYANOS: Хозяин, я запущен 24/7!")
    else:
        bot.send_message(message.chat.id, "🤖 Привет! Я AYANOS")

@bot.message_handler(commands=['ping'])
def ping(message):
    bot.reply_to(message, "🏓 Я жив!")

@bot.message_handler(func=lambda message: True)
def handle(message):
    bot.send_message(message.chat.id, f"🧠 {message.text}")

bot.infinity_polling()
