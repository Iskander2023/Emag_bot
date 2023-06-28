import sqlite3
import aiosqlite
from bot.functions.paths import path_to_machines_db


def create_about_company():
    """
    Функция, создающая таблицу о компании в базе данных machines.db.
    :param :
    :return: None
    """
    with sqlite3.connect(path_to_machines_db) as conn:
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS about_company (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  address TEXT,
                  info TEXT,
                  email TEXT,
                  website TEXT,
                  phone_number TEXT   )
            """)
        conn.commit()

def insert_about_company(names: list[str], addresss: list[str], infos: list[str], emails: list[str], websites: list[str], phone_numbers: list[str]):
    """
    функция для загрузки контактов
    :param address: адресс
    :param info:  нформация
    :param email: емейл
    :param website: сайт
    :param phone_number: номер телефона

    :return:
    """
    conn = sqlite3.connect(path_to_machines_db)
    cursor = conn.cursor()
    for name, address, info, email, website, phone_number in zip\
                (names, addresss, infos, emails, websites, phone_numbers):

        cursor.execute('INSERT INTO about_company (name, address, info, email, website, phone_number) VALUES (?, ?, ?, ?, ?, ?)',
                       (name, address, info, email, website, phone_number))

    conn.commit()
    conn.close()

names = ["EMAG"]
addresss = ["Москва и Московская обл., Москва, ул. Академика Челомея д.3 корп.2"]
infos = ["Группа EMAG поставляет станки и производственные системы для обработки деталей в сфере автомобильной, авиационной, энергетической и добывающей промышленности. Идет ли речь о токарной обработке, шлифовании, зубофрезеровании, сборке с лазерной сваркой, либо индукционной закалке как для крупногабаритных, так и для малоразмерных деталей - группа EMAG всегда предложит оптимальное решение для любого случая."
"При этом богатая своими производственными традициями группа EMAG опирается на обширное ноу-хау, накопленное предприятиями, вошедшими в ее состав, и предлагает своим заказчикам модульные решения технологических задач под ключ на высочайшем мировом уровне."
]
emails = ["main@emag-group.ru"]
websites = ["https://www.emag.com"]
phone_numbers = ["+74952870960"]

#insert_about_company(names, addresss, infos, emails, websites, phone_numbers)


async def select_company(name):
    """
    Функция делающая запрос в БД о фирме
    :param department: str
    :return:
    """
    async with aiosqlite.connect(path_to_machines_db) as db:
        cursor = await db.execute('SELECT address, info, email, website, phone_number FROM about_company WHERE name = ?',(name,))
        rows = await cursor.fetchall()

    return rows