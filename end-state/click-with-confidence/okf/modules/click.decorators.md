---
type: Code Module
title: "click.decorators"
description: "click.decorators: pass_context, pass_obj, make_pass_decorator, pass_meta_key"
resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/decorators.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/decorators.py"
    sha256: "16069357615691fcdfc9c794bb515f6009eb35aad6f7a76c017bdce06dae8d55"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

> `[high]` is stated directly in the source; `[medium]` is a deterministic inference.

# click.decorators

Source: `src/click/decorators.py`

## Functions and methods
- `pass_context(f: t.Callable[te.Concatenate[Context, P], R]) -> t.Callable[P, R]` `src/click/decorators.py:28` `[high]`
- `pass_obj(f: t.Callable[te.Concatenate[T, P], R]) -> t.Callable[P, R]` `src/click/decorators.py:39` `[high]`
- `make_pass_decorator(object_type: type[T], ensure: bool) -> t.Callable[[t.Callable[te.Concatenate[T, P], R]], t.Callable[P, R]]` `src/click/decorators.py:51` `[high]`
- `pass_meta_key(key: str, doc_description: str | None) -> t.Callable[[t.Callable[te.Concatenate[T, P], R]], t.Callable[P, R]]` `src/click/decorators.py:100` `[high]`
- `command(name: str | _AnyCallable | None) -> Command | t.Callable[[_AnyCallable], Command | CmdType]` `src/click/decorators.py:168` `[high]`
- `group(name: str | _AnyCallable | None) -> Group | t.Callable[[_AnyCallable], Group | GrpType]` `src/click/decorators.py:293` `[high]`
- `_param_memo(f: t.Callable[..., t.Any], param: Parameter) -> None` `src/click/decorators.py:314` `[high]`
- `argument() -> t.Callable[[FC], FC]` `src/click/decorators.py:324` `[high]`
- `option() -> t.Callable[[FC], FC]` `src/click/decorators.py:352` `[high]`
- `confirmation_option() -> t.Callable[[FC], FC]` `src/click/decorators.py:380` `[high]`
- `password_option() -> t.Callable[[FC], FC]` `src/click/decorators.py:404` `[high]`
- `version_option(version: str | None, package_name: str | None, prog_name: str | None, message: str | None) -> t.Callable[[FC], FC]` `src/click/decorators.py:421` `[high]`
- `custom_version_option(callback: t.Callable[[Context], str]) -> t.Callable[[FC], FC]` `src/click/decorators.py:561` `[high]`
- `help_option() -> t.Callable[[FC], FC]` `src/click/decorators.py:603` `[high]`

## Depends on
- [click.core](/modules/click.core.md) `src/click/decorators.py:8` `[high]`
- [click.globals](/modules/click.globals.md) `src/click/decorators.py:14` `[high]`
- [click.utils](/modules/click.utils.md) `src/click/decorators.py:15` `[high]`

## Calls
- `custom_version_option` calls [click.utils](/modules/click.utils.md) `echo` `src/click/decorators.py:589` `[medium]`
- `help_option` calls [click.utils](/modules/click.utils.md) `echo` `src/click/decorators.py:615` `[medium]`
- `make_pass_decorator` calls [click.core](/modules/click.core.md) `Context.ensure_object` `src/click/decorators.py:82` `[medium]`
- `make_pass_decorator` calls [click.core](/modules/click.core.md) `Context.find_object` `src/click/decorators.py:84` `[medium]`
- `make_pass_decorator` calls [click.core](/modules/click.core.md) `Context.invoke` `src/click/decorators.py:93` `[medium]`
- `make_pass_decorator` calls [click.globals](/modules/click.globals.md) `get_current_context` `src/click/decorators.py:78` `[medium]`
- `pass_context` calls [click.globals](/modules/click.globals.md) `get_current_context` `src/click/decorators.py:34` `[medium]`
- `pass_meta_key` calls [click.core](/modules/click.core.md) `Context.invoke` `src/click/decorators.py:119` `[medium]`
- `pass_meta_key` calls [click.globals](/modules/click.globals.md) `get_current_context` `src/click/decorators.py:117` `[medium]`
- `pass_obj` calls [click.globals](/modules/click.globals.md) `get_current_context` `src/click/decorators.py:46` `[medium]`
- `version_option` calls [click.utils](/modules/click.utils.md) `echo` `src/click/decorators.py:544` `[medium]`
