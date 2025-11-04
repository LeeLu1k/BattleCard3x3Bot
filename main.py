import os
import telebot
from flask import Flask, request

# --- Настройки ---
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден в переменных окружения")

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

# --- Обработчик команды /start ---
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "👋 Привет! Бот работает и отвечает через Render!")

# --- Webhook обработчик ---
@app.route(f"/{BOT_TOKEN}", methods=['POST'])
def webhook():
    update = request.get_data().decode("utf-8")
    bot.process_new_updates([telebot.types.Update.de_json(update)])
    return "OK", 200

# --- Проверка что бот жив ---
@app.route("/", methods=['GET'])
def index():
    return "🤖 Bot is alive and ready! Try /start in Telegram.", 200

# --- Запуск ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
