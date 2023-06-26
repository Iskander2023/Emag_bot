from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types import FSInputFile

from bot.database.data import select_machines_by_line_and_model
from bot.keyboards.button_lists import machines_list_vm
from bot.keyboards.machine_keyboard import make_row_keyboard
from bot.states_class.user_class import UserState

router = Router()

@router.message(UserState.machine_selection,
                F.text.casefold() == "vm") # указываем "слово" именно с маленькой буквы, casefold приводит текст к нижнему регистру
async def answer_machine(message: Message, state: FSMContext) -> None:
    data = await state.update_data(line_name=message.text)
    await state.set_state(UserState.vm_state)
    await message.answer(
        text="Спасибо. Теперь, пожалуйста, выберите интересующий Вас станок:",
        reply_markup=make_row_keyboard(machines_list_vm))

@router.message(
    UserState.vm_state,
    F.text.casefold() == "vm9"
)
async def answer_machine(message: Message, state: FSMContext) -> None:
    await state.set_state(UserState.vm_state)

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
    UserState.vm_state,
    F.text.casefold() == "vm12")

async def answer_machine(message: Message, state: FSMContext) -> None:
    await state.set_state(UserState.vm_state)

    data = await state.update_data(model=message.text)
    result = await select_machines_by_line_and_model(**data)

    for row in result:
        image_data = row[0]
        caption = row[1]
        photo = types.BufferedInputFile(image_data, filename='image.jpg')
        if len(caption) > 1024:
            caption = caption[:1020] + "..."
        await message.answer_photo(photo, caption)

@router.message(UserState.vm_state
                )
async def process_unknown_write_bots(message: Message, state: FSMContext) -> None:
    await state.set_state(UserState.vm_state)
    await message.answer(f"Станка {message.text} в списке нет. "
                         f"\nЗдесь представлены станки ветки VM "
                         f"\nВернитесь в главное меню кнопкой /start\n")