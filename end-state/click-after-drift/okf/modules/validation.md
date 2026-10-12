---
type: Code Module
title: "validation"
description: "validation: URL"
resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/examples/validation/validation.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/examples/validation/validation.py"
    sha256: "246c4962fff19bbf12cf620e141a904ac9059698f0002c11833bb882f492786f"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

# validation

Source: `examples/validation/validation.py`

## Types
- `URL` (class) extends `click.ParamType[urlparse.ParseResult]` `examples/validation/validation.py:12`

## Functions and methods
- `validate_count(ctx, param, value)` `examples/validation/validation.py:6`
- `URL.convert(value, param, ctx) -> urlparse.ParseResult` `examples/validation/validation.py:15`
- `cli(count, foo, url)` `examples/validation/validation.py:34`

## Depends on
- [click](/modules/click.md) `examples/validation/validation.py:3`

## Calls
- `cli` calls [click.decorators](/modules/click.decorators.md) `command` `examples/validation/validation.py:27`
- `cli` calls [click.decorators](/modules/click.decorators.md) `option` `examples/validation/validation.py:28`
- `cli` calls [click.decorators](/modules/click.decorators.md) `version_option` `examples/validation/validation.py:33`
- `cli` calls [click.utils](/modules/click.utils.md) `echo` `examples/validation/validation.py:46`
