from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot.keyboards.button_lists import machines_list_vl, machines_list_vm, dekay_or_emag, \
    list_of_emag_models, list_of_dekay_models, machines_list_dekay_v, machines_list_dekay_y, list_of_models
from bot.keyboards.machine_keyboard import make_row_keyboard
from bot.states_class.bot_states import BotState


router = Router()

@router.message(
    BotState.machine_selection,
    F.text.in_(dekay_or_emag)
)
async def machine_company_selection(message: Message, state: FSMContext) -> None:
    #data = await state.update_data(company_name=message.text)
    state_mapping = {
        "Dekay": (BotState.choice_line, list_of_dekay_models),
        "EMAG": (BotState.choice_line, list_of_emag_models)
    }
    if message.text in state_mapping:
        new_state, model_list = state_mapping[message.text]
        await state.set_state(new_state)
        await message.answer(
            text="Выберите модельный ряд станков:",
            reply_markup=make_row_keyboard(model_list))
@router.message(BotState.machine_selection
                )
async def process_unknown_machine_selection(message: Message, state: FSMContext) -> None:
    await state.set_state(BotState.machine_selection)
    await message.answer(f"Модельного ряда {message.text} в списке нет. "
                         f"\nВыберите линейку из предосталенных"
                         )

@router.message(
    BotState.choice_line,
    F.text.in_(list_of_models)
)
async def answer_emag(message: Message, state: FSMContext) -> None:
    #data = await state.update_data(line_name=message.text)

    state_mapping = {
        "VL": (BotState.choice_machine, machines_list_vl),
        "VM": (BotState.choice_machine, machines_list_vm),
        "V": (BotState.choice_machine, machines_list_dekay_v),
        "Y": (BotState.choice_machine, machines_list_dekay_y)
    }

    if message.text in state_mapping:
        new_state, machine_type_list = state_mapping[message.text]
        await state.set_state(new_state)
        await message.answer(
            text="Выберите интересующий Вас станок:",
            reply_markup=make_row_keyboard(machine_type_list))

@router.message(BotState.choice_line
                )
async def process_unknown_choice_line(message: Message, state: FSMContext) -> None:
    await state.set_state(BotState.choice_line)
    await message.answer(f"Станка модели {message.text} в списке нет. "
                         f"\nВыберите модель станка из предосталенных"
                         )