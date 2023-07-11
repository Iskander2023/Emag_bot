from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot.database.machine_base import select_details
from bot.keyboards.button_lists import details_list
from bot.states_class.bot_states import BotState


router = Router()

@router.message(
    BotState.details_choice,
    F.text.in_(details_list)
)
async def answer_choice_details(message: Message, state: FSMContext) -> None:
    await state.set_state(BotState.details_choice)
    data = await state.update_data(name=message.text)
    result = await select_details(**data)

    for row in result:
        image_data = row[0]
        caption = row[1]
        photo = types.BufferedInputFile(image_data, filename='image.jpg')
        if len(caption) > 1024:
            caption = caption[:1020] + "..."
        await message.answer_photo(photo, caption)

@router.message(BotState.details_choice
                )
async def process_unknown_choice_details(message: Message, state: FSMContext) -> None:
    await state.set_state(BotState.details_choice)
    await message.answer(f"Детали {message.text} в списке нет. "
                         f"\nВыберите из предоставленого списка деталей "
)