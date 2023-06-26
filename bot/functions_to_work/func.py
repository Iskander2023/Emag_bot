from PIL import Image
import os

def is_user_allowed(user_id) -> bool:
    """
    Функция проверяющая есть ли user_id в файле allowed.txt если есть, True
    :param user_id: int
    :return: bool
    """
    with open("/Users/admin/PycharmProjects/Emag_bot/bot/functions_to_work/ allowed.txt") as allow_file:
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
        #print(new_file_name)
        new_image.save(new_file_name)


# def restricted():
#     def decorator(functions_to_work):
#         @wraps(functions_to_work)
#         async def wrapper(message):
#             user_id = message.from_user.id
#             if is_user_allowed(user_id) is False:
#                 await message.reply(f"У вас нет доступа к этой команде.")
#                 return
#             await functions_to_work(message)
#         return wrapper
#     return decorator

