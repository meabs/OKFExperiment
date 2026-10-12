---
type: Code Module
title: "repo"
description: "repo: Repo"
resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/examples/repo/repo.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/examples/repo/repo.py"
    sha256: "cef5766bc59330ff9342f7c6a7eabfe89716ab46a7f719d84a7b97d3b12f5f09"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

> `[high]` is stated directly in the source; `[medium]` is a deterministic inference.

# repo

Source: `examples/repo/repo.py`

## Types
- `Repo` (class) `examples/repo/repo.py:8` `[high]`

## Functions and methods
- `Repo.__init__(home)` `examples/repo/repo.py:9` `[high]`
- `Repo.set_config(key, value)` `examples/repo/repo.py:14` `[high]`
- `Repo.__repr__()` `examples/repo/repo.py:19` `[high]`
- `cli(ctx, repo_home, config, verbose)` `examples/repo/repo.py:44` `[high]`
- `clone(repo, src, dest, shallow, rev)` `examples/repo/repo.py:72` `[high]`
- `delete(repo)` `examples/repo/repo.py:91` `[high]`
- `setuser(repo, username, email, password)` `examples/repo/repo.py:105` `[high]`
- `commit(repo, files, message)` `examples/repo/repo.py:126` `[high]`
- `copy(repo, src, dst, force)` `examples/repo/repo.py:161` `[high]`

## Depends on
- [click](/modules/click.md) `examples/repo/repo.py:5` `[high]`

## Calls
- `cli` calls [click.decorators](/modules/click.decorators.md) `group` `examples/repo/repo.py:26` `[medium]`
- `cli` calls [click.decorators](/modules/click.decorators.md) `option` `examples/repo/repo.py:27` `[medium]`
- `cli` calls [click.decorators](/modules/click.decorators.md) `version_option` `examples/repo/repo.py:42` `[medium]`
- `clone` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/repo/repo.py:61` `[medium]`
- `clone` calls [click.decorators](/modules/click.decorators.md) `option` `examples/repo/repo.py:63` `[medium]`
- `clone` calls [click.utils](/modules/click.utils.md) `echo` `examples/repo/repo.py:81` `[medium]`
- `commit` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/repo/repo.py:124` `[medium]`
- `commit` calls [click.decorators](/modules/click.decorators.md) `option` `examples/repo/repo.py:117` `[medium]`
- `commit` calls [click.termui](/modules/click.termui.md) `edit` `examples/repo/repo.py:140` `[medium]`
- `commit` calls [click.utils](/modules/click.utils.md) `echo` `examples/repo/repo.py:142` `[medium]`
- `copy` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/repo/repo.py:158` `[medium]`
- `copy` calls [click.decorators](/modules/click.decorators.md) `option` `examples/repo/repo.py:155` `[medium]`
- `copy` calls [click.utils](/modules/click.utils.md) `echo` `examples/repo/repo.py:166` `[medium]`
- `delete` calls [click.decorators](/modules/click.decorators.md) `confirmation_option` `examples/repo/repo.py:89` `[medium]`
- `delete` calls [click.utils](/modules/click.utils.md) `echo` `examples/repo/repo.py:96` `[medium]`
- `setuser` calls [click.decorators](/modules/click.decorators.md) `option` `examples/repo/repo.py:101` `[medium]`
- `setuser` calls [click.decorators](/modules/click.decorators.md) `password_option` `examples/repo/repo.py:103` `[medium]`
- `setuser` calls [click.utils](/modules/click.utils.md) `echo` `examples/repo/repo.py:113` `[medium]`
- `Repo.set_config` calls [click.utils](/modules/click.utils.md) `echo` `examples/repo/repo.py:17` `[medium]`
