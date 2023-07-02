import sqlite3
import aiosqlite

from bot.functions.func import read_info
from bot.functions.paths import path_to_machines_db, path_to_vl2_txt


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
                        machine_id INTEGER,
                        name TEXT,
                        description TEXT
                        image BLOB,
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

machine_ids = ["10"]
images = read_info("/Users/admin/PycharmProjects/Emag_bot/mashines_foto/dekay y-3122/image_y3122.txt")
descriptions = read_info("/Users/admin/PycharmProjects/Emag_bot/mashines_foto/dekay y-3122/y3122.txt")

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
