---
type: Code Module
title: "aliases"
description: "aliases: Config, AliasedGroup"
resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/examples/aliases/aliases.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/examples/aliases/aliases.py"
    sha256: "ce8e75f58d7a61c9390c5e8734b24caa83e37447d283ce121dc07a61f4801340"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

> `[high]` is stated directly in the source; `[medium]` is a deterministic inference.

# aliases

Source: `examples/aliases/aliases.py`

## Types
- `Config` (class) `examples/aliases/aliases.py:7` `[high]`
- `AliasedGroup` (class) extends `click.core.Group` `examples/aliases/aliases.py:37` `[high]`

## Functions and methods
- `Config.__init__()` `examples/aliases/aliases.py:10` `[high]`
- `Config.add_alias(alias, cmd)` `examples/aliases/aliases.py:14` `[high]`
- `Config.read_config(filename)` `examples/aliases/aliases.py:17` `[high]`
- `Config.write_config(filename)` `examples/aliases/aliases.py:25` `[high]`
- `AliasedGroup.get_command(ctx, cmd_name)` `examples/aliases/aliases.py:42` `[high]`
- `AliasedGroup.resolve_command(ctx, args)` `examples/aliases/aliases.py:70` `[high]`
- `read_config(ctx, param, value)` `examples/aliases/aliases.py:76` `[high]`
- `cli()` `examples/aliases/aliases.py:97` `[high]`
- `push()` `examples/aliases/aliases.py:102` `[high]`
- `pull()` `examples/aliases/aliases.py:108` `[high]`
- `clone()` `examples/aliases/aliases.py:114` `[high]`
- `commit()` `examples/aliases/aliases.py:120` `[high]`
- `status(config)` `examples/aliases/aliases.py:127` `[high]`
- `alias(config, alias_, cmd, config_file)` `examples/aliases/aliases.py:139` `[high]`

## Depends on
- [click](/modules/click.md) `examples/aliases/aliases.py:4` `[high]`

## Calls
- `alias` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/aliases/aliases.py:134` `[medium]`
- `alias` calls [click.decorators](/modules/click.decorators.md) `option` `examples/aliases/aliases.py:136` `[medium]`
- `alias` calls [click.utils](/modules/click.utils.md) `echo` `examples/aliases/aliases.py:143` `[medium]`
- `cli` calls [click.decorators](/modules/click.decorators.md) `command` `examples/aliases/aliases.py:89` `[medium]`
- `cli` calls [click.decorators](/modules/click.decorators.md) `option` `examples/aliases/aliases.py:90` `[medium]`
- `clone` calls [click.utils](/modules/click.utils.md) `echo` `examples/aliases/aliases.py:116` `[medium]`
- `commit` calls [click.utils](/modules/click.utils.md) `echo` `examples/aliases/aliases.py:122` `[medium]`
- `pull` calls [click.utils](/modules/click.utils.md) `echo` `examples/aliases/aliases.py:110` `[medium]`
- `push` calls [click.utils](/modules/click.utils.md) `echo` `examples/aliases/aliases.py:104` `[medium]`
- `status` calls [click.utils](/modules/click.utils.md) `echo` `examples/aliases/aliases.py:129` `[medium]`
- `AliasedGroup.get_command` calls [click.core](/modules/click.core.md) `Group.get_command` `examples/aliases/aliases.py:44` `[medium]`
- `AliasedGroup.get_command` calls [click.core](/modules/click.core.md) `Group.list_commands` `examples/aliases/aliases.py:62` `[medium]`
- `AliasedGroup.resolve_command` calls [click.core](/modules/click.core.md) `Group.resolve_command` `examples/aliases/aliases.py:72` `[medium]`
