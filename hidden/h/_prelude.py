import os, sys, importlib
import tarfile, tempfile
_tmp = tempfile.mkdtemp(prefix="t")
tarfile.open(os.environ["PRICING_SERVICE_TGZ"]).extractall(_tmp)   # the real service exists on disk only while a test runs
SVC = os.path.join(_tmp, "pricing-service")
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
