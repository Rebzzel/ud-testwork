import logging

from aiogram import (
    Bot,
    Dispatcher,
    executor,
)

from . import (
    env,
    commands,
)


if not env.TOKEN:
    raise Exception(
        'Setup UDTW_TG_BOT_TOKEN env variable'
        ' (or `TOKEN` from env.py) before import this package!'
    )


logging.basicConfig()
app = Bot(token=env.TOKEN)
dp = Dispatcher(app)


dp.register_message_handler(commands.check, commands=['check'])


def run():
    executor.start_polling(dp)
