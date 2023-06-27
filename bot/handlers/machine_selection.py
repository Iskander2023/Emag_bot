from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot.keyboards.button_lists import machines_list_vl, list_of_machine_models, machines_list_vm
from bot.keyboards.machine_keyboard import make_row_keyboard
from bot.states_class.user_class import UserState


router = Router()

@router.message(
    UserState.machine_selection,
    F.text.in_(list_of_machine_models)
)
async def answer_machine(message: Message, state: FSMContext) -> None:
    data = await state.update_data(line_name=message.text)
    if message.text == "VL":
        await state.set_state(UserState.vl_state)
        await message.answer(
            text="Спасибо. Теперь, пожалуйста, выберите интересующий Вас станок:",
            reply_markup=make_row_keyboard(machines_list_vl))
    elif message.text == "VM":
        await state.set_state(UserState.vm_state)
        await message.answer(
            text="Спасибо. Теперь, пожалуйста, выберите интересующий Вас станок:",
            reply_markup=make_row_keyboard(machines_list_vm))