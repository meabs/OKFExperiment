from decimal import Decimal

import pytest
from invoices import InvoiceService
from ledgerlib import AlreadyReversed, InvalidEntry, Ledger


def test_partial_refund_reduces_the_balance_by_the_amount():
    lg = Ledger(); svc = InvoiceService(lg)
    inv = svc.create_invoice("acme", Decimal("12.50"))
    rid = svc.refund_invoice_partial(inv, Decimal("5.00"), "late delivery")
    assert lg.balance("acme").cents == 750 and lg.get(rid).money.cents == -500


def test_more_than_the_total_is_rejected():
    lg = Ledger(); svc = InvoiceService(lg)
    inv = svc.create_invoice("acme", Decimal("12.50"))
    with pytest.raises(InvalidEntry):
        svc.refund_invoice_partial(inv, Decimal("20.00"), "too much")
    assert lg.balance("acme").cents == 1250


def test_only_one_refund_per_invoice():
    lg = Ledger(); svc = InvoiceService(lg)
    inv = svc.create_invoice("acme", Decimal("12.50"))
    svc.refund_invoice_partial(inv, Decimal("5.00"), "a")
    with pytest.raises(AlreadyReversed):
        svc.refund_invoice_partial(inv, Decimal("1.00"), "b")
