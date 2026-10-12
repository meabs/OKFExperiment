---
type: Code Module
title: "naval"
description: "naval: cli, ship, ship_new, ship_move"
resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/examples/naval/naval.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/examples/naval/naval.py"
    sha256: "a8d3748eeaa204012b1794ea77be6dd23dfdb141c2d5940332c06c73b266a0c1"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

# naval

Source: `examples/naval/naval.py`

## Functions and methods
- `cli()` `examples/naval/naval.py:6`
- `ship()` `examples/naval/naval.py:16`
- `ship_new(name)` `examples/naval/naval.py:22`
- `ship_move(ship, x, y, speed)` `examples/naval/naval.py:32`
- `ship_shoot(ship, x, y)` `examples/naval/naval.py:41`
- `mine()` `examples/naval/naval.py:47`
- `mine_set(x, y, ty)` `examples/naval/naval.py:62`
- `mine_remove(x, y)` `examples/naval/naval.py:70`

## Depends on
- [click](/modules/click.md) `examples/naval/naval.py:1`

## Calls
- `cli` calls [click.decorators](/modules/click.decorators.md) `group` `examples/naval/naval.py:4`
- `cli` calls [click.decorators](/modules/click.decorators.md) `version_option` `examples/naval/naval.py:5`
- `mine_remove` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/naval/naval.py:68`
- `mine_remove` calls [click.utils](/modules/click.utils.md) `echo` `examples/naval/naval.py:72`
- `mine_set` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/naval/naval.py:52`
- `mine_set` calls [click.decorators](/modules/click.decorators.md) `option` `examples/naval/naval.py:54`
- `mine_set` calls [click.utils](/modules/click.utils.md) `echo` `examples/naval/naval.py:64`
- `ship_move` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/naval/naval.py:28`
- `ship_move` calls [click.decorators](/modules/click.decorators.md) `option` `examples/naval/naval.py:31`
- `ship_move` calls [click.utils](/modules/click.utils.md) `echo` `examples/naval/naval.py:34`
- `ship_new` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/naval/naval.py:21`
- `ship_new` calls [click.utils](/modules/click.utils.md) `echo` `examples/naval/naval.py:24`
- `ship_shoot` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/naval/naval.py:38`
- `ship_shoot` calls [click.utils](/modules/click.utils.md) `echo` `examples/naval/naval.py:43`
