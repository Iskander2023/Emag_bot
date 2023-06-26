from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BufferedInputFile
from aiogram.types import FSInputFile
from bot.database.data import select_machines_by_line_and_model
from bot.keyboards.button_lists import machines_list_vl
from bot.keyboards.machine_keyboard import make_row_keyboard
from bot.states_class.user_class import UserState


router = Router()

@router.message(UserState.machine_selection,
                F.text.casefold() == "vl") # указываем "слово" именно с маленькой буквы, casefold приводит текст к нижнему регистру
async def answer_machine(message: Message, state: FSMContext) -> None:
    data = await state.update_data(line_name=message.text)
    await state.set_state(UserState.vl_state)
    await message.answer(
        text="Спасибо. Теперь, пожалуйста, выберите интересующий Вас станок:",
        reply_markup=make_row_keyboard(machines_list_vl))

@router.message(
    UserState.vl_state,
    F.text.casefold() == "vl2"
)
async def answer_machine(message: Message, state: FSMContext) -> None:
    await state.set_state(UserState.vl_state)

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
    UserState.vl_state,
    F.text.casefold() == "vl4")  # выводит фотографию при нажатии на кнопку vl4

async def answer_machine(message: Message, state: FSMContext) -> None:
    await state.set_state(UserState.vl_state) # устанавливаем состояние в machine_selection для



    photos = [
              FSInputFile('/Users/admin/PycharmProjects/Emag_bot/mashines_foto/vl/vl4/vl4_mashine_1_2.jpg'),
              FSInputFile('/Users/admin/PycharmProjects/Emag_bot/mashines_foto/vl/vl4/vl4_drilling_1_2.jpg'),
              FSInputFile('/Users/admin/PycharmProjects/Emag_bot/mashines_foto/vl/vl4/vl4_revolver_1_2.jpg')
            ]
    cap = "Вертикальный токарный центр VL 4 способен обрабатывать заготовки с максимальным диаметром до 200 мм. VL 4 - один из модульных токарных центров EMAG, отличающихся очень компактной конструкцией. Как и все вертикальные токарные центры этой серии, VL 4 также имеет встроенную систему автоматизации подбора.  Массовое производство с вертикальным токарным центром VL 4 Модульная концепция VL 4 делает это возможным: Вертикальный токарный центр идеально адаптируется к различным областям применения, отличается чрезвычайно компактной конструкцией и оснащен мощными приводами. Конструкция токарного центра VL 4 позволяет гибко внедрять различные производственные технологии для мягкой и твердой обработки.  Основание станка, изготовленное из полимербетона MINERALIT®, обеспечивает низкую вибрацию при обработке и гарантирует длительный срок службы инструмента, а также очень высокое качество обработки при токарной обработке заготовок. Главный шпиндель закреплен на передней стороне с помощью составного упора скольжения и обеспечивает динамическое движение по осям X и Z. Ось Y для обработки сложных геометрических форм поставляется в качестве опции."
    cap1 = "Для фактической обработки используется 12-позиционная инструментальная револьверная головка, отличающаяся очень коротким временем индексации и исключительной стабильностью. Отличная доступность зоны обработки и инструментальной башни позволяет переналаживать вертикальный токарный центр за сравнительно короткое время.  В качестве опции для вертикальных токарных центров серии VL предлагается измерительная станция вне зоны обработки. Измерительная станция устанавливается между зоной обработки и приемной станцией. Таким образом, измерение производится во время загрузки/разгрузки, что значительно экономит время."

    if len(cap) > 1024:
        cap = cap[:1020] + "..."  # Укорачиваем описание до 1021 символа и добавляем многоточие

    for index, photo in enumerate(photos):
        if index == 0:
            await message.answer_photo(photo,
                                       caption=cap
                                       )
        elif index == 1:
            await message.answer_photo(photo,
                                       caption=cap1
                                      )
        else:
            await message.answer_photo(photo, caption=None
                                       )

@router.message(UserState.vl_state
                )
async def process_unknown_write_bots(message: Message, state: FSMContext) -> None:
    await state.set_state(UserState.vl_state)
    await message.answer(f"Станка {message.text} в списке нет. "
                         f"\nЗдесь представлены станки ветки VL "
                         f"\nВернитесь в главное меню кнопкой /start\n")