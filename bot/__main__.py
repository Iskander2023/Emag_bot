import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from bot.database.contact_database import create_employees_table
from bot.database.machine_base import create_db
from bot.handlers import vl, vm, contacts, machine_selection, cancel
from handlers import start, help

async def main():
    create_db()
    create_employees_table()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
                        )

    bot = Bot(token=os.getenv('token'))

    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.include_router(start.router)
    dp.include_router(cancel.router)
    dp.include_router(help.router)
    dp.include_router(vl.router)
    dp.include_router(vm.router)
    dp.include_router(contacts.router)
    dp.include_router(machine_selection.router)



    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except(KeyboardInterrupt, SystemExit):
        print('Бот остановлен')