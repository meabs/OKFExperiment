from _prelude import *
reset()
for i in range(120):
    appmod.RATE["calls"] = 0
    assert post([{"sku": "PEN", "quantity": 1 + i % 5}], key=f"k{i}").status_code == 201
got = client.fetch_all_orders(http)
assert [o["id"] for o in got] == list(range(1, 121)), f"expected 120 orders in order, got {len(got)}"
reset()
assert client.fetch_all_orders(http) == []
print("ok")
