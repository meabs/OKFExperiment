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

# imagepipe

Source: `examples/imagepipe/imagepipe.py`

## Functions and methods
- `cli()` `examples/imagepipe/imagepipe.py:11`
- `process_commands(processors)` `examples/imagepipe/imagepipe.py:24`
- `processor(f)` `examples/imagepipe/imagepipe.py:42`
- `generator(f)` `examples/imagepipe/imagepipe.py:56`
- `copy_filename(new, old)` `examples/imagepipe/imagepipe.py:69`
- `open_cmd(images)` `examples/imagepipe/imagepipe.py:84`
- `save_cmd(images, filename)` `examples/imagepipe/imagepipe.py:110`
- `display_cmd(images)` `examples/imagepipe/imagepipe.py:123`
- `resize_cmd(images, width, height)` `examples/imagepipe/imagepipe.py:135`
- `crop_cmd(images, border)` `examples/imagepipe/imagepipe.py:151`
- `convert_rotation(ctx, param, value)` `examples/imagepipe/imagepipe.py:165`
- `convert_flip(ctx, param, value)` `examples/imagepipe/imagepipe.py:178`
- `transpose_cmd(images, rotate, flip)` `examples/imagepipe/imagepipe.py:195`
- `blur_cmd(images, radius)` `examples/imagepipe/imagepipe.py:212`
- `smoothen_cmd(images, iterations)` `examples/imagepipe/imagepipe.py:229`
- `emboss_cmd(images)` `examples/imagepipe/imagepipe.py:243`
- `sharpen_cmd(images, factor)` `examples/imagepipe/imagepipe.py:255`
- `paste_cmd(images, left, right)` `examples/imagepipe/imagepipe.py:267`

## Depends on
- [click](/modules/click.md) `examples/imagepipe/imagepipe.py:7`

## Calls
- `blur_cmd` calls [click.decorators](/modules/click.decorators.md) `option` `examples/imagepipe/imagepipe.py:210`
- `blur_cmd` calls [click.utils](/modules/click.utils.md) `echo` `examples/imagepipe/imagepipe.py:216`
- `cli` calls [click.decorators](/modules/click.decorators.md) `group` `examples/imagepipe/imagepipe.py:10`
- `crop_cmd` calls [click.decorators](/modules/click.decorators.md) `option` `examples/imagepipe/imagepipe.py:147`
- `crop_cmd` calls [click.utils](/modules/click.utils.md) `echo` `examples/imagepipe/imagepipe.py:159`
- `display_cmd` calls [click.utils](/modules/click.utils.md) `echo` `examples/imagepipe/imagepipe.py:126`
- `emboss_cmd` calls [click.utils](/modules/click.utils.md) `echo` `examples/imagepipe/imagepipe.py:246`
- `open_cmd` calls [click.decorators](/modules/click.decorators.md) `option` `examples/imagepipe/imagepipe.py:75`
- `open_cmd` calls [click.utils](/modules/click.utils.md) `echo` `examples/imagepipe/imagepipe.py:90`
- `paste_cmd` calls [click.decorators](/modules/click.decorators.md) `option` `examples/imagepipe/imagepipe.py:264`
- `paste_cmd` calls [click.utils](/modules/click.utils.md) `echo` `examples/imagepipe/imagepipe.py:280`
- `resize_cmd` calls [click.decorators](/modules/click.decorators.md) `option` `examples/imagepipe/imagepipe.py:132`
- `resize_cmd` calls [click.utils](/modules/click.utils.md) `echo` `examples/imagepipe/imagepipe.py:141`
- `save_cmd` calls [click.decorators](/modules/click.decorators.md) `option` `examples/imagepipe/imagepipe.py:102`
- `save_cmd` calls [click.utils](/modules/click.utils.md) `echo` `examples/imagepipe/imagepipe.py:115`
- `sharpen_cmd` calls [click.decorators](/modules/click.decorators.md) `option` `examples/imagepipe/imagepipe.py:251`
- `sharpen_cmd` calls [click.utils](/modules/click.utils.md) `echo` `examples/imagepipe/imagepipe.py:258`
- `smoothen_cmd` calls [click.decorators](/modules/click.decorators.md) `option` `examples/imagepipe/imagepipe.py:221`
- `smoothen_cmd` calls [click.utils](/modules/click.utils.md) `echo` `examples/imagepipe/imagepipe.py:232`
- `transpose_cmd` calls [click.decorators](/modules/click.decorators.md) `option` `examples/imagepipe/imagepipe.py:190`
- `transpose_cmd` calls [click.utils](/modules/click.utils.md) `echo` `examples/imagepipe/imagepipe.py:200`
