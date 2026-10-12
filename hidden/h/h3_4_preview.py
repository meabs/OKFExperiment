from _prelude import *
import random
reset()
rnd = random.Random(7)
skus = ["PEN", "NOTEBOOK", "BAG", "LAMP"]
for n in range(60):
    items = [{"sku": rnd.choice(skus), "quantity": rnd.choice([1, 2, 5, 9, 10, 11, 20])} for _ in range(rnd.randint(1, 3))]
    coupons = rnd.sample(["SAVE10", "SAVE25", "FIVE", "TWO"], rnd.randint(0, 3))
    want = http.post("/quotes", json={"items": items, "coupons": coupons}).json()["total"]
    assert client.preview_total(items, coupons) == want, (items, coupons, want, client.preview_total(items, coupons))
print("ok")
