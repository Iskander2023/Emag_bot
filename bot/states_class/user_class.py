from aiogram.fsm.state import StatesGroup, State


class BotState(StatesGroup):
    start_state = State()
    machine_selection = State()
    emag = State()
    dekay = State()
    vl_state = State()
    vm_state = State()
    about_us = State()
    select_contacts = State()
    about_company = State()