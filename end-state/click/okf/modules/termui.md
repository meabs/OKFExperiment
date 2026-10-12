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

# termui

Source: `examples/termui/termui.py`

## Functions and methods
- `cli()` `examples/termui/termui.py:9`
- `colordemo()` `examples/termui/termui.py:15`
- `pager()` `examples/termui/termui.py:23`
- `progress(count)` `examples/termui/termui.py:38`
- `open(url)` `examples/termui/termui.py:105`
- `locate(url)` `examples/termui/termui.py:112`
- `edit()` `examples/termui/termui.py:118`
- `clear()` `examples/termui/termui.py:133`
- `pause()` `examples/termui/termui.py:139`
- `menu()` `examples/termui/termui.py:145`

## Depends on
- [click](/modules/click.md) `examples/termui/termui.py:5`

## Calls
- `clear` calls [click.termui](/modules/click.termui.md) `clear` `examples/termui/termui.py:135`
- `cli` calls [click.decorators](/modules/click.decorators.md) `group` `examples/termui/termui.py:8`
- `colordemo` calls [click.termui](/modules/click.termui.md) `style` `examples/termui/termui.py:18`
- `colordemo` calls [click.utils](/modules/click.utils.md) `echo` `examples/termui/termui.py:18`
- `edit` calls [click.termui](/modules/click.termui.md) `edit` `examples/termui/termui.py:121`
- `edit` calls [click.utils](/modules/click.utils.md) `echo` `examples/termui/termui.py:125`
- `locate` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/termui/termui.py:111`
- `locate` calls [click.termui](/modules/click.termui.md) `launch` `examples/termui/termui.py:114`
- `menu` calls [click.termui](/modules/click.termui.md) `getchar` `examples/termui/termui.py:153`
- `menu` calls [click.utils](/modules/click.utils.md) `echo` `examples/termui/termui.py:150`
- `open` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/termui/termui.py:104`
- `open` calls [click.termui](/modules/click.termui.md) `launch` `examples/termui/termui.py:107`
- `pager` calls [click.termui](/modules/click.termui.md) `echo_via_pager` `examples/termui/termui.py:28`
- `pager` calls [click.termui](/modules/click.termui.md) `style` `examples/termui/termui.py:27`
- `pause` calls [click.termui](/modules/click.termui.md) `pause` `examples/termui/termui.py:141`
- `progress` calls [click._termui_impl](/modules/click._termui_impl.md) `ProgressBar.update` `examples/termui/termui.py:100`
- `progress` calls [click.decorators](/modules/click.decorators.md) `option` `examples/termui/termui.py:32`
- `progress` calls [click.termui](/modules/click.termui.md) `progressbar` `examples/termui/termui.py:50`
- `progress` calls [click.termui](/modules/click.termui.md) `style` `examples/termui/termui.py:51`
