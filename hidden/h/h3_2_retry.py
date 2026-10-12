from _prelude import *
reset()
sleeps = []
items = [{"sku": "NOTEBOOK", "quantity": 2}]
for i in range(5):
    assert post(items, key=f"warm{i}").status_code == 201        # the sixth create call in a row is rate limited
before = len(appmod.ORDERS)
order = client.place_order(http, items, [], "mine", sleep=sleeps.append)
assert order["quote"]["total"] == 2 * 1250 + 599, order
assert len(appmod.ORDERS) == before + 1, "the order must exist exactly once"
assert sleeps == [2] or sleeps == [2.0], f"must wait as long as the service asks, slept {sleeps}"
# a repeat of the same call returns the same order and creates nothing
again = client.place_order(http, items, [], "mine", sleep=sleeps.append)
assert again["id"] == order["id"] and len(appmod.ORDERS) == before + 1
print("ok")
