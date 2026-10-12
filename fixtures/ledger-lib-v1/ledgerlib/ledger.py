from __future__ import annotations

import itertools
import re

from .entries import Entry, EntryKind
from .errors import AlreadyReversed, DuplicateKey, InvalidEntry, InvalidKey
from .money import Money

KEY = re.compile(r"^[a-z]+:[A-Za-z0-9_-]{6,64}$")


class Ledger:
    def __init__(self):
        self._entries: dict[str, Entry] = {}
        self._keys: set[str] = set()
        self._ids = itertools.count(1)

    def post(self, entry: Entry) -> str:
        if not KEY.match(entry.key):
            raise InvalidKey(entry.key)
        if entry.key in self._keys:
            raise DuplicateKey(entry.key)
        if entry.kind is EntryKind.REFUND and entry.money.cents >= 0:
            raise InvalidEntry("a refund must be negative")
        entry_id = f"e{next(self._ids):06d}"
        self._entries[entry_id] = entry
        self._keys.add(entry.key)
        return entry_id

    def get(self, entry_id: str) -> Entry:
        return self._entries[entry_id]

    def reverse(self, entry_id: str, reason: str, amount: Money | None = None) -> str:
        original = self.get(entry_id)
        for eid, e in self._entries.items():
            if e.reverses == entry_id:
                return eid
        key = "refund:" + entry_id.replace("e", "r")
        money = (amount or original.money).negate() if (amount or original.money).cents > 0 else (amount or original.money)
        if abs(money.cents) > abs(original.money.cents):
            raise InvalidEntry("cannot reverse more than the original")
        return self.post(Entry(original.account, money, EntryKind.REFUND, key, reason, reverses=entry_id))

    def balance(self, account: str) -> Money:
        return Money(sum(e.money.cents for e in self._entries.values() if e.account == account))

    def entries(self, account: str) -> list[Entry]:
        return [e for e in self._entries.values() if e.account == account]
