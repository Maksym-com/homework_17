import logging

from aiogram.utils.exceptions import CantParseEntities

from loader import dp

@dp.errors_handler()
async def error_handler(update, exception):

    if isinstance(exception, CantParseEntities):
        logging.exception(CantParseEntities)
        return True