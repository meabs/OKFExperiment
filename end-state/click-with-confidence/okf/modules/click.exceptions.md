---
type: Code Module
title: "click.exceptions"
description: "click.exceptions: ClickException, UsageError, BadParameter, MissingParameter"
resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/exceptions.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/exceptions.py"
    sha256: "1ef498df81b86ae8ff6d8451f3e4fc094f09c2aff5f8e72c454e1ecdfa337849"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

> `[high]` is stated directly in the source; `[medium]` is a deterministic inference.

# click.exceptions

Source: `src/click/exceptions.py`

## Types
- `ClickException` (class) extends `Exception` `src/click/exceptions.py:35` `[high]`
- `UsageError` (class) extends `click.exceptions.ClickException` `src/click/exceptions.py:68` `[high]`
- `BadParameter` (class) extends `click.exceptions.UsageError` `src/click/exceptions.py:114` `[high]`
- `MissingParameter` (class) extends `click.exceptions.BadParameter` `src/click/exceptions.py:159` `[high]`
- `NoSuchOption` (class) extends `click.exceptions.UsageError` `src/click/exceptions.py:232` `[high]`
- `NoSuchCommand` (class) extends `click.exceptions.UsageError` `src/click/exceptions.py:268` `[high]`
- `BadOptionUsage` (class) extends `click.exceptions.UsageError` `src/click/exceptions.py:304` `[high]`
- `BadArgumentUsage` (class) extends `click.exceptions.UsageError` `src/click/exceptions.py:323` `[high]`
- `NoArgsIsHelpError` (class) extends `click.exceptions.UsageError` `src/click/exceptions.py:332` `[high]`
- `FileError` (class) extends `click.exceptions.ClickException` `src/click/exceptions.py:342` `[high]`
- `Abort` (class) extends `RuntimeError` `src/click/exceptions.py:362` `[high]`
- `Exit` (class) extends `RuntimeError` `src/click/exceptions.py:366` `[high]`

## Functions and methods
- `_join_param_hints(param_hint: cabc.Sequence[str] | str | None) -> str | None` `src/click/exceptions.py:19` `[high]`
- `_format_possibilities(possibilities: list[str]) -> str` `src/click/exceptions.py:26` `[high]`
- `ClickException.__init__(message: str) -> None` `src/click/exceptions.py:44` `[high]`
- `ClickException.format_message() -> str` `src/click/exceptions.py:51` `[high]`
- `ClickException.__str__() -> str` `src/click/exceptions.py:54` `[high]`
- `ClickException.show(file: t.IO[t.Any] | None) -> None` `src/click/exceptions.py:57` `[high]`
- `UsageError.__init__(message: str, ctx: Context | None) -> None` `src/click/exceptions.py:82` `[high]`
- `UsageError.show(file: t.IO[t.Any] | None) -> None` `src/click/exceptions.py:87` `[high]`
- `BadParameter.__init__(message: str, ctx: Context | None, param: Parameter | None, param_hint: cabc.Sequence[str] | str | None) -> None` `src/click/exceptions.py:135` `[high]`
- `BadParameter.format_message() -> str` `src/click/exceptions.py:146` `[high]`
- `MissingParameter.__init__(message: str | None, ctx: Context | None, param: Parameter | None, param_hint: cabc.Sequence[str] | str | None, param_type: str | None) -> None` `src/click/exceptions.py:173` `[high]`
- `MissingParameter.format_message() -> str` `src/click/exceptions.py:184` `[high]`
- `MissingParameter.__str__() -> str` `src/click/exceptions.py:224` `[high]`
- `NoSuchOption.__init__(option_name: str, message: str | None, possibilities: cabc.Iterable[str] | None, ctx: Context | None) -> None` `src/click/exceptions.py:241` `[high]`
- `NoSuchOption.format_message() -> str` `src/click/exceptions.py:262` `[high]`
- `NoSuchCommand.__init__(command_name: str, message: str | None, possibilities: cabc.Iterable[str] | None, ctx: Context | None) -> None` `src/click/exceptions.py:277` `[high]`
- `NoSuchCommand.format_message() -> str` `src/click/exceptions.py:298` `[high]`
- `BadOptionUsage.__init__(option_name: str, message: str, ctx: Context | None) -> None` `src/click/exceptions.py:316` `[high]`
- `NoArgsIsHelpError.__init__(ctx: Context) -> None` `src/click/exceptions.py:335` `[high]`
- `NoArgsIsHelpError.show(file: t.IO[t.Any] | None) -> None` `src/click/exceptions.py:338` `[high]`
- `FileError.__init__(filename: str, hint: str | None) -> None` `src/click/exceptions.py:348` `[high]`
- `FileError.format_message() -> str` `src/click/exceptions.py:356` `[high]`
- `Exit.__init__(code: int) -> None` `src/click/exceptions.py:377` `[high]`

## Depends on
- [click._compat](/modules/click._compat.md) `src/click/exceptions.py:8` `[high]`
- [click.core](/modules/click.core.md) `src/click/exceptions.py:14` `[high]`
- [click.globals](/modules/click.globals.md) `src/click/exceptions.py:9` `[high]`
- [click.utils](/modules/click.utils.md) `src/click/exceptions.py:10` `[high]`

## Calls
- `BadParameter.format_message` calls [click.core](/modules/click.core.md) `Parameter.get_error_hint` `src/click/exceptions.py:150` `[medium]`
- `ClickException.__init__` calls [click.globals](/modules/click.globals.md) `resolve_color_default` `src/click/exceptions.py:48` `[medium]`
- `ClickException.show` calls [click._compat](/modules/click._compat.md) `get_text_stderr` `src/click/exceptions.py:59` `[medium]`
- `ClickException.show` calls [click.utils](/modules/click.utils.md) `echo` `src/click/exceptions.py:61` `[medium]`
- `FileError.__init__` calls [click.utils](/modules/click.utils.md) `format_filename` `src/click/exceptions.py:353` `[medium]`
- `MissingParameter.format_message` calls [click.core](/modules/click.core.md) `Parameter.get_error_hint` `src/click/exceptions.py:188` `[medium]`
- `MissingParameter.format_message` calls [click.types](/modules/click.types.md) `ParamType.get_missing_message` `src/click/exceptions.py:201` `[medium]`
- `NoArgsIsHelpError.__init__` calls [click.core](/modules/click.core.md) `Context.get_help` `src/click/exceptions.py:336` `[medium]`
- `NoArgsIsHelpError.show` calls [click.utils](/modules/click.utils.md) `echo` `src/click/exceptions.py:339` `[medium]`
- `UsageError.show` calls [click._compat](/modules/click._compat.md) `get_text_stderr` `src/click/exceptions.py:89` `[medium]`
- `UsageError.show` calls [click.core](/modules/click.core.md) `Command.get_help_option` `src/click/exceptions.py:94` `[medium]`
- `UsageError.show` calls [click.core](/modules/click.core.md) `Command.get_help_option_names` `src/click/exceptions.py:96` `[medium]`
- `UsageError.show` calls [click.core](/modules/click.core.md) `Context.get_usage` `src/click/exceptions.py:106` `[medium]`
- `UsageError.show` calls [click.utils](/modules/click.utils.md) `echo` `src/click/exceptions.py:106` `[medium]`

## Tests
- `test_exceptions`
