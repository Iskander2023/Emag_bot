from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot.database.about_company import select_company
from bot.database.contact_database import select_contacts
from bot.keyboards.button_lists import contacts_list, about_the_company
from bot.keyboards.machine_keyboard import make_row_keyboard
from bot.states_class.bot_states import BotState

router = Router()

@router.message(
    BotState.about_us,
    F.text.in_(about_the_company)
)

async def answer_about_us(message: Message, state: FSMContext) -> None:
    if message.text == "Контакты":
        await state.set_state(BotState.select_contacts)
        await message.answer(
            text="Спасибо. Теперь, пожалуйста, выберите контакты:",
            reply_markup=make_row_keyboard(contacts_list))
    elif message.text == "О нас":
        await state.set_state(BotState.about_company)
        about = await select_company(name="EMAG")
        for data in about:
            message_text = f"Адресс компании: {data[0]}\n" \
                           f"Телефон: {data[4]}\n" \
                           f"Емейл: {data[2]}\n" \
                           f"Сайт: [{data[3]}]({data[3]})\n" \
                           f"Наша деятельность: {data[1]}\n" \

            await message.answer(text=message_text, parse_mode="Markdown")
        await state.set_state(BotState.about_us)

@router.message(BotState.about_us
                )
async def process_unknown_dekay(message: Message, state: FSMContext) -> None:
    await state.set_state(BotState.about_us)
    await message.answer(f"Команды {message.text} в списке нет. "
                         f"\nВыберите из доступных команд"
                         )

@router.message(
    BotState.select_contacts,
    F.text.in_(contacts_list)
)
async def answer_contacts(message: Message, state: FSMContext) -> None:
    await state.set_state(BotState.select_contacts)
    result = await select_contacts(message.text)
    for data in result:
        message_text = f"---------------------------\n" \
                       f"{data[2]}\n" \
                       f"{data[0]} {data[1]}\n" \
                       f"Номер телефона: {data[3]}\n" \
                       f"Email: {data[4]}\n" \
                       f"---------------------------"

        await message.answer(text=message_text)
        await state.set_state(BotState.select_contacts)

@router.message(BotState.select_contacts
                )
async def process_unknown_dekay(message: Message, state: FSMContext) -> None:
    await state.set_state(BotState.select_contacts)
    await message.answer(f"Контактов {message.text} в списке нет. "
                         f"\nВыберите из доступных контактов"
                         )