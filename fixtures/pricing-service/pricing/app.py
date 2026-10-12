import base64
import time
from fastapi import FastAPI, Header, HTTPException, Query, Response
from pydantic import BaseModel

from . import rules

app = FastAPI(title="Pricing service", version="1.0")

ORDERS: list[dict] = []
IDEMPOTENT: dict[str, tuple[str, dict]] = {}
RATE = {"calls": 0, "limit": 5}


class Item(BaseModel):
    sku: str
    quantity: int


class OrderIn(BaseModel):
    items: list[Item]
    coupons: list[str] = []
    currency: str = "EUR"


class Quote(BaseModel):
    subtotal: int
    discount: int
    shipping: int
    total: int
    applied_coupons: list[str]


class Order(BaseModel):
    id: int
    quote: Quote


class OrderPage(BaseModel):
    orders: list[Order]
    next_cursor: str | None


def _quote(body: OrderIn) -> Quote:
    if body.currency != "EUR":
        raise HTTPException(422, "unsupported currency")
    subtotal = 0
    for it in body.items:
        if it.sku not in rules.CATALOGUE:
            raise HTTPException(404, f"unknown sku {it.sku}")
        if not 1 <= it.quantity <= rules.MAX_QUANTITY:
            raise HTTPException(422, "quantity out of range")
        subtotal += rules.line_total(it.sku, it.quantity)
    for c in body.coupons:
        if c not in rules.COUPONS:
            raise HTTPException(422, f"unknown coupon {c}")
    discounted, applied = rules.apply_coupons(subtotal, body.coupons)
    ship = rules.shipping(discounted)
    return Quote(subtotal=subtotal, discount=subtotal - discounted, shipping=ship, total=discounted + ship, applied_coupons=applied)


@app.post("/quotes", response_model=Quote)
def quote(body: OrderIn) -> Quote:
    return _quote(body)


@app.post("/orders", response_model=Order, status_code=201, responses={429: {"description": "Too many requests"}})
def create_order(body: OrderIn, response: Response, idempotency_key: str = Header(...)) -> Order:
    RATE["calls"] += 1
    if RATE["calls"] > RATE["limit"]:
        RATE["calls"] = 0
        raise HTTPException(429, "slow down", headers={"Retry-After": "2"})
    digest = body.model_dump_json()
    if idempotency_key in IDEMPOTENT:
        stored_digest, stored = IDEMPOTENT[idempotency_key]
        if stored_digest != digest:
            raise HTTPException(409, "idempotency key reused with a different body")
        response.status_code = 200
        return Order(**stored)
    order = {"id": len(ORDERS) + 1, "quote": _quote(body).model_dump()}
    ORDERS.append(order)
    IDEMPOTENT[idempotency_key] = (digest, order)
    return Order(**order)


@app.get("/orders", response_model=OrderPage)
def list_orders(cursor: str | None = None, limit: int = Query(10)) -> OrderPage:
    limit = min(max(limit, 1), 50)
    start = int(base64.urlsafe_b64decode(cursor).decode().split(":")[1]) if cursor else 0
    page = ORDERS[start:start + limit]
    nxt = base64.urlsafe_b64encode(f"o:{start + limit}".encode()).decode() if start + limit < len(ORDERS) else None
    return OrderPage(orders=[Order(**o) for o in page], next_cursor=nxt)
