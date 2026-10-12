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

> `[high]` is stated directly in the source; `[medium]` is a deterministic inference.

# naval

Source: `examples/naval/naval.py`

## Functions and methods
- `cli()` `examples/naval/naval.py:6` `[high]`
- `ship()` `examples/naval/naval.py:16` `[high]`
- `ship_new(name)` `examples/naval/naval.py:22` `[high]`
- `ship_move(ship, x, y, speed)` `examples/naval/naval.py:32` `[high]`
- `ship_shoot(ship, x, y)` `examples/naval/naval.py:41` `[high]`
- `mine()` `examples/naval/naval.py:47` `[high]`
- `mine_set(x, y, ty)` `examples/naval/naval.py:62` `[high]`
- `mine_remove(x, y)` `examples/naval/naval.py:70` `[high]`

## Depends on
- [click](/modules/click.md) `examples/naval/naval.py:1` `[high]`

## Calls
- `cli` calls [click.decorators](/modules/click.decorators.md) `group` `examples/naval/naval.py:4` `[medium]`
- `cli` calls [click.decorators](/modules/click.decorators.md) `version_option` `examples/naval/naval.py:5` `[medium]`
- `mine_remove` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/naval/naval.py:68` `[medium]`
- `mine_remove` calls [click.utils](/modules/click.utils.md) `echo` `examples/naval/naval.py:72` `[medium]`
- `mine_set` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/naval/naval.py:52` `[medium]`
- `mine_set` calls [click.decorators](/modules/click.decorators.md) `option` `examples/naval/naval.py:54` `[medium]`
- `mine_set` calls [click.utils](/modules/click.utils.md) `echo` `examples/naval/naval.py:64` `[medium]`
- `ship_move` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/naval/naval.py:28` `[medium]`
- `ship_move` calls [click.decorators](/modules/click.decorators.md) `option` `examples/naval/naval.py:31` `[medium]`
- `ship_move` calls [click.utils](/modules/click.utils.md) `echo` `examples/naval/naval.py:34` `[medium]`
- `ship_new` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/naval/naval.py:21` `[medium]`
- `ship_new` calls [click.utils](/modules/click.utils.md) `echo` `examples/naval/naval.py:24` `[medium]`
- `ship_shoot` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/naval/naval.py:38` `[medium]`
- `ship_shoot` calls [click.utils](/modules/click.utils.md) `echo` `examples/naval/naval.py:43` `[medium]`
