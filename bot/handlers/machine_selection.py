from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot.keyboards.button_lists import machines_list_vl, list_of_emag_models, machines_list_vm, dekay_or_emag, \
    list_of_emag_models, list_of_dekay_models
from bot.keyboards.machine_keyboard import make_row_keyboard
from bot.states_class.user_class import BotState


router = Router()

@router.message(
    BotState.machine_selection,
    F.text.in_(dekay_or_emag)
)
async def machine_company_selection(message: Message, state: FSMContext) -> None:
    data = await state.update_data(company_choice=message.text)
    if message.text == "Dekay":
        await state.set_state(BotState.dekay)
        await message.answer(
            text="Спасибо. Теперь, пожалуйста, выберите интересующий Вас станок:",
            reply_markup=make_row_keyboard(list_of_dekay_models))
    elif message.text == "EMAG":
        await state.set_state(BotState.emag)
        await message.answer(
            text="Спасибо. Теперь, пожалуйста, выберите интересующий Вас станок:",
            reply_markup=make_row_keyboard(list_of_emag_models))

@router.message(
    BotState.emag,
    F.text.in_(list_of_emag_models)
)
async def answer_emag(message: Message, state: FSMContext) -> None:
    data = await state.update_data(line_name=message.text)
    if message.text == "VL":
        await state.set_state(BotState.vl_state)
        await message.answer(
            text="Спасибо. Теперь, пожалуйста, выберите интересующий Вас станок:",
            reply_markup=make_row_keyboard(machines_list_vl))
    elif message.text == "VM":
        await state.set_state(BotState.vm_state)
        await message.answer(
            text="Спасибо. Теперь, пожалуйста, выберите интересующий Вас станок:",
            reply_markup=make_row_keyboard(machines_list_vm))