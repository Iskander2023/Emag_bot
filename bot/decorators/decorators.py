from functools import wraps

def is_user_allowed(user_id) -> bool:
    with open("/Users/admin/PycharmProjects/Emag_bot/bot/decorators/ allowed.txt") as allow_file:
        for ruid in allow_file:
            if ruid.strip() == str(user_id):
                return True
    return False

def restricted():
    def decorator(func):
        @wraps(func)
        async def wrapper(message):
            user_id = message.from_user.id
            if is_user_allowed(user_id) is False:
                await message.reply(f"У вас нет доступа к этой команде.")
                return
            await func(message)
        return wrapper
    return decorator

