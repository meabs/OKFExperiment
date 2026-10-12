---
type: Code Module
title: "validation"
description: "validation: URL"
resource: "repo:examples/validation/validation.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "repo:examples/validation/validation.py"
    id: "246c4962fff1"
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
