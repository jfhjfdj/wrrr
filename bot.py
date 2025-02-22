import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.enums import ParseMode

TOKEN = "8117577175:AAG3mc5GjWYAnIqkdMfGw4yCOf0W6xHy3cI"

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Обычная (Reply) клавиатура
main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.add(KeyboardButton("сталкер 2"), KeyboardButton("я обязательно выйду"))

# Инлайн (Inline) клавиатура
inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Перейти на сайт", url="https://www.stalker2.com/ru")],
    [InlineKeyboardButton(text="нажми сюда", callback_data="button_click")]
])

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет!", reply_markup=main_keyboard)

@dp.message(lambda message: message.text == "гог")
async def hello(message: types.Message):
    await message.answer("Привет!", reply_markup=inline_keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())