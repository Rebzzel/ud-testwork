import os


def _env(key, default=None):
    return os.getenv(f'UDTW_TG_BOT_{key}', default)


TOKEN = _env('TOKEN')

TARGET_SPREADSHEET_ID = _env('TARGET_SPREADSHEET_ID', '1DwfUKQ1jbBkMW-dPr1jRsYY-SifQDwUKqscXr67lCPk')

API_URL = _env('API_URL', 'http://localhost:5000')


__all__ = [
    'TOKEN',

    'TARGET_SPREADSHEET_ID',

    'API_URL',
]
