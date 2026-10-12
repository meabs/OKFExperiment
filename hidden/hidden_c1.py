from decimal import Decimal

import pytest
from invoices import InvoiceNotFound, InvoiceService
from ledgerlib import Ledger


def test_full_refund_zeroes_the_balance():
    lg = Ledger(); svc = InvoiceService(lg)
    inv = svc.create_invoice("acme", Decimal("12.50"))
    rid = svc.refund_invoice(inv, "customer asked")
    assert lg.balance("acme").cents == 0 and lg.get(rid).reverses == svc.get(inv)["entry_id"]


def test_refund_twice_is_safe():
    lg = Ledger(); svc = InvoiceService(lg)
    inv = svc.create_invoice("acme", Decimal("12.50"))
    first = svc.refund_invoice(inv, "once")
    assert svc.refund_invoice(inv, "twice") == first
    assert len(lg.entries("acme")) == 2


def test_unknown_invoice():
    with pytest.raises(InvoiceNotFound):
        InvoiceService(Ledger()).refund_invoice("inv-99999", "x")
