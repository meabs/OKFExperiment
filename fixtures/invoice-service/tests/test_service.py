from decimal import Decimal

from invoices import InvoiceService
from ledgerlib import Ledger


def test_create_invoice_posts_a_charge():
    lg = Ledger()
    svc = InvoiceService(lg)
    inv = svc.create_invoice("acme", Decimal("12.50"))
    assert lg.balance("acme").cents == 1250 and svc.get(inv)["total"] == Decimal("12.50")
