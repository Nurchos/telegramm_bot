import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import random
from dotenv import dotenv_values
import logging

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()
Names = ("Tokito", "Xan", "Alex", "Hamura", "2Pac", "Ronaldo")

@dp.message(Command('start'))
async def start_handler(message):
    name = message.from_user.first_name
    await message.answer(f"Hi,{name}")


@dp.message(Command('myinfo'))
async def myinfo_handler(message: types.Message):
    user = message.from_user
    user_id = user.id
    first_name = user.first_name
    username = user.username
    response = (
        f"Ваш ID: {user_id}\n"
        f"Ваше имя: {first_name}\n"
        f"Ваш username: @{username if username else 'не указан'}")
    await message.answer(response)


@dp.message(Command('random'))
async def random_name_handler(message: types.Message):
    random_name = random.choice(Names)
    await message.answer(f"рандомное имя: {random_name}")


@dp.message()
async def echo_handler(message: types.Message):
    await message.answer("Hi bro!Попробуй вбить: /start, /myinfo, /random")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
