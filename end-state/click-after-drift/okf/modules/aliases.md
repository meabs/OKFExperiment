---
type: Code Module
title: "aliases"
description: "aliases: Config, AliasedGroup"
resource: "repo:examples/aliases/aliases.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "repo:examples/aliases/aliases.py"
    id: "ce8e75f58d7a"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

# aliases

Source: `examples/aliases/aliases.py`

## Types
- `Config` (class) `examples/aliases/aliases.py:7`
- `AliasedGroup` (class) extends `click.core.Group` `examples/aliases/aliases.py:37`

## Functions and methods
- `Config.__init__()` `examples/aliases/aliases.py:10`
- `Config.add_alias(alias, cmd)` `examples/aliases/aliases.py:14`
- `Config.read_config(filename)` `examples/aliases/aliases.py:17`
- `Config.write_config(filename)` `examples/aliases/aliases.py:25`
- `AliasedGroup.get_command(ctx, cmd_name)` `examples/aliases/aliases.py:42`
- `AliasedGroup.resolve_command(ctx, args)` `examples/aliases/aliases.py:70`
- `read_config(ctx, param, value)` `examples/aliases/aliases.py:76`
- `cli()` `examples/aliases/aliases.py:97`
- `push()` `examples/aliases/aliases.py:102`
- `pull()` `examples/aliases/aliases.py:108`
- `clone()` `examples/aliases/aliases.py:114`
- `commit()` `examples/aliases/aliases.py:120`
- `status(config)` `examples/aliases/aliases.py:127`
- `alias(config, alias_, cmd, config_file)` `examples/aliases/aliases.py:139`

## Depends on
- [click](/modules/click.md) `examples/aliases/aliases.py:4`

## Calls
- `alias` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/aliases/aliases.py:134`
- `alias` calls [click.decorators](/modules/click.decorators.md) `option` `examples/aliases/aliases.py:136`
- `alias` calls [click.utils](/modules/click.utils.md) `echo` `examples/aliases/aliases.py:143`
- `cli` calls [click.decorators](/modules/click.decorators.md) `command` `examples/aliases/aliases.py:89`
- `cli` calls [click.decorators](/modules/click.decorators.md) `option` `examples/aliases/aliases.py:90`
- `clone` calls [click.utils](/modules/click.utils.md) `echo` `examples/aliases/aliases.py:116`
- `commit` calls [click.utils](/modules/click.utils.md) `echo` `examples/aliases/aliases.py:122`
- `pull` calls [click.utils](/modules/click.utils.md) `echo` `examples/aliases/aliases.py:110`
- `push` calls [click.utils](/modules/click.utils.md) `echo` `examples/aliases/aliases.py:104`
- `status` calls [click.utils](/modules/click.utils.md) `echo` `examples/aliases/aliases.py:129`
- `AliasedGroup.get_command` calls [click.core](/modules/click.core.md) `Group.get_command` `examples/aliases/aliases.py:44`
- `AliasedGroup.get_command` calls [click.core](/modules/click.core.md) `Group.list_commands` `examples/aliases/aliases.py:62`
- `AliasedGroup.resolve_command` calls [click.core](/modules/click.core.md) `Group.resolve_command` `examples/aliases/aliases.py:72`
