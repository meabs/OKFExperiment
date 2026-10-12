from __future__ import annotations

import enum
from dataclasses import dataclass

from .money import Money


class EntryKind(enum.Enum):
    CHARGE = "charge"
    REFUND = "refund"
    ADJUSTMENT = "adjustment"


@dataclass(frozen=True)
class Entry:
    account: str
    money: Money
    kind: EntryKind
    key: str
    memo: str = ""
    reverses: str | None = None
