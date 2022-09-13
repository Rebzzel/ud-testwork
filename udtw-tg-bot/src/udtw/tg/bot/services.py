import typing as t

from datetime import datetime
from urllib.parse import urljoin

import requests

from . import (
    env,
    models,
)


def fetch_orders_info_from_spreadsheet(spreadsheet_id: str) -> t.List[models.OrderInfo]:
    response = requests.get(
        urljoin(env.API_URL, f'/handle/spreadsheet/{spreadsheet_id}')
    )

    response.raise_for_status()
    raw_orders_info = response.json()
    orders_info = []

    for raw_order_info in raw_orders_info:
        orders_info.append(models.OrderInfo(
            id=raw_order_info['id'],
            order_id=raw_order_info['order_id'],
            cost_in_usd=raw_order_info['cost_in_usd'],
            delivery_at=datetime.strptime(
                raw_order_info['delivery_at'], '%d.%m.%Y'
            ).date(),
            cost_in_rub=raw_order_info['cost_in_rub'],
        ))

    return orders_info


def check_orders_from_spreadsheet(spreadsheet_id: str) -> set:
    orders_info = fetch_orders_info_from_spreadsheet(spreadsheet_id)
    outdated = set()
    today = datetime.now().date()

    for order_info in orders_info:
        if today > order_info.delivery_at:
            outdated.add(order_info.order_id)

    return outdated


__all__ = [
    'fetch_orders_info_from_spreadsheet',
    'check_orders_from_spreadsheet',
]
