---
type: Code Module
title: "completion"
description: "completion: cli, ls, get_env_vars, show_env"
resource: "repo:examples/completion/completion.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "repo:examples/completion/completion.py"
    id: "ceeb4f35fa92"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

# completion

Source: `examples/completion/completion.py`

## Functions and methods
- `cli()` `examples/completion/completion.py:8`
- `ls(dir)` `examples/completion/completion.py:14`
- `get_env_vars(ctx, param, incomplete)` `examples/completion/completion.py:18`
- `show_env(envvar)` `examples/completion/completion.py:26`
- `group()` `examples/completion/completion.py:32`
- `list_users(ctx, param, incomplete)` `examples/completion/completion.py:36`
- `select_user(user)` `examples/completion/completion.py:52`

## Depends on
- [click](/modules/click.md) `examples/completion/completion.py:3`
- [click.shell_completion](/modules/click.shell_completion.md) `examples/completion/completion.py:4`

## Calls
- `cli` calls [click.decorators](/modules/click.decorators.md) `group` `examples/completion/completion.py:7`
- `ls` calls [click.decorators](/modules/click.decorators.md) `option` `examples/completion/completion.py:13`
- `ls` calls [click.utils](/modules/click.utils.md) `echo` `examples/completion/completion.py:15`
- `select_user` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/completion/completion.py:51`
- `select_user` calls [click.utils](/modules/click.utils.md) `echo` `examples/completion/completion.py:53`
- `show_env` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/completion/completion.py:25`
- `show_env` calls [click.utils](/modules/click.utils.md) `echo` `examples/completion/completion.py:27`
