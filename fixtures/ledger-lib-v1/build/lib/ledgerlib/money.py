from __future__ import annotations

from dataclasses import dataclass
from decimal import ROUND_HALF_EVEN, Decimal


@dataclass(frozen=True)
class Money:
    """An amount in the smallest currency unit (cents)."""

    cents: int
    currency: str = "USD"

    @classmethod
    def from_decimal(cls, amount: Decimal, currency: str = "USD") -> "Money":
        return cls(int((Decimal(amount) * 100).quantize(Decimal("1"), rounding=ROUND_HALF_EVEN)), currency)

    def to_decimal(self) -> Decimal:
        return Decimal(self.cents) / 100

    def negate(self) -> "Money":
        return Money(-self.cents, self.currency)
