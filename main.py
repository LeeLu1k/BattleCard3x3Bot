import os
from flask import Flask, request
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

# === Telegram webhook ===
@app.route(f"/{BOT_TOKEN}", methods=["POST", "GET"])
def webhook():
    if request.method == "POST":
        update = request.get_json()
        print(f"📩 Update received: {update}")
        bot.process_new_updates([telebot.types.Update.de_json(update)])
        return "OK", 200
    else:
        return "✅ Webhook is working!", 200


# === Простая проверка бота через браузер ===
@app.route("/", methods=["GET"])
def index():
    return "🤖 Bot is alive and ready! Try /start in Telegram.", 200


# === Тест-страница /start через браузер ===
@app.route("/start", methods=["GET"])
def start_test():
    return "✅ /start работает (через браузер)!", 200


# === Обработка команды /start в Telegram ===
@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "👋 Привет! Бот запущен и готов к работе!"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 10000)))
