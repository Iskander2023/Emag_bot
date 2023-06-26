from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from bot.functions_to_work.func import is_user_allowed
from bot.keyboards.button_lists import start_keyboard_menu, list_of_machine_models
from bot.keyboards.machine_keyboard import make_row_keyboard
from bot.states_class.user_class import UserState

router = Router()

@router.message(Command(commands=('start')))
async def cmd_start(message: Message, state: FSMContext) -> None:
    name = message.from_user.first_name
    user_id = message.from_user.id # юзер айди
    if is_user_allowed(user_id) is False:
        await message.reply(f"{name} у вас нет доступа к этой команде.")
        return
    else:
        await state.set_state(UserState.start_state)
        await message.answer(f"Добрый день {name}, выберите что Вас интересует:", reply_markup=make_row_keyboard(start_keyboard_menu))


@router.message(UserState.start_state,
                F.text.casefold() == "станки") # указываем "слово" именно с маленькой буквы, casefold приводит текст к нижнему регистру
async def answer_machine(message: Message, state: FSMContext) -> None:
    await state.set_state(UserState.machine_selection)
    await message.answer(
        text="Спасибо. Теперь, пожалуйста, выберите модельный ряд станков:",
        reply_markup=make_row_keyboard(list_of_machine_models))






