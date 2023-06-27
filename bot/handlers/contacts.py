from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot.database.contact_database import select_contacts
from bot.keyboards.button_lists import contacts_list
from bot.states_class.user_class import UserState

router = Router()

@router.message(
    UserState.select_contacts,
    F.text.in_(contacts_list)
)
async def answer_contacts(message: Message, state: FSMContext) -> None:
    await state.set_state(UserState.select_contacts)
    result = await select_contacts(message.text)
    for data in result:
        message_text = f"---------------------------\n" \
                       f"{data[2]}\n" \
                       f"{data[0]} {data[1]}\n" \
                       f"Номер телефона: {data[3]}\n" \
                       f"Email: {data[4]}\n" \
                       f"---------------------------"

        await message.answer(text=message_text)

