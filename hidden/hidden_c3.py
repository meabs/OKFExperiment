from decimal import Decimal

from invoices import InvoiceService
from ledgerlib import Ledger


def test_customer_balance_is_a_decimal_in_currency_units():
    lg = Ledger(); svc = InvoiceService(lg)
    svc.create_invoice("acme", Decimal("12.50")); svc.create_invoice("acme", Decimal("0.05")); svc.create_invoice("other", Decimal("3"))
    bal = svc.customer_balance("acme")
    assert isinstance(bal, Decimal) and bal == Decimal("12.55")
    assert svc.customer_balance("nobody") == Decimal("0")
