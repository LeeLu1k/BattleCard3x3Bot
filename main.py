import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
import os

# === 1. Настройки ===
BOT_TOKEN = os.getenv("BOT_TOKEN") or "8439963996:AAG5rNpBrPdBZTB5iaMCLNtCn8wSD_Ozdpc"  # 👈 заменишь или задашь в Render Variables

bot = telebot.TeleBot(BOT_TOKEN)

# === 2. Команда /start ===
@bot.message_handler(commands=['start'])
def start(message):
    web_app = WebAppInfo(url="https://your-app-name.onrender.com/index.html")  # 👈 заменишь на свой Render URL
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton(text="🎮 Играть", web_app=web_app))
    bot.send_message(message.chat.id, "Привет! Готов к битве 3×3? ⚔️", reply_markup=kb)

# === 3. Запуск ===
print("✅ Бот запущен!")
bot.infinity_polling()
