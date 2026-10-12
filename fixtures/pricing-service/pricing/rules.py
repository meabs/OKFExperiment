"""Price rules. All amounts are integer cents."""
from decimal import Decimal, ROUND_HALF_EVEN

CATALOGUE = {"PEN": 150, "NOTEBOOK": 1250, "BAG": 4999, "LAMP": 3500}
COUPONS = {"SAVE10": ("percent", 10), "SAVE25": ("percent", 25), "FIVE": ("fixed", 500), "TWO": ("fixed", 200)}
SHIPPING_FLAT = 599
FREE_SHIPPING_FROM = 5000
MAX_QUANTITY = 20


def line_total(sku: str, quantity: int) -> int:
    unit = CATALOGUE[sku]
    total = unit * quantity
    if quantity >= 10:  # bulk price: 5% off the line
        total = _round(Decimal(total) * Decimal("0.95"))
    return total


def _round(x: Decimal) -> int:
    return int(x.quantize(Decimal(1), rounding=ROUND_HALF_EVEN))


def apply_coupons(subtotal: int, codes: list[str]) -> tuple[int, list[str]]:
    """Fixed coupons stack and come off first; then only the single best percent coupon applies. Never below zero."""
    applied = []
    total = subtotal
    for c in codes:
        kind, value = COUPONS[c]
        if kind == "fixed":
            total -= value
            applied.append(c)
    percents = sorted((c for c in codes if COUPONS[c][0] == "percent"), key=lambda c: -COUPONS[c][1])
    if percents:
        best = percents[0]
        total = _round(Decimal(max(total, 0)) * (Decimal(100 - COUPONS[best][1]) / Decimal(100)))
        applied.append(best)
    return max(total, 0), applied


def shipping(discounted: int) -> int:
    return 0 if discounted >= FREE_SHIPPING_FROM else SHIPPING_FLAT
