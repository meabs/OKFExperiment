from decimal import Decimal

import pytest

from ledgerlib import AlreadyReversed, DuplicateKey, Entry, EntryKind, InvalidKey, Ledger, Money


def test_post_reverse_and_balance():
    lg = Ledger()
    eid = lg.post(Entry("acct", Money.from_decimal(Decimal("10.005")), EntryKind.CHARGE, "invoice:abc123"))
    assert lg.get(eid).money.cents == 1000
    rid = lg.reverse(eid, "oops", key="refund:abc123")
    assert lg.balance("acct").cents == 0 and lg.find_reversal(eid) == rid
    with pytest.raises(AlreadyReversed):
        lg.reverse(eid, "again", key="refund:abc124")


def test_keys():
    lg = Ledger()
    lg.post(Entry("a", Money(5), EntryKind.CHARGE, "invoice:abc123"))
    with pytest.raises(DuplicateKey):
        lg.post(Entry("a", Money(5), EntryKind.CHARGE, "invoice:abc123"))
    with pytest.raises(InvalidKey):
        lg.post(Entry("a", Money(5), EntryKind.CHARGE, "bad key"))
