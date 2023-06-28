from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot.keyboards.button_lists import machines_list_vl, machines_list_vm, dekay_or_emag, \
    list_of_emag_models, list_of_dekay_models, machines_list_dekay_v, machines_list_dekay_y, list_of_models
from bot.keyboards.machine_keyboard import make_row_keyboard
from bot.states_class.user_class import BotState


router = Router()

@router.message(
    BotState.machine_selection,
    F.text.in_(dekay_or_emag)
)
async def machine_company_selection(message: Message, state: FSMContext) -> None:
    data = await state.update_data(company_choice=message.text)
    state_mapping = {
        "Dekay": (BotState.choice_line, list_of_dekay_models),
        "EMAG": (BotState.choice_line, list_of_emag_models)
    }
    if message.text in state_mapping:
        new_state, machine_list = state_mapping[message.text]
        await state.set_state(new_state)
        await message.answer(
            text="Спасибо. Теперь, пожалуйста, выберите модельный ряд станков:",
            reply_markup=make_row_keyboard(machine_list))

@router.message(
    BotState.choice_line,
    F.text.in_(list_of_models)
)
async def answer_emag(message: Message, state: FSMContext) -> None:
    data = await state.update_data(line_name=message.text)

    state_mapping = {
        "VL": (BotState.vl_state, machines_list_vl),
        "VM": (BotState.vm_state, machines_list_vm),
        "V": (BotState.dekay_state, machines_list_dekay_v),
        "Y": (BotState.dekay_state, machines_list_dekay_y)
    }

    if message.text in state_mapping:
        new_state, machine_list = state_mapping[message.text]
        await state.set_state(new_state)
        await message.answer(
            text="Спасибо. Теперь, пожалуйста, выберите интересующий Вас станок:",
            reply_markup=make_row_keyboard(machine_list))
    else:
        await message.answer("Неверный выбор.")