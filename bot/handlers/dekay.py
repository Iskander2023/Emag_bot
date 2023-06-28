from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot.database.machine_base import select_machines_by_line_and_model
from bot.keyboards.button_lists import list_of_dekay_models, machines_list_dekay_v, machines_list_dekay_y
from bot.states_class.user_class import BotState


router = Router()

@router.message(
    BotState.dekay_state,
    F.text.in_(machines_list_dekay_v)
)
async def answer_dekay_v(message: Message, state: FSMContext) -> None:
    await state.set_state(BotState.dekay_state)
    data = await state.update_data(model=message.text)
    result = await select_machines_by_line_and_model(**data)

    for row in result:
        image_data = row[0]
        caption = row[1]
        photo = types.BufferedInputFile(image_data, filename='image.jpg')
        if len(caption) > 1024:
            caption = caption[:1020] + "..."
        await message.answer_photo(photo, caption)

@router.message(
    BotState.dekay_state,
    F.text.in_(machines_list_dekay_y)
)
async def answer_dekay_v(message: Message, state: FSMContext) -> None:
    await state.set_state(BotState.dekay_state)
    data = await state.update_data(model=message.text)
    result = await select_machines_by_line_and_model(**data)

    for row in result:
        image_data = row[0]
        caption = row[1]
        photo = types.BufferedInputFile(image_data, filename='image.jpg')
        if len(caption) > 1024:
            caption = caption[:1020] + "..."
        await message.answer_photo(photo, caption)