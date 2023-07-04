import sqlite3
import aiosqlite

from bot.functions.func import read_info
from bot.functions.paths import path_to_machines_db


def create_db():
    """
    Функция, создающая базу данных.
    :param :
    :return: None
    """
    with sqlite3.connect(path_to_machines_db) as conn:
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS machines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name TEXT,
                line_name TEXT,
                model TEXT
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS info_machines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                machine_id INTEGER,
                image BLOB,
                description TEXT NULL, 
                FOREIGN KEY (machine_id) REFERENCES machines(id) ON DELETE CASCADE
            )
        """)

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

        cur.execute("""
                    CREATE TABLE IF NOT EXISTS details (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        type TEXT,
                        description TEXT,
                        image BLOB)
                        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS detail_machine_mapping (
                detail_id INTEGER,
                machine_id INTEGER,
                FOREIGN KEY (detail_id) REFERENCES details(id) ON DELETE CASCADE,
                FOREIGN KEY (machine_id) REFERENCES machines(id) ON DELETE CASCADE
                )
                """)

        conn.commit()

def insert_machine_list(company_names: list[str], line_names: list[str], models: list[str]):
    """
    функция для загрузки станков в БД
    :param company_names: фирма
    :param line_name: название линейки станков
    :param model: модель станка

    :return:
    """
    conn = sqlite3.connect(path_to_machines_db)
    cursor = conn.cursor()
    for company_name, line_name, model in zip(company_names, line_names, models):

        cursor.execute('INSERT INTO machines (company_name, line_name, model) VALUES (?, ?, ?)',
                       (company_name, line_name, model))

    conn.commit()
    conn.close()

# company_names = ["EMAG", "EMAG", "EMAG", "EMAG", "Dekay", "Dekay"]
# line_names = ["VL", "VL", "VM", "VM", "V", "Y"]
# models = ["vl2", "vl4", "vm9", "vm12", "V-1160", "Y-3122"]
# insert_machine_list(company_names, line_names, models)



def insert_machine_info(machine_ids: list[str], images: list[str], descriptions: list[str]):
    """
    функция для загрузки информации о станках в БД
    :param ids: id станков
    :param image_paths: путь к фото
    :param descriptions: описание

    :return:
    """
    conn = sqlite3.connect(path_to_machines_db)
    cursor = conn.cursor()
    for machine_id, image, description in zip(machine_ids, images, descriptions):
        with open(image, 'rb') as file:
            image_data = file.read()
        cursor.execute('INSERT INTO info_machines (machine_id, image, description) VALUES (?, ?, ?)',
                       (machine_id, image_data, description))

    conn.commit()
    conn.close()

# machine_ids = ["10"]
# images = read_info("/Users/admin/PycharmProjects/Emag_bot/mashines_foto/dekay y-3122/image_y3122.txt")
# descriptions = read_info("/Users/admin/PycharmProjects/Emag_bot/mashines_foto/dekay y-3122/y3122.txt")

# create_db()
#insert_machine_info(machine_ids, images, descriptions)


async def select_machines_by_model(model):
    """
    Функция делающая выборку из БД по названию модели станка
    :param model: int
    :return:
    """
    async with aiosqlite.connect(path_to_machines_db) as db:
        cursor = await db.execute(
            'SELECT info.image, info.description FROM info_machines info JOIN machines m ON info.machine_id = m.id WHERE m.model = ?',
            (model,))
        rows = await cursor.fetchall()

    return rows

def insert_details_info(names: list[str], types: list[str], descriptions: list[str], images: list[str]):
    """
    функция для загрузки информации о деталях в БД

    :param names: название детали
    :param descriptions: описание детали
    :param images: изображение
    :return:
    """
    conn = sqlite3.connect(path_to_machines_db)
    cursor = conn.cursor()
    for name, type, description, image in zip(names, types, descriptions, images):
        with open(image, 'rb') as file:
            image_data = file.read()
        cursor.execute('INSERT INTO details (name, type, description, image) VALUES (?, ?, ?, ?)',
                       (name, type, description, image_data))

    conn.commit()
    conn.close()

async def select_details(type: str, name: str):
    """
    Функция получения из БД деталей по типу и названию
    :param type: str
    :param name: str
    :return:
    """
    async with aiosqlite.connect(path_to_machines_db) as db:
        cursor = await db.execute('SELECT image, description FROM details WHERE type = ? AND name = ?',(type, name))
        rows = await cursor.fetchall()

    return rows

# names = ["OTTM", "OTTM"]
# type = ["Муфта", "Муфта"]
# descriptions = read_info("/Users/admin/PycharmProjects/Emag_bot/details_foto/coupling/OTTM/ottm.txt")
#images = read_info("/Users/admin/PycharmProjects/Emag_bot/details_foto/coupling/OTTM/image_ottm.txt")

# names = ["BATRESS", "BATRESS"]
# type = ["Муфта", "Муфта"]
# descriptions = read_info("/Users/admin/PycharmProjects/Emag_bot/details_foto/coupling/BATRESS/batress.txt")
# images = read_info("/Users/admin/PycharmProjects/Emag_bot/details_foto/coupling/BATRESS/image_batress.txt")

# names = ["CENTUM"]
# type = ["Муфта"]
# descriptions = read_info("/Users/admin/PycharmProjects/Emag_bot/details_foto/coupling/CENTUM/centum.txt")
# images = read_info("/Users/admin/PycharmProjects/Emag_bot/details_foto/coupling/CENTUM/image_centum.txt")

# names = ["Ступица"]
# type = ["Ступица колеса"]
# descriptions = read_info("/Users/admin/PycharmProjects/Emag_bot/details_foto/automobile_hub/hub.txt")
# images = read_info("/Users/admin/PycharmProjects/Emag_bot/details_foto/automobile_hub/image_hub.txt")

# names = ["Кольцо подшипника внутреннее"]
# type = ["Кольцо подшипника внутреннее"]
# descriptions = read_info("/Users/admin/PycharmProjects/Emag_bot/details_foto/bearing_ring/ring.txt")
# images = read_info("/Users/admin/PycharmProjects/Emag_bot/details_foto/bearing_ring/image_ring.txt")
#
# insert_details_info(names, type, descriptions, images)




# def add_column_to_table(table_name: str, column_name: str, data_type: str):
#     """
#     Функция для добавления новых полей в БД
#     :param table_name: название таблицы
#     :param column_name: название поля
#     :param data_type: тип данных
#     :return:
#     """
#     conn = sqlite3.connect(path_to_machines_db)
#     c = conn.cursor()
#     c.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {data_type}")
#     conn.commit()
#     conn.close()
