import os, sys, importlib
SVC = os.environ["PRICING_SERVICE"]          # the real service, used only by the test
sys.path.insert(0, SVC)
sys.path.insert(0, os.getcwd())               # the agent's working copy of shop-client
from fastapi.testclient import TestClient
from pricing import app as appmod
http = TestClient(appmod.app)
def reset():
    appmod.ORDERS.clear(); appmod.IDEMPOTENT.clear(); appmod.RATE["calls"] = 0
def post(items, coupons=(), key="k"):
    return http.post("/orders", json={"items": items, "coupons": list(coupons)}, headers={"Idempotency-Key": key})
client = importlib.import_module("shop.client")
