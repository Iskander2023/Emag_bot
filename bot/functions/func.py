from PIL import Image
import os
from bot.functions.paths import path_to_allowed_txt


def is_user_allowed(user_id) -> bool:
    """
    Функция проверяющая есть ли user_id в файле allowed.txt если есть, True
    :param user_id: int
    :return: bool
    """
    with open(path_to_allowed_txt) as allow_file:
        for ruid in allow_file:
            if ruid.strip() == str(user_id):
                return True
    return False

def same_pictures(image_path) -> None:
    """
    Функция принимающая список путей к файлам изображений и меняющая их под нужный размер
    с сохранением и тем же именем

    :param image_path: list
    :return: None
    """
    for im in image_path:
        img = Image.open(im)
        new_image = img.resize((700, 945))
        file_name, file_ext = os.path.splitext(im)
        new_file_name = file_name + "" + file_ext
        new_image.save(new_file_name)


# def restricted():
#     def decorator(functions):
#         @wraps(functions)
#         async def wrapper(message):
#             user_id = message.from_user.id
#             if is_user_allowed(user_id) is False:
#                 await message.reply(f"У вас нет доступа к этой команде.")
#                 return
#             await functions(message)
#         return wrapper
#     return decorator

