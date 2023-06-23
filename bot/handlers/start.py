from aiogram import Router
from aiogram.filters.text import Text
from aiogram.types import Message
from aiogram.filters import Command
from bot.decorators.decorators import restricted
from bot.keyboards.button_lists import machines_list, start_keyboard_menu
from bot.keyboards.machine_keyboard import make_row_keyboard

router = Router()

@router.message(Command(commands=('start')))
@restricted()
async def cmd_start(message: Message):
    name = message.from_user.first_name
    user_id = message.from_user.id # юзер айди
    await message.answer(f"Добрый день {name}, выберите что Вас интересует:", reply_markup=make_row_keyboard(start_keyboard_menu))



@router.message(Text(text="Станки"))
@restricted()
async def answer_machine(message: Message):
    await message.answer(
        text="Спасибо. Теперь, пожалуйста, выберите станок:",
        reply_markup=make_row_keyboard(machines_list)
    )



