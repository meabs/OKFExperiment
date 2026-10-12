---
type: Code Module
title: "repo"
description: "repo: Repo"
resource: "repo:examples/repo/repo.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "repo:examples/repo/repo.py"
    id: "cef5766bc593"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

# repo

Source: `examples/repo/repo.py`

## Types
- `Repo` (class) `examples/repo/repo.py:8`

## Functions and methods
- `Repo.__init__(home)` `examples/repo/repo.py:9`
- `Repo.set_config(key, value)` `examples/repo/repo.py:14`
- `Repo.__repr__()` `examples/repo/repo.py:19`
- `cli(ctx, repo_home, config, verbose)` `examples/repo/repo.py:44`
- `clone(repo, src, dest, shallow, rev)` `examples/repo/repo.py:72`
- `delete(repo)` `examples/repo/repo.py:91`
- `setuser(repo, username, email, password)` `examples/repo/repo.py:105`
- `commit(repo, files, message)` `examples/repo/repo.py:126`
- `copy(repo, src, dst, force)` `examples/repo/repo.py:161`

## Depends on
- [click](/modules/click.md) `examples/repo/repo.py:5`

## Calls
- `cli` calls [click.decorators](/modules/click.decorators.md) `group` `examples/repo/repo.py:26`
- `cli` calls [click.decorators](/modules/click.decorators.md) `option` `examples/repo/repo.py:27`
- `cli` calls [click.decorators](/modules/click.decorators.md) `version_option` `examples/repo/repo.py:42`
- `clone` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/repo/repo.py:61`
- `clone` calls [click.decorators](/modules/click.decorators.md) `option` `examples/repo/repo.py:63`
- `clone` calls [click.utils](/modules/click.utils.md) `echo` `examples/repo/repo.py:81`
- `commit` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/repo/repo.py:124`
- `commit` calls [click.decorators](/modules/click.decorators.md) `option` `examples/repo/repo.py:117`
- `commit` calls [click.termui](/modules/click.termui.md) `edit` `examples/repo/repo.py:140`
- `commit` calls [click.utils](/modules/click.utils.md) `echo` `examples/repo/repo.py:142`
- `copy` calls [click.decorators](/modules/click.decorators.md) `argument` `examples/repo/repo.py:158`
- `copy` calls [click.decorators](/modules/click.decorators.md) `option` `examples/repo/repo.py:155`
- `copy` calls [click.utils](/modules/click.utils.md) `echo` `examples/repo/repo.py:166`
- `delete` calls [click.decorators](/modules/click.decorators.md) `confirmation_option` `examples/repo/repo.py:89`
- `delete` calls [click.utils](/modules/click.utils.md) `echo` `examples/repo/repo.py:96`
- `setuser` calls [click.decorators](/modules/click.decorators.md) `option` `examples/repo/repo.py:101`
- `setuser` calls [click.decorators](/modules/click.decorators.md) `password_option` `examples/repo/repo.py:103`
- `setuser` calls [click.utils](/modules/click.utils.md) `echo` `examples/repo/repo.py:113`
- `Repo.set_config` calls [click.utils](/modules/click.utils.md) `echo` `examples/repo/repo.py:17`
