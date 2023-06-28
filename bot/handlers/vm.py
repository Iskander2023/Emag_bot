from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot.database.machine_base import select_machines_by_line_and_model
from bot.keyboards.button_lists import machines_list_vm
from bot.states_class.user_class import BotState

router = Router()

@router.message(
    BotState.vm_state,
    F.text.in_(machines_list_vm)
)
async def answer_machine(message: Message, state: FSMContext) -> None:
    await state.set_state(BotState.vm_state)

    data = await state.update_data(model=message.text)
    result = await select_machines_by_line_and_model(**data)

    for row in result:
        image_data = row[0]
        caption = row[1]
        photo = types.BufferedInputFile(image_data, filename='image.jpg')
        if len(caption) > 1024:
            caption = caption[:1020] + "..."
        await message.answer_photo(photo, caption)

@router.message(BotState.vm_state
                )
async def process_unknown_write_bots(message: Message, state: FSMContext) -> None:
    await state.set_state(BotState.vm_state)
    await message.answer(f"Станка {message.text} в списке нет. "
                         f"\nЗдесь представлены станки ветки VM "
                         f"\nВернитесь в главное меню кнопкой /start\n")