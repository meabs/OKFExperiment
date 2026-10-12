import sys
p=sys.argv[1]+'/invoices/service.py';s=open(p).read()
s=s.replace("from ledgerlib import Entry,","from ledgerlib import AlreadyReversed, Entry,",1) if False else s
s+='''
    def refund_invoice(self, invoice_id: str, reason: str) -> str:
        inv = self.get(invoice_id)
        existing = self.ledger.find_reversal(inv["entry_id"])
        if existing:
            return existing
        return self.ledger.reverse(inv["entry_id"], reason, key=f"refund:{invoice_id}")

    def refund_invoice_partial(self, invoice_id: str, amount: Decimal, reason: str) -> str:
        inv = self.get(invoice_id)
        return self.ledger.reverse(inv["entry_id"], reason, key=f"refund:{invoice_id}", amount=Money.from_decimal(amount))

    def customer_balance(self, customer: str) -> Decimal:
        return self.ledger.balance(customer).to_decimal()
'''
open(p,'w').write(s)
