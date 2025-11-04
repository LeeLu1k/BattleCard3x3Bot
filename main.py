import os
import telebot
from flask import Flask, request

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Bot is running!", 200

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    json_data = request.get_json(force=True)
    bot.process_new_updates([telebot.types.Update.de_json(json_data)])
    return '', 200

# === HANDLERS ===
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Привет! Бот успешно запущен на Render 🚀")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"Ты написал: {message.text}")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
