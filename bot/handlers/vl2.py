from aiogram import Router
from aiogram.filters.text import Text
from aiogram.types import Message
from aiogram.types import FSInputFile
from bot.decorators.decorators import restricted

router = Router()



@router.message(Text(text="vl2"))  # выводит фотографию при нажатии на кнопку vl4
@restricted()
async def answer_machine(message: Message):

    photos = [
              FSInputFile('/Users/admin/PycharmProjects/EmagBot/mashines_foto/vl2/vl2_mashine.jpg'),
              FSInputFile('/Users/admin/PycharmProjects/EmagBot/mashines_foto/vl2/vl2_revolver.jpg'),
              FSInputFile('/Users/admin/PycharmProjects/EmagBot/mashines_foto/vl2/vl2_automation.jpg'),
              FSInputFile('/Users/admin/PycharmProjects/EmagBot/mashines_foto/vl2/vl2_billet.jpg'),
              FSInputFile('/Users/admin/PycharmProjects/EmagBot/mashines_foto/vl2/vl2_probe.jpg'),

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