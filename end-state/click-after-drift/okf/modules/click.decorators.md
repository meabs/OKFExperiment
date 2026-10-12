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

# click.decorators

Source: `src/click/decorators.py`

## Functions and methods
- `pass_context(f: t.Callable[te.Concatenate[Context, P], R]) -> t.Callable[P, R]` `src/click/decorators.py:28`
- `pass_obj(f: t.Callable[te.Concatenate[T, P], R]) -> t.Callable[P, R]` `src/click/decorators.py:39`
- `make_pass_decorator(object_type: type[T], ensure: bool) -> t.Callable[[t.Callable[te.Concatenate[T, P], R]], t.Callable[P, R]]` `src/click/decorators.py:51`
- `pass_meta_key(key: str, doc_description: str | None) -> t.Callable[[t.Callable[te.Concatenate[T, P], R]], t.Callable[P, R]]` `src/click/decorators.py:100`
- `command(name: str | _AnyCallable | None) -> Command | t.Callable[[_AnyCallable], Command | CmdType]` `src/click/decorators.py:168`
- `group(name: str | _AnyCallable | None) -> Group | t.Callable[[_AnyCallable], Group | GrpType]` `src/click/decorators.py:293`
- `_param_memo(f: t.Callable[..., t.Any], param: Parameter) -> None` `src/click/decorators.py:314`
- `argument() -> t.Callable[[FC], FC]` `src/click/decorators.py:324`
- `option() -> t.Callable[[FC], FC]` `src/click/decorators.py:352`
- `confirmation_option() -> t.Callable[[FC], FC]` `src/click/decorators.py:380`
- `password_option() -> t.Callable[[FC], FC]` `src/click/decorators.py:404`
- `version_option(version: str | None, package_name: str | None, prog_name: str | None, message: str | None) -> t.Callable[[FC], FC]` `src/click/decorators.py:421`
- `custom_version_option(callback: t.Callable[[Context], str]) -> t.Callable[[FC], FC]` `src/click/decorators.py:561`
- `help_option() -> t.Callable[[FC], FC]` `src/click/decorators.py:603`

## Depends on
- [click.core](/modules/click.core.md) `src/click/decorators.py:8`
- [click.globals](/modules/click.globals.md) `src/click/decorators.py:14`
- [click.utils](/modules/click.utils.md) `src/click/decorators.py:15`

## Calls
- `custom_version_option` calls [click.utils](/modules/click.utils.md) `echo` `src/click/decorators.py:589`
- `help_option` calls [click.utils](/modules/click.utils.md) `echo` `src/click/decorators.py:615`
- `make_pass_decorator` calls [click.core](/modules/click.core.md) `Context.ensure_object` `src/click/decorators.py:82`
- `make_pass_decorator` calls [click.core](/modules/click.core.md) `Context.find_object` `src/click/decorators.py:84`
- `make_pass_decorator` calls [click.core](/modules/click.core.md) `Context.invoke` `src/click/decorators.py:93`
- `make_pass_decorator` calls [click.globals](/modules/click.globals.md) `get_current_context` `src/click/decorators.py:78`
- `pass_context` calls [click.globals](/modules/click.globals.md) `get_current_context` `src/click/decorators.py:34`
- `pass_meta_key` calls [click.core](/modules/click.core.md) `Context.invoke` `src/click/decorators.py:119`
- `pass_meta_key` calls [click.globals](/modules/click.globals.md) `get_current_context` `src/click/decorators.py:117`
- `pass_obj` calls [click.globals](/modules/click.globals.md) `get_current_context` `src/click/decorators.py:46`
- `version_option` calls [click.utils](/modules/click.utils.md) `echo` `src/click/decorators.py:544`
