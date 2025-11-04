import os
import telebot
from flask import Flask, request

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "🤖 Bot is alive and ready! Try /start in Telegram."

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    json_update = request.get_json(force=True)
    print("📩 Update received:", json_update, flush=True)
    update = telebot.types.Update.de_json(json_update)
    bot.process_new_updates([update])
    return "ok", 200

@bot.message_handler(commands=["start"])
def start_message(message):
    print(f"➡️ /start received from: @{message.from_user.username} (id={message.chat.id})", flush=True)
    bot.reply_to(message, "👋 Привет! Бот успешно запущен и работает на Render!")
    print(f"✅ Reply sent to: @{message.from_user.username}", flush=True)

if __name__ == "__main__":
    # Webhook only — polling не нужен
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
