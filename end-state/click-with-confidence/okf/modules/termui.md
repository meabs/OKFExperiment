---
type: Code Module
title: "termui"
description: "termui: cli, colordemo, pager, progress"
resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/examples/termui/termui.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/examples/termui/termui.py"
    sha256: "cc79721d0e7250c9aa23cfafb4f897cd1fd25711371ae58aab616760be47381d"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

> `[high]` is stated directly in the source; `[medium]` is a deterministic inference.

# termui

Source: `examples/termui/termui.py`

## Functions and methods
- `cli()` `examples/termui/termui.py:9` `[high]`
- `colordemo()` `examples/termui/termui.py:15` `[high]`
- `pager()` `examples/termui/termui.py:23` `[high]`
- `progress(count)` `examples/termui/termui.py:38` `[high]`
- `open(url)` `examples/termui/termui.py:105` `[high]`
- `locate(url)` `examples/termui/termui.py:112` `[high]`
- `edit()` `examples/termui/termui.py:118` `[high]`
- `clear()` `examples/termui/termui.py:133` `[high]`
- `pause()` `examples/termui/termui.py:139` `[high]`
- `menu()` `examples/termui/termui.py:145` `[high]`

## Depends on
- [click](/modules/click.md) `examples/termui/termui.py:5` `[high]`

## Calls
- `clear` calls [click.termui](/modules/click.termui.md) `clear` `examples/termui/termui.py:135` `[medium]`
- `cli` calls [click.decorators](/modules/click.decorators.md) `group` `examples/termui/termui.py:8` `[medium]`
- `colordemo` calls [click.termui](/modules/click.termui.md) `style` `examples/termui/termui.py:18` `[medium]`
- `colordemo` calls [click.utils](/modules/click.utils.md) `echo` `examples/termui/termui.py:18` `[medium]`
- `edit` calls [click.termui](/modules/click.termui.md) `edit` `examples/termui/termui.py:121` `[medium]`
- `edit` calls [click.utils](/modules/click.utils.md) `echo` `examples/termui/termui.py:125` `[medium]`
- `locate` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/termui/termui.py:111` `[medium]`
- `locate` calls [click.termui](/modules/click.termui.md) `launch` `examples/termui/termui.py:114` `[medium]`
- `menu` calls [click.termui](/modules/click.termui.md) `getchar` `examples/termui/termui.py:153` `[medium]`
- `menu` calls [click.utils](/modules/click.utils.md) `echo` `examples/termui/termui.py:150` `[medium]`
- `open` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/termui/termui.py:104` `[medium]`
- `open` calls [click.termui](/modules/click.termui.md) `launch` `examples/termui/termui.py:107` `[medium]`
- `pager` calls [click.termui](/modules/click.termui.md) `echo_via_pager` `examples/termui/termui.py:28` `[medium]`
- `pager` calls [click.termui](/modules/click.termui.md) `style` `examples/termui/termui.py:27` `[medium]`
- `pause` calls [click.termui](/modules/click.termui.md) `pause` `examples/termui/termui.py:141` `[medium]`
- `progress` calls [click._termui_impl](/modules/click._termui_impl.md) `ProgressBar.update` `examples/termui/termui.py:100` `[medium]`
- `progress` calls [click.decorators](/modules/click.decorators.md) `option` `examples/termui/termui.py:32` `[medium]`
- `progress` calls [click.termui](/modules/click.termui.md) `progressbar` `examples/termui/termui.py:50` `[medium]`
- `progress` calls [click.termui](/modules/click.termui.md) `style` `examples/termui/termui.py:51` `[medium]`
