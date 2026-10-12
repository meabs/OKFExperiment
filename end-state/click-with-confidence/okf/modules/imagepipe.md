---
type: Code Module
title: "imagepipe"
description: "imagepipe: cli, process_commands, processor, generator"
resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/examples/imagepipe/imagepipe.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/examples/imagepipe/imagepipe.py"
    sha256: "eaf679fc90b988c938b2a32ff4d716d25127fe63a8c3804222628ffe8ec46dc2"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

> `[high]` is stated directly in the source; `[medium]` is a deterministic inference.

# imagepipe

Source: `examples/imagepipe/imagepipe.py`

## Functions and methods
- `cli()` `examples/imagepipe/imagepipe.py:11` `[high]`
- `process_commands(processors)` `examples/imagepipe/imagepipe.py:24` `[high]`
- `processor(f)` `examples/imagepipe/imagepipe.py:42` `[high]`
- `generator(f)` `examples/imagepipe/imagepipe.py:56` `[high]`
- `copy_filename(new, old)` `examples/imagepipe/imagepipe.py:69` `[high]`
- `open_cmd(images)` `examples/imagepipe/imagepipe.py:84` `[high]`
- `save_cmd(images, filename)` `examples/imagepipe/imagepipe.py:110` `[high]`
- `display_cmd(images)` `examples/imagepipe/imagepipe.py:123` `[high]`
- `resize_cmd(images, width, height)` `examples/imagepipe/imagepipe.py:135` `[high]`
- `crop_cmd(images, border)` `examples/imagepipe/imagepipe.py:151` `[high]`
- `convert_rotation(ctx, param, value)` `examples/imagepipe/imagepipe.py:165` `[high]`
- `convert_flip(ctx, param, value)` `examples/imagepipe/imagepipe.py:178` `[high]`
- `transpose_cmd(images, rotate, flip)` `examples/imagepipe/imagepipe.py:195` `[high]`
- `blur_cmd(images, radius)` `examples/imagepipe/imagepipe.py:212` `[high]`
- `smoothen_cmd(images, iterations)` `examples/imagepipe/imagepipe.py:229` `[high]`
- `emboss_cmd(images)` `examples/imagepipe/imagepipe.py:243` `[high]`
- `sharpen_cmd(images, factor)` `examples/imagepipe/imagepipe.py:255` `[high]`
- `paste_cmd(images, left, right)` `examples/imagepipe/imagepipe.py:267` `[high]`

## Depends on
- [click](/modules/click.md) `examples/imagepipe/imagepipe.py:7` `[high]`

## Calls
- `blur_cmd` calls [click.decorators](/modules/click.decorators.md) `option` `examples/imagepipe/imagepipe.py:210` `[medium]`
- `blur_cmd` calls [click.utils](/modules/click.utils.md) `echo` `examples/imagepipe/imagepipe.py:216` `[medium]`
- `cli` calls [click.decorators](/modules/click.decorators.md) `group` `examples/imagepipe/imagepipe.py:10` `[medium]`
- `crop_cmd` calls [click.decorators](/modules/click.decorators.md) `option` `examples/imagepipe/imagepipe.py:147` `[medium]`
- `crop_cmd` calls [click.utils](/modules/click.utils.md) `echo` `examples/imagepipe/imagepipe.py:159` `[medium]`
- `display_cmd` calls [click.utils](/modules/click.utils.md) `echo` `examples/imagepipe/imagepipe.py:126` `[medium]`
- `emboss_cmd` calls [click.utils](/modules/click.utils.md) `echo` `examples/imagepipe/imagepipe.py:246` `[medium]`
- `open_cmd` calls [click.decorators](/modules/click.decorators.md) `option` `examples/imagepipe/imagepipe.py:75` `[medium]`
- `open_cmd` calls [click.utils](/modules/click.utils.md) `echo` `examples/imagepipe/imagepipe.py:90` `[medium]`
- `paste_cmd` calls [click.decorators](/modules/click.decorators.md) `option` `examples/imagepipe/imagepipe.py:264` `[medium]`
- `paste_cmd` calls [click.utils](/modules/click.utils.md) `echo` `examples/imagepipe/imagepipe.py:280` `[medium]`
- `resize_cmd` calls [click.decorators](/modules/click.decorators.md) `option` `examples/imagepipe/imagepipe.py:132` `[medium]`
- `resize_cmd` calls [click.utils](/modules/click.utils.md) `echo` `examples/imagepipe/imagepipe.py:141` `[medium]`
- `save_cmd` calls [click.decorators](/modules/click.decorators.md) `option` `examples/imagepipe/imagepipe.py:102` `[medium]`
- `save_cmd` calls [click.utils](/modules/click.utils.md) `echo` `examples/imagepipe/imagepipe.py:115` `[medium]`
- `sharpen_cmd` calls [click.decorators](/modules/click.decorators.md) `option` `examples/imagepipe/imagepipe.py:251` `[medium]`
- `sharpen_cmd` calls [click.utils](/modules/click.utils.md) `echo` `examples/imagepipe/imagepipe.py:258` `[medium]`
- `smoothen_cmd` calls [click.decorators](/modules/click.decorators.md) `option` `examples/imagepipe/imagepipe.py:221` `[medium]`
- `smoothen_cmd` calls [click.utils](/modules/click.utils.md) `echo` `examples/imagepipe/imagepipe.py:232` `[medium]`
- `transpose_cmd` calls [click.decorators](/modules/click.decorators.md) `option` `examples/imagepipe/imagepipe.py:190` `[medium]`
- `transpose_cmd` calls [click.utils](/modules/click.utils.md) `echo` `examples/imagepipe/imagepipe.py:200` `[medium]`
