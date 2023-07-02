from aiogram.fsm.state import StatesGroup, State


class BotState(StatesGroup):
    start_state = State() # старт

    machine_selection = State() # выбор станка
    choice_line = State() # выбор линейки станков
    choice_machine = State() # выбор станка

    about_us = State() # о нас
    select_contacts = State() # выбор контактов
    about_company = State() # о компании

    part_selection = State() # выбор детали
    choice_of_direction = State() # выбор направления
    details_choice = State() # выбор деталей