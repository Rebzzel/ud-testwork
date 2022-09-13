import os


def _env(key, default=None):
    return os.getenv(f'UDTW_SERVER_{key}', default)


def _parse_bool(string: str):
    return string.lower() in ( '1', 'true', 'yes', 'on', )


DEBUG = _parse_bool(_env('DEBUG', '1'))

HOST = _env('HOST', '0.0.0.0')
PORT = int(_env('PORT', '5000'))

GOOGLE_CREDENTIALS_FILEPATH = _env(
    'GOOGLE_CREDENTIALS_FILEPATH',
    os.path.join(os.getcwd(), 'credentials.json')
)

DB_DATABASE = _env('DB_DATABASE')
DB_HOST = _env('DB_HOST', '127.0.0.1')
DB_PORT = int(_env('DB_PORT', '5432'))
DB_USERNAME = _env('DB_USERNAME', 'postgres')
DB_PASSWORD = _env('DB_PASSWORD')


__all__ = [
    'DEBUG',

    'HOST',
    'PORT',

    'GOOGLE_CREDENTIALS_FILEPATH',

    'DB_DATABASE',
    'DB_HOST',
    'DB_PORT',
    'DB_USERNAME',
    'DB_PASSWORD',
]
