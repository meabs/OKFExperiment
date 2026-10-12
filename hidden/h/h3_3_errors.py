from _prelude import *
reset()
c = client
try:
    c.place_order(http, [{"sku": "NOPE", "quantity": 1}], [], "a", sleep=lambda s: None); raise SystemExit("expected UnknownSku")
except c.UnknownSku:
    pass
ok = c.place_order(http, [{"sku": "PEN", "quantity": 1}], [], "b", sleep=lambda s: None)
try:
    c.place_order(http, [{"sku": "BAG", "quantity": 1}], [], "b", sleep=lambda s: None); raise SystemExit("expected KeyConflict")
except c.KeyConflict:
    pass
try:
    c.place_order(http, [{"sku": "PEN", "quantity": 99}], [], "c", sleep=lambda s: None); raise SystemExit("expected OrderError")
except c.OrderError as e:
    assert not isinstance(e, (c.UnknownSku, c.KeyConflict))
print("ok")
