from enum import Enum


class Order(Enum):
    ASCENDING = "ascending"
    DESCENDING = "descending"


class Sort():
    def __init__(self, key: str, order: Order) -> None:
        self._sort = {
            "key": key,
            "order": order.value
        }
