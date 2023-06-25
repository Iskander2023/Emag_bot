from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types import FSInputFile
from bot.keyboards.button_lists import machines_list_vl
from bot.keyboards.machine_keyboard import make_row_keyboard
from bot.states_class.user_class import UserState

router = Router()

@router.message(UserState.machine_selection,
                F.text.casefold() == "vl") # указываем "слово" именно с маленькой буквы, casefold приводит текст к нижнему регистру
async def answer_machine(message: Message, state: FSMContext) -> None:
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

    photos = [
              FSInputFile('/Users/admin/PycharmProjects/Emag_bot/mashines_foto/vl/vl2/vl2_mashine.jpg'),
              FSInputFile('/Users/admin/PycharmProjects/Emag_bot/mashines_foto/vl/vl2/vl2_revolver.jpg'),
              FSInputFile('/Users/admin/PycharmProjects/Emag_bot/mashines_foto/vl/vl2/vl2_automation.jpg'),
              FSInputFile('/Users/admin/PycharmProjects/Emag_bot/mashines_foto/vl/vl2/vl2_billet.jpg'),
              FSInputFile('/Users/admin/PycharmProjects/Emag_bot/mashines_foto/vl/vl2/vl2_probe.jpg'),

    ]
    cap = "Стабильная конструкция станка, динамичные оси и простота управления - вот выдающиеся характеристики вертикальных токарных станков серии VL. Основанные на совершенно новой модульной концепции станка, вертикальные токарные станки VL 2 позволяют использовать различные производственные технологии для мягкой и твердой обработки с интегрированной автоматикой и шпинделем с подхватом, обеспечивая при этом наилучшую отдачу от инвестиций."
    cap2 = "Три оси + револьверная головка с двенадцатью приводными инструментами + автоматизация.  Базовый станок VL 2, трехосевой инвертированный вертикальный токарный станок, имеет привлекательный дизайн. Основой токарного станка является корпус станка, изготовленный из полимербетона MINERALIT®. Рабочий шпиндель установлен на передней части корпуса станка на составном суппорте, который совершает движения по осям X и Z. Револьверная головка расположена под рабочим шпинделем и вмещает до двенадцати токарных или приводных инструментов. Кроме того, токарный станок с ЧПУ VL 2 может быть оснащен осью Y в револьверной головке."
    cap3 = "Токарные станки также идеально подходят для использования в конвейерном производстве, поскольку токарные станки VL 2 могут быть соединены с простыми компонентами автоматизации, такими как конвейеры, перекидные устройства и устройства смены.  Заготовки, которые можно обрабатывать на токарном станке, включают фланцы и шестерни. Комбинация вертикальных токарных станков с другими модульными станками позволяет эффективно реализовать сборочную линию, например, для зубчатых колес. Токарная обработка на станке VL 2 дополняется последующим процессом на станке VL 4 H для зубофрезерования и использованием станка VLC 100 C для снятия фаски."
    cap4 = "Преимущества Простая концепция автоматизации = высокая готовность Интегрированная автоматизация, автоматическая смена заготовок"

    if len(cap) > 1024:
        cap = cap[:1020] + "..."  # Укорачиваем описание до 1021 символа и добавляем многоточие

    for index, photo in enumerate(photos):
        if index == 0:
            await message.answer_photo(photo,
                                       caption=cap)  # Описание будет применено только для фотографии с указанным индексом
        elif index == 1:
            await message.answer_photo(photo,
                                       caption=cap2)
        elif index == 2:
            await message.answer_photo(photo,
                                       caption=cap3)
        elif index == 3:
            await message.answer_photo(photo,
                                       caption=cap4)
        else:
            await message.answer_photo(photo, caption=None)

@router.message(
    UserState.vl_state,
    F.text.casefold() == "vl4")  # выводит фотографию при нажатии на кнопку vl4

async def answer_machine(message: Message, state: FSMContext) -> None:
    await state.set_state(UserState.vl_state) # устанавливаем состояние в machine_selection для
                                                       # возможности потыкать по кнопкам и посмтреть все станки в меню

    photos = [
              FSInputFile('/Users/admin/PycharmProjects/Emag_bot/mashines_foto/vl/vl4/vl4_mashine.jpg'),
              FSInputFile('/Users/admin/PycharmProjects/Emag_bot/mashines_foto/vl/vl4/vl4_drilling.jpg'),
              FSInputFile('/Users/admin/PycharmProjects/Emag_bot/mashines_foto/vl/vl4/vl4_revolver.jpg')
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