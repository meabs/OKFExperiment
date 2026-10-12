from __future__ import annotations

from decimal import Decimal

from ledgerlib import Entry, EntryKind, Ledger, Money


class InvoiceNotFound(KeyError):
    pass


class InvoiceService:
    def __init__(self, ledger: Ledger):
        self.ledger = ledger
        self._invoices: dict[str, dict] = {}
        self._seq = 0

    def create_invoice(self, customer: str, total: Decimal, currency: str = "USD") -> str:
        self._seq += 1
        invoice_id = f"inv-{self._seq:05d}"
        entry_id = self.ledger.post(Entry(customer, Money.from_decimal(total, currency), EntryKind.CHARGE, f"invoice:{invoice_id}", memo=invoice_id))
        self._invoices[invoice_id] = {"customer": customer, "total": total, "entry_id": entry_id}
        return invoice_id

    def get(self, invoice_id: str) -> dict:
        try:
            return self._invoices[invoice_id]
        except KeyError:
            raise InvoiceNotFound(invoice_id) from None
