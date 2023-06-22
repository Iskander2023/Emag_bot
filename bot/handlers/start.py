from aiogram import Router, types
from aiogram.filters.text import Text
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command(commands=('start')))
async def cmd_start(message: Message):
    kb = [
         [
            types.KeyboardButton(text="Станки"),
            types.KeyboardButton(text="Завершенные проекты"),
            types.KeyboardButton(text="Изготовленые детали"),

         ]
        ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         input_field_placeholder="Выберите что Вас интересует:"
                                         )
    await message.answer("Выберите что Вас интересует?", reply_markup=keyboard)


@router.message(Text(text="Станки"))  # выводит варианты станков которые есть
async def answer_machine(message: Message):
    kb = [
        [
            types.KeyboardButton(text="vl2"),
            types.KeyboardButton(text="vl4"),
        ]
    ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         input_field_placeholder="Выберите станок:"
                                         )
    await message.answer("Выберите станок:", reply_markup=keyboard)



