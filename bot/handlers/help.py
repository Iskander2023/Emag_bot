from aiogram import Router
from aiogram.filters.text import Text
from aiogram.types import Message
from aiogram.filters import Command
router = Router()


@router.message(Command(commands=('help')))
async def cmd_help(message: Message):
    await message.answer(
        " помощь и подсказка по работе бота"

    )
