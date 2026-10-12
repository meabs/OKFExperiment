---
type: Code Module
title: "invoices.service"
description: "invoices.service: InvoiceNotFound, InvoiceService"
resource: "repo:invoices/service.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-12T13:50:42+01:00"
sources:
  - resource: "repo:invoices/service.py"
    id: "b383f2fe730d"
    last_modified: "2026-10-12T13:50:42+01:00"
status: stable
---

# invoices.service

Source: `invoices/service.py`

## Types
- `InvoiceNotFound` (class) extends `KeyError` `invoices/service.py:8`
- `InvoiceService` (class) `invoices/service.py:12`

## Functions and methods
- `InvoiceService.__init__(ledger: Ledger)` `invoices/service.py:13`
- `InvoiceService.create_invoice(customer: str, total: Decimal, currency: str) -> str` `invoices/service.py:18`
- `InvoiceService.get(invoice_id: str) -> dict` `invoices/service.py:25`

## Tests
- `test_service`
