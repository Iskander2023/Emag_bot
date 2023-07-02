from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot.database.machine_base import select_machines_by_model
from bot.keyboards.button_lists import e_d_list
from bot.states_class.bot_states import BotState


router = Router()

@router.message(
    BotState.choice_machine,
    F.text.in_(e_d_list)
)
async def answer_choice_machine(message: Message, state: FSMContext) -> None:
    await state.set_state(BotState.choice_machine)
    data = await state.update_data(model=message.text)
    result = await select_machines_by_model(**data)

    for row in result:
        image_data = row[0]
        caption = row[1]
        photo = types.BufferedInputFile(image_data, filename='image.jpg')
        if len(caption) > 1024:
            caption = caption[:1020] + "..."
        await message.answer_photo(photo, caption)

@router.message(BotState.choice_machine
                )
async def process_unknown_choice_machine(message: Message, state: FSMContext) -> None:
    await state.set_state(BotState.choice_machine)
    await message.answer(f"Станка {message.text} в списке нет. "
                         f"\nВыберите из предоставленого списка станков "
)
