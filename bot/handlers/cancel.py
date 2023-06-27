from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command, Text

from bot.keyboards.button_lists import start_keyboard_menu
from bot.keyboards.machine_keyboard import make_row_keyboard
from bot.states_class.user_class import UserState

router = Router()

@router.message(Command(commands=["cancel"]))
@router.message(Text(text="в меню =>>", ignore_case=True))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(UserState.start_state)
    await message.answer(
        text="Действие отменено",
        reply_markup=make_row_keyboard(start_keyboard_menu)
    )