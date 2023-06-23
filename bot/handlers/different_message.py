from aiogram import Router
from aiogram.types import Message
from aiogram import F
from bot.decorators.decorators import restricted

router = Router()

@router.message(F.text)
@restricted()
async def message_with_text(message: Message):
    await message.answer("Выберите что вас интересует из предоставленого списка!")


@router.message(F.sticker)
@restricted()
async def message_with_sticker(message: Message):
    await message.answer("Выберите что вас интересует из предоставленого списка")


@router.message(F.animation)
@restricted()
async def message_with_gif(message: Message):
    await message.answer("Выберите что вас интересует из предоставленого списка")