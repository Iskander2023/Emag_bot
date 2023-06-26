import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from bot.database.data import create_db
from bot.handlers import vl, vm
from handlers import start, help

async def main():
    create_db()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
                        )

    bot = Bot(token=os.getenv('token'))

    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.include_router(start.router)
    dp.include_router(help.router)
    dp.include_router(vl.router)
    dp.include_router(vm.router)



    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except(KeyboardInterrupt, SystemExit):
        print('Бот остановлен')