import functools
import logging

from flask import (
    request,
    make_response,
)

from . import services


def catch(fn):
    @functools.wraps(fn)
    def wrapper(**kwargs):
        try:
            return fn(**kwargs)
        except Exception:
            logging.exception('')
            return make_response({ 'error': 'Unknown error.' }, 500)
    return wrapper


@catch
def handle_spreadsheet(id: str):
    return services.build_orders_info_from_spreadsheet(id)


__all__ = [
    'handle_spreadsheet',
]
