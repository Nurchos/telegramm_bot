import asyncio
import logging
from handlers.start import start_router
from handlers.other_messages import other_router
from config_bot import bot, dp
from handlers.my_info import my_info_router
from handlers.random_name import random_name_router


async def main():
    dp.include_router(start_router)
    dp.include_router(my_info_router)
    dp.include_router(random_name_router)
    dp.include_router(other_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
