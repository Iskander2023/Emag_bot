from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot.keyboards.button_lists import  part_type, \
                                        oil_production_details, mechanical_engineering_details, parts_list, coupling, \
                                        pipe_thread, bearings, hub
from bot.keyboards.machine_keyboard import make_row_keyboard
from bot.states_class.bot_states import BotState


router = Router()

@router.message(
    BotState.choice_of_direction,
    F.text.in_(part_type)
)
async def part_type_selection(message: Message, state: FSMContext) -> None:

    state_mapping = {
        "Нефтедобдыча": (BotState.part_selection, oil_production_details),
        "Машиностроение": (BotState.part_selection, mechanical_engineering_details)
    }
    if message.text in state_mapping:
        new_state, direction_list = state_mapping[message.text]
        await state.set_state(new_state)
        await message.answer(
            text="Выберите тип деталей:",
            reply_markup=make_row_keyboard(direction_list))



@router.message(BotState.choice_of_direction
                )
async def process_unknown_type_selection(message: Message, state: FSMContext) -> None:
    await state.set_state(BotState.choice_of_direction)
    await message.answer(f"Направления {message.text} в списке нет. "
                         f"\nВыберите направление из предоставленных"
                         )
@router.message(
    BotState.part_selection,
    F.text.in_(parts_list)
)
async def answer_part_selection(message: Message, state: FSMContext) -> None:
    data = await state.update_data(type=message.text)
    state_mapping = {
        "Муфта": (BotState.details_choice, coupling),
        "Трубы": (BotState.details_choice, pipe_thread),
        "Подшипники": (BotState.details_choice, bearings),
        "Ступицы": (BotState.details_choice, hub)
    }

    if message.text in state_mapping:
        new_state, part_type_list = state_mapping[message.text]
        await state.set_state(new_state)
        await message.answer(
            text="Выберите интересующие Вас вид деталей:",
            reply_markup=make_row_keyboard(part_type_list))


@router.message(BotState.part_selection
                )
async def process_unknown_part_selection(message: Message, state: FSMContext) -> None:
    await state.set_state(BotState.part_selection)
    await message.answer(f"Детали {message.text} в списке нет. "
                         f"\nВыберите деталь из предоставленных"
                         )