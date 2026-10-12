"""Client code for the pricing service, which is a separate repository that runs elsewhere.

`http` is an httpx-style client already bound to the service's base URL, so call it with paths: `http.get("/orders")`.
"""
import time


class OrderError(Exception):
    """Any other failure to place an order."""


class UnknownSku(OrderError):
    """The order named a SKU the catalogue does not have."""


class KeyConflict(OrderError):
    """An idempotency key was reused for a different order."""


def fetch_all_orders(http):
    raise NotImplementedError


def place_order(http, items, coupons, key, sleep=time.sleep):
    raise NotImplementedError


def preview_total(items, coupons):
    raise NotImplementedError
