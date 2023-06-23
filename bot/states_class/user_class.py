from aiogram.fsm.state import StatesGroup, State


class Bot_States(StatesGroup):
    start = State()
    machine_selection = State()
    vl2 = State()
    vl4 = State()
    projects = State()