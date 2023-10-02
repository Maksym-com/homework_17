from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("get_user_by_id", "Знайти користувача за id"),
            types.BotCommand("get_user_by_name", "Знайти користувача за ім'ям"),
            types.BotCommand("add_me", "Додати мене до бази даних"),
            types.BotCommand("remove_me", "Видалити мене з бази даних"),
            types.BotCommand("update_my_name", "Змінити моє ім'я"),
            types.BotCommand("update_my_last_name", "Змінити моє прізвище")
        ]
    )