import typing as t
import xml.dom.minidom as xml

import requests

from . import (
    env,
    exceptions,
)


def _build_google_api():
    from google.oauth2.service_account import Credentials
    from googleapiclient.discovery import build

    credentials = Credentials.from_service_account_file(
        env.GOOGLE_CREDENTIALS_FILEPATH,
        scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']
    )

    return build('sheets', 'v4', credentials=credentials)


def _build_database_engine():
    from psycopg2 import connect
    return connect(
        host=env.DB_HOST,
        port=env.DB_PORT,
        database=env.DB_DATABASE,
        user=env.DB_USERNAME,
        password=env.DB_PASSWORD,
    )


gapi = _build_google_api()
db = _build_database_engine() if env.DB_DATABASE else None


def fetch_spreadsheet(
    id: str,
    range: str = 'A:Z',
    format: t.Literal['rows', 'columns'] = 'rows'
) -> dict:
    '''Fetching Google spreadsheets data.'''

    return gapi.spreadsheets().values().get(
        spreadsheetId=id,
        range=range,
        majorDimension=format.upper(),
    ).execute()


def fetch_valute_cost(symbol: str) -> float:
    '''Fetching valute cost in rubles at CBR rate.'''

    actual_symbol = symbol.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    response.raise_for_status()

    dom = xml.parseString(response.text)
    valutes = dom.getElementsByTagName('Valute')

    for valute in valutes:
        valute_symbol = _parse_text_from_xml(
            valute.getElementsByTagName('CharCode')[0]
        )

        if valute_symbol != actual_symbol:
            continue

        valute_cost = _parse_text_from_xml(
            valute.getElementsByTagName('Value')[0]
        )

        return float(valute_cost.replace(',', '.'))

    raise exceptions.ValuteNotFoundException(symbol)


def build_orders_info_from_spreadsheet(spreadsheet_id: str) -> t.List[dict]:
    '''
    Building orders info from spreadsheet. 
    This also writting result to database.
    '''

    spreadsheet = fetch_spreadsheet(spreadsheet_id)
    
    # Skipping first record with columns names...
    records = spreadsheet['values'][1:]
    rub_per_usd = fetch_valute_cost('usd')
    orders_info = []

    for record in records:
        (id, order_id, cost_in_usd, delivery_at) = record
        (id, order_id) = map(int, (id, order_id,))
        (cost_in_usd) = float(cost_in_usd)
        (cost_in_rub) = cost_in_usd * rub_per_usd

        orders_info.append({
            'id': id,
            'order_id': order_id,
            'cost_in_usd': cost_in_usd,
            'delivery_at': delivery_at,
            'cost_in_rub': cost_in_rub
        })

    if db:
        cursor = db.cursor()
        table_name = f'spreadsheet_{spreadsheet_id}'

        if _is_table_exists(table_name):
            cursor.execute(f'TRUNCATE TABLE "{table_name}"')
        else:
            cursor.execute(
                f'CREATE TABLE "{table_name}" ('
                ' id int PRIMARY KEY,'
                ' order_id int NOT NULL,'
                ' cost_in_usd float NOT NULL,'
                ' delivery_at date NOT NULL,'
                ' cost_in_rub float NOT NULL'
                ' )'
            )

        for order_info in orders_info:
            cursor.execute(
                f'INSERT INTO "{table_name}" VALUES (%s, %s, %s, %s, %s)',
                tuple(v for v in order_info.values())
            )
        
        db.commit()

    return orders_info


def _is_table_exists(name: str, *, schema: str = 'public') -> bool:
    cursor = db.cursor()

    cursor.execute(
        "SELECT EXISTS ("
        " SELECT FROM pg_tables WHERE"
        f" schemaname = '{schema}' AND tablename='{name}'"
        " )"
    )

    return cursor.fetchone()[0]


def _parse_text_from_xml_nodes(nodes) -> str:
    records = []

    for node in nodes:
        if node.nodeType == node.TEXT_NODE:
            records.append(node.data)

    return ''.join(records)


def _parse_text_from_xml(element) -> str:
    return _parse_text_from_xml_nodes(element.childNodes)
