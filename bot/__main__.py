import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from bot.handlers import vl2, vl4
from handlers import start, help

async def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
                        )
    dp = Dispatcher()
    bot = Bot(token=os.getenv('token'))
    dp.include_router(start.router)
    dp.include_router(help.router)
    dp.include_router(vl2.router)
    dp.include_router(vl4.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except(KeyboardInterrupt, SystemExit):
        print('Бот остановлен')