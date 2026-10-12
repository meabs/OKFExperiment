# Pricing service notes

- All money is integer cents (EUR).
- `POST /quotes` takes `items` (`sku`, `quantity`) and `coupons` (codes) and returns the price breakdown.
- `POST /orders` takes the same body and needs an `Idempotency-Key` header. It stores the order and returns it.
- Order creation is rate limited. A 429 response carries a `Retry-After` header in seconds.
- `GET /orders` is cursor paginated: query `limit` and `cursor`; the response has `next_cursor`, which is null on the last page.
