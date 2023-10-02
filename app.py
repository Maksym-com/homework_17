import logging
from aiogram import executor

import handlers
from loader import dp, db_bot
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    db_bot.open()
    db_bot.create_default_table()
    # db_bot.cursor.execute("INSERT INTO users VALUES (1, 'Valentyn', 'Starushok', 'I1nk3r')")
    # db_bot.conn.commit()
    logging.info("Db has opened connection")
    await set_default_commands(dispatcher)

async def on_shutdown(dispatcher):
    db_bot.close()
    logging.info("Db has closed connection")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)