import logging

from flask import Flask

from . import (
    env,
    routes,
)


logging.basicConfig()
app = Flask('wdtw-server')


@app.after_request
def _insert_cors_to_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


app.add_url_rule(
    '/handle/spreadsheet/<id>',
    view_func=routes.handle_spreadsheet,
)


def run(
    *,
    host: str = env.HOST,
    port: int = env.PORT,
    debug: bool = env.DEBUG,
):
    app.run(host=host, port=port, debug=debug)
