---
type: Code Module
title: "ledgerlib.ledger"
description: "ledgerlib.ledger: Ledger"
resource: "https://github.com/meabs/OKFExperiment/blob/main/fixtures/ledger-lib/ledgerlib/ledger.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-12T13:50:42+01:00"
sources:
  - resource: "https://github.com/meabs/OKFExperiment/blob/main/fixtures/ledger-lib/ledgerlib/ledger.py"
    sha256: "5ed69f2c3031649838b55868b2e7fd3150916d5a5d19da7ac91fcb5b4d37d856"
    last_modified: "2026-10-12T13:50:42+01:00"
status: stable
---

# ledgerlib.ledger

Source: `ledgerlib/ledger.py`

## Types
- `Ledger` (class) `ledgerlib/ledger.py:13`

## Functions and methods
- `Ledger.__init__()` `ledgerlib/ledger.py:14`
- `Ledger.post(entry: Entry) -> str` `ledgerlib/ledger.py:19`
- `Ledger.get(entry_id: str) -> Entry` `ledgerlib/ledger.py:31`
- `Ledger.find_reversal(entry_id: str) -> str | None` `ledgerlib/ledger.py:34`
- `Ledger.reverse(entry_id: str, reason: str, key: str, amount: Money | None) -> str` `ledgerlib/ledger.py:40`
- `Ledger.balance(account: str) -> Money` `ledgerlib/ledger.py:49`
- `Ledger.entries(account: str) -> list[Entry]` `ledgerlib/ledger.py:52`

## Depends on
- [ledgerlib.entries](/references/ledger-lib/modules/ledgerlib.entries.md) `ledgerlib/ledger.py:6`
- [ledgerlib.errors](/references/ledger-lib/modules/ledgerlib.errors.md) `ledgerlib/ledger.py:7`
- [ledgerlib.money](/references/ledger-lib/modules/ledgerlib.money.md) `ledgerlib/ledger.py:8`

## Tests
- `test_ledger`
