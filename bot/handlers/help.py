from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()

@router.message(Command(commands=('help')))
async def cmd_help(message: Message):
    await message.answer(
        "Бот создан для лучшего представления о деятельности фирмы ЭМАГ, наших станках, проектах и изготовленых на станках деталях."

    )
