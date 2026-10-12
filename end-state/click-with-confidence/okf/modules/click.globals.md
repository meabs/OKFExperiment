---
type: Code Module
title: "click.globals"
description: "click.globals: get_current_context, push_context, pop_context, resolve_color_default"
resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/globals.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/globals.py"
    sha256: "80cf8d87a0383341c1fd2824685e4ce2770618c0c773f7e51d7bbdfe88781845"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

> `[high]` is stated directly in the source; `[medium]` is a deterministic inference.

# click.globals

Source: `src/click/globals.py`

## Functions and methods
- `get_current_context(silent: bool) -> Context | None` `src/click/globals.py:20` `[high]`
- `push_context(ctx: Context) -> None` `src/click/globals.py:44` `[high]`
- `pop_context() -> None` `src/click/globals.py:49` `[high]`
- `resolve_color_default(color: bool | None) -> bool | None` `src/click/globals.py:54` `[high]`

## Depends on
- [click.core](/modules/click.core.md) `src/click/globals.py:7` `[high]`
