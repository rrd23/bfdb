from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher()



router = Router()

@router.message(CommandStart())
async def start_command(message: types.Message):
    keyboard = InlineKeyboardBuilder()

    web_app_url = "https://myrrd.xyz"  # URL твоего Flask-приложения
    keyboard.button(text="Открыть WebApp", web_app=WebAppInfo(url=web_app_url))
    keyboard.adjust(1)

    await message.answer(
        "Нажмите на кнопку ниже, чтобы открыть WebApp.",
        reply_markup=keyboard.as_markup()
    )

dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
