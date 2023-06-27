import sqlite3
import aiosqlite
from bot.functions.paths import path_to_machines_db


def create_employees_table():
    """
    Функция, создающая таблицу контактов в базе данных machines.db.
    :param :
    :return: None
    """
    with sqlite3.connect(path_to_machines_db) as conn:
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS employee_contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                  department TEXT,
                  first_name TEXT,
                  surname TEXT,
                  position_at_work TEXT,
                  phone_number TEXT,
                  email TEXT
            )
        """)
        conn.commit()

def insert_employee_list(departments: list[str], first_names: list[str], surnames: list[str], positions_at_work: list[str], phone_numbers: list[str], emails: list[str]):
    """
    функция для загрузки контактов
    :param department: отдел
    :param first_name: имя
    :param surname: фамилия
    :param position_at_work: должность
    :param phone_number: номер телефона
    :param email: емейл

    :return:
    """
    conn = sqlite3.connect(path_to_machines_db)
    cursor = conn.cursor()
    for department, first_name, surname, position_at_work, phone_number, email in zip\
                (departments, first_names, surnames, positions_at_work, phone_numbers, emails):

        cursor.execute('INSERT INTO employee_contacts (department, first_name, surname, position_at_work, phone_number, email) VALUES (?, ?, ?, ?, ?, ?)',
                       (department, first_name, surname, position_at_work, phone_number, email))

    conn.commit()
    conn.close()

departments = ["Юридический отдел"]
first_names = ["Павел"]
surnames = ["Султанов"]
positions_at_work = ["Руководитель юр.отдела"]
phone_numbers = ["+791234567"]
emails = ["psultanov@emag.com"]

#insert_employee_list(departments, first_names, surnames, positions_at_work, phone_numbers, emails)


async def select_contacts(department):
    """
    Функция делающая выборку из БД по отделам
    :param department: str
    :return:
    """
    async with aiosqlite.connect(path_to_machines_db) as db:
        cursor = await db.execute('SELECT first_name, surname, position_at_work, phone_number, email FROM employee_contacts WHERE department = ?',(department,))
        rows = await cursor.fetchall()

    return rows

#select_contacts("Технический отдел")