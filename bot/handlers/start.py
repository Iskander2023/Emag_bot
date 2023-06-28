from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from bot.functions.func import is_user_allowed
from bot.keyboards.button_lists import start_keyboard_menu, \
                                       about_the_company, dekay_or_emag
from bot.keyboards.machine_keyboard import make_row_keyboard
from bot.states_class.user_class import BotState

router = Router()

@router.message(Command(commands=('start')))
async def cmd_start(message: Message, state: FSMContext) -> None:
    name = message.from_user.first_name
    user_id = message.from_user.id # юзер айди
    if is_user_allowed(user_id) is False:
        await message.reply(f"{name} у вас нет доступа к этой команде.")
        return
    else:
        await state.set_state(BotState.start_state)
        await message.answer(f"Добрый день {name}, выберите что Вас интересует:", reply_markup=make_row_keyboard(start_keyboard_menu))


@router.message(
    BotState.start_state,
    F.text.in_(start_keyboard_menu)
)
async def menu_command_selection (message: Message, state: FSMContext):
    if message.text == "Станки":
        await state.set_state(BotState.machine_selection)
        await message.answer(
            text="Спасибо. Теперь, пожалуйста, выберите станок нужной Вам фирмы:",
            reply_markup=make_row_keyboard(dekay_or_emag))
    elif message.text == "О нас":
        await state.set_state(BotState.about_us)
        await message.answer(
            text="Спасибо. Теперь, пожалуйста, выберите что вас интересует:",
            reply_markup=make_row_keyboard(about_the_company))


