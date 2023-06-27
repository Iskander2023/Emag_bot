from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    start_state = State()
    machine_selection = State()
    vl_state = State()
    vm_state = State()
    select_contacts = State()