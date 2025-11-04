import os
import telebot
from flask import Flask, request

# Токен берем из переменной окружения Render
BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

# Главная страница — проверка, что сервис жив
@app.route('/', methods=['GET'])
def index():
    return "Bot is alive!", 200

# Вебхук — сюда Telegram шлет обновления
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    json_data = request.get_json(force=True)
    update = telebot.types.Update.de_json(json_data)
    bot.process_new_updates([update])
    return '', 200

# === Команды бота ===
@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "✅ Привет! Бот запущен и работает на Render 🚀")

@bot.message_handler(func=lambda message: True)
def echo_handler(message):
    bot.send_message(message.chat.id, f"Ты написал: {message.text}")

# === Запуск Flask ===
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
