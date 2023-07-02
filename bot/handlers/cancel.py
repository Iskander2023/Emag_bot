from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command, Text

from bot.keyboards.button_lists import start_keyboard_menu
from bot.keyboards.machine_keyboard import make_row_keyboard
from bot.states_class.bot_states import BotState

router = Router()

@router.message(Command(commands=["cancel"]))
@router.message(Text(text="в меню =>>", ignore_case=True))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(BotState.start_state)
    await message.answer(
        text="Вы в главном меню",
        reply_markup=make_row_keyboard(start_keyboard_menu)
    )