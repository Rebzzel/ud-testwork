import dataclasses as dc
import typing as t

from datetime import date


@dc.dataclass
class OrderInfo:
    id: int
    order_id: int
    cost_in_usd: int
    delivery_at: date
    cost_in_rub: int


__all__ = [
    'OrderInfo',
]
