import sqlite3
import aiosqlite

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
                  line_name TEXT,
                  model TEXT,
                  image BLOB,
                  description TEXT
            )
        """)
        conn.commit()

def insert_machine(line_name: str, model: str, image_path: bool, description: str):
    """
    функция для загрузки станков в БД
    :param line_name: название линейки станков
    :param model: модель станка
    :param image_path: путь к изображению
    :param description: описание изображения
    :return:
    """
    conn = sqlite3.connect(path_to_machines_db)
    cursor = conn.cursor()
    with open(image_path, 'rb') as file:
        image_data = file.read()
    cursor.execute('INSERT INTO machines (line_name, model, image, description) VALUES (?, ?, ?, ?)',
                   (line_name, model, image_data, description))
    conn.commit()
    conn.close()

def insert_machine_list(line_names: list[str], models: list[str], image_paths: list[str], descriptions: list[str]):
    """
    функция для загрузки станков в БД
    :param line_name: название линейки станков
    :param model: модель станка
    :param image_path: путь к изображению
    :param description: описание изображения
    :return:
    """
    conn = sqlite3.connect(path_to_machines_db)
    cursor = conn.cursor()
    for line_name, model, image_path, description in zip(line_names, models, image_paths, descriptions):
        with open(image_path, 'rb') as file:
            image_data = file.read()
        cursor.execute('INSERT INTO machines (line_name, model, image, description) VALUES (?, ?, ?, ?)',
                       (line_name, model, image_data, description))

    conn.commit()
    conn.close()

# line_names = []
# models = []
# image_paths = ['/Users/admin/PycharmProjects/Emag_bot/mashines_foto/vm/vm12/vm12_machine.jpg',
#               '/Users/admin/PycharmProjects/Emag_bot/mashines_foto/vm/vm12/vm12_clamping_device.jpg']
# descriptions = ["Vm12 machine",
#                 "Clamping device"]

#insert_machine_list(line_names, models, image_paths, descriptions)


async def select_machines_by_line_and_model(line_name, model):
    """
    Функция делающая выборку из БД по названию линейки станков и модели станка
    :param line_name: str
    :param model: str
    :return:
    """
    async with aiosqlite.connect(path_to_machines_db) as db:
        cursor = await db.execute('SELECT image, description FROM machines WHERE line_name = ? AND model = ?', (line_name, model))
        rows = await cursor.fetchall()

    return rows


