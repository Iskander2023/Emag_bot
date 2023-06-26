from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types import FSInputFile
from bot.keyboards.button_lists import machines_list_vm
from bot.keyboards.machine_keyboard import make_row_keyboard
from bot.states_class.user_class import UserState

router = Router()

@router.message(UserState.machine_selection,
                F.text.casefold() == "vm") # указываем "слово" именно с маленькой буквы, casefold приводит текст к нижнему регистру
async def answer_machine(message: Message, state: FSMContext) -> None:
    print(message.text)
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
    print(message.text)

    photos = [
              FSInputFile('/Users/admin/PycharmProjects/Emag_bot/mashines_foto/vm/vm9/vm9_machine.jpg'),
              FSInputFile('/Users/admin/PycharmProjects/Emag_bot/mashines_foto/vm/vm9/vm9_part_processing.jpg'),
              FSInputFile('/Users/admin/PycharmProjects/Emag_bot/mashines_foto/vm/vm9/vm9_part_processing2.jpg'),
              FSInputFile('/Users/admin/PycharmProjects/Emag_bot/mashines_foto/vm/vm9/vm9_installation_detail.jpg'),
    ]
    cap = "С новым вертикальным токарным центром VM 9 EMAG представила платформу, которая охватывает широкий спектр применений благодаря комбинированным технологиям токарной обработки, фрезерования и сверления и интеллектуальной конструкции станков. Высокодоступная область обработки и шпиндель заготовки, установленный внизу, обеспечивают короткое время оснастки и максимальную гибкость в производстве крупных компонентов."
    cap1 = "Сверхмощный фундамент вертикального токарного центра VM 9 изготовлен из полимербетонной колонны MINERALIT®. Особенно хорошие демпфирующие свойства Mineralit® в сочетании с составным слайдом с осями X и Z обеспечивают отличное качество обработки, высокую скорость и короткое время простоя. Главный шпиндель обеспечивает необходимую мощность с номинальной мощностью 83 кВт и крутящим моментом 990 Нм.В зависимости от желаемого интерфейса (BMT или VDI) инструментальная башня имеет восемь или двенадцать позиций инструмента, которые также могут быть оснащены приводными инструментами, например, для выполнения буровых работ. Встроенный зонд обеспечивает надежность процесса и стабильно высокое качество заготовки (первая часть = хорошая часть)."
    cap2 = "Эргономичное обслуживание и погрузка. Но токарный центр VM 9 не только обеспечивает отличное качество обработки. Эргономичный дизайн машин является прекрасным свидетельством многолетнего опыта EMAG с вертикальными токарными станками. Как область обработки, так и все компоненты обслуживания легко доступны. Это основное преимущество для клиентов, которым приходится обрабатывать с ЧПУ много разных заготовок или различных семейств деталей."
    cap3 = "С вертикальным токарным станком VM 9 EMAG предлагает новую систему станков с ЧПУ для деталей, подходящих для производства широкого спектра заготовок во многих различных сценариях производства благодаря своей гибкости. Будь то компоненты для грузовых автомобилей, строительной и сельскохозяйственной техники или для машиностроения и машиностроения, поворотный центр VM 9 идеально подходит практически для любого сектора. Отличная доступность зоны обработки делает станки универсальным решением для точеных деталей."

    if len(cap) > 1024:
        cap = cap[:1020] + "..."  # Укорачиваем описание до 1021 символа и добавляем многоточие

    for index, photo in enumerate(photos):
        if index == 0:
            await message.answer_photo(photo,
                                       caption=cap)  # Описание будет применено только для фотографии с указанным индексом
        elif index == 1:
            await message.answer_photo(photo,
                                       caption=cap1)
        elif index == 2:
            await message.answer_photo(photo,
                                       caption=cap2)
        elif index == 3:
            await message.answer_photo(photo,
                                       caption=cap3)
        else:
            await message.answer_photo(photo, caption=None)

@router.message(
    UserState.vm_state,
    F.text.casefold() == "vm12")

async def answer_machine(message: Message, state: FSMContext) -> None:
    await state.set_state(UserState.vm_state)

    photos = [
              FSInputFile('/Users/admin/PycharmProjects/Emag_bot/mashines_foto/vm/vm12/vm12_machine.jpg'),
              FSInputFile('/Users/admin/PycharmProjects/Emag_bot/mashines_foto/vm/vm12/vm12_clamping_device.jpg'),
            ]
    cap = "Vm12 machine"
    cap1 = "Clamping device"

    if len(cap) > 1024:
        cap = cap[:1020] + "..."

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

@router.message(UserState.vm_state
                )
async def process_unknown_write_bots(message: Message, state: FSMContext) -> None:
    await state.set_state(UserState.vm_state)
    await message.answer(f"Станка {message.text} в списке нет. "
                         f"\nЗдесь представлены станки ветки VM "
                         f"\nВернитесь в главное меню кнопкой /start\n")