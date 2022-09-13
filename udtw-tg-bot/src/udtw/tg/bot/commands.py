import functools
import logging

from aiogram import types

from . import (
    env,
    services,
)


def catch(fn):
    @functools.wraps(fn)
    async def wrapper(message: types.Message):
        try:
            return await fn(message)
        except Exception:
            logging.exception(message)
            await message.answer('Упс. Кажется, что-то пошло не так...')
    return wrapper


@catch
async def check(message: types.Message) -> None:
    orders_outdated = services.check_orders_from_spreadsheet(
        env.TARGET_SPREADSHEET_ID
    )
    
    if not orders_outdated:
        return await message.answer('Просроченных заказов не найдено.')
    
    await message.answer(
        'Найдено {} просроченных заказов:\n{}'
        .format(len(orders_outdated), '\n'.join(map(str, orders_outdated)))
    )


__all__ = [
    'check',
]
