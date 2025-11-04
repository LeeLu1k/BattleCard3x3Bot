from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

TOKEN = os.getenv("BOT_TOKEN")  # или просто "вставь токен сюда" для теста

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# 👇 твоя ссылка на web-app
WEB_APP_URL = "https://worker-production-173e.up.railway.app/"

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    web_app_button = types.KeyboardButton(
        text="🎮 Открыть игру", web_app=types.WebAppInfo(url=WEB_APP_URL)
    )
    keyboard.add(web_app_button)
    await message.answer("Привет! Нажми кнопку, чтобы открыть игру 👇", reply_markup=keyboard)


@dp.message_handler(commands=['play'])
async def play(message: types.Message):
    # Альтернативная версия через inline кнопку
    keyboard = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(
        text="🎮 Играть сейчас", web_app=types.WebAppInfo(url=WEB_APP_URL)
    )
    keyboard.add(btn)
    await message.answer("Готов к битве? 😎", reply_markup=keyboard)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
