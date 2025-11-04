import os
from flask import Flask, request
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
RENDER_EXTERNAL_URL = os.getenv("RENDER_EXTERNAL_URL")

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

# Простой маршрут для проверки
@app.route('/')
def index():
    return "Bot is running!", 200

# Обработка обновлений от Telegram
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

# Установка webhook при старте
@app.before_first_request
def set_webhook():
    webhook_url = f"{RENDER_EXTERNAL_URL}/{BOT_TOKEN}"
    bot.remove_webhook()
    bot.set_webhook(url=webhook_url)
    print(f"✅ Webhook set to {webhook_url}")

# Обработчики команд
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Бот успешно запущен на Render 🚀")

# Flask приложение должно слушать порт из окружения
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
