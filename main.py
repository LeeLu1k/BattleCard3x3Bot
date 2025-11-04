from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from flask import Flask, send_from_directory
from threading import Thread
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
app = Flask(__name__)

# --- Telegram Bot ---
WEB_APP_URL = "https://proud-quietude.up.railway.app"

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    web_app_btn = types.KeyboardButton(
        text="🎮 Открыть игру", web_app=types.WebAppInfo(url=WEB_APP_URL)
    )
    keyboard.add(web_app_btn)
    await message.answer("Привет! Готов сыграть? 👇", reply_markup=keyboard)

@dp.message_handler(commands=['menu'])
async def menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton(
        text="🎮 Открыть игру",
        web_app=types.WebAppInfo(url="https://<твой-проект>.up.railway.app/")
    )
    keyboard.add(btn)
    await message.answer("Выбери действие:", reply_markup=keyboard)

# --- Flask WebApp ---
@app.route('/')
def index():
    return send_from_directory('webapp', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('webapp', path)

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# --- Запуск ---
if __name__ == "__main__":
    Thread(target=run_flask).start()
    executor.start_polling(dp, skip_updates=True)
