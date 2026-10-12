---
type: Code Module
title: "click.exceptions"
description: "click.exceptions: ClickException, UsageError, BadParameter, MissingParameter"
resource: "repo:src/click/exceptions.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "repo:src/click/exceptions.py"
    id: "1ef498df81b8"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

# click.exceptions

Source: `src/click/exceptions.py`

## Types
- `ClickException` (class) extends `Exception` `src/click/exceptions.py:35`
- `UsageError` (class) extends `click.exceptions.ClickException` `src/click/exceptions.py:68`
- `BadParameter` (class) extends `click.exceptions.UsageError` `src/click/exceptions.py:114`
- `MissingParameter` (class) extends `click.exceptions.BadParameter` `src/click/exceptions.py:159`
- `NoSuchOption` (class) extends `click.exceptions.UsageError` `src/click/exceptions.py:232`
- `NoSuchCommand` (class) extends `click.exceptions.UsageError` `src/click/exceptions.py:268`
- `BadOptionUsage` (class) extends `click.exceptions.UsageError` `src/click/exceptions.py:304`
- `BadArgumentUsage` (class) extends `click.exceptions.UsageError` `src/click/exceptions.py:323`
- `NoArgsIsHelpError` (class) extends `click.exceptions.UsageError` `src/click/exceptions.py:332`
- `FileError` (class) extends `click.exceptions.ClickException` `src/click/exceptions.py:342`
- `Abort` (class) extends `RuntimeError` `src/click/exceptions.py:362`
- `Exit` (class) extends `RuntimeError` `src/click/exceptions.py:366`

## Functions and methods
- `_join_param_hints(param_hint: cabc.Sequence[str] | str | None) -> str | None` `src/click/exceptions.py:19`
- `_format_possibilities(possibilities: list[str]) -> str` `src/click/exceptions.py:26`
- `ClickException.__init__(message: str) -> None` `src/click/exceptions.py:44`
- `ClickException.format_message() -> str` `src/click/exceptions.py:51`
- `ClickException.__str__() -> str` `src/click/exceptions.py:54`
- `ClickException.show(file: t.IO[t.Any] | None) -> None` `src/click/exceptions.py:57`
- `UsageError.__init__(message: str, ctx: Context | None) -> None` `src/click/exceptions.py:82`
- `UsageError.show(file: t.IO[t.Any] | None) -> None` `src/click/exceptions.py:87`
- `BadParameter.__init__(message: str, ctx: Context | None, param: Parameter | None, param_hint: cabc.Sequence[str] | str | None) -> None` `src/click/exceptions.py:135`
- `BadParameter.format_message() -> str` `src/click/exceptions.py:146`
- `MissingParameter.__init__(message: str | None, ctx: Context | None, param: Parameter | None, param_hint: cabc.Sequence[str] | str | None, param_type: str | None) -> None` `src/click/exceptions.py:173`
- `MissingParameter.format_message() -> str` `src/click/exceptions.py:184`
- `MissingParameter.__str__() -> str` `src/click/exceptions.py:224`
- `NoSuchOption.__init__(option_name: str, message: str | None, possibilities: cabc.Iterable[str] | None, ctx: Context | None) -> None` `src/click/exceptions.py:241`
- `NoSuchOption.format_message() -> str` `src/click/exceptions.py:262`
- `NoSuchCommand.__init__(command_name: str, message: str | None, possibilities: cabc.Iterable[str] | None, ctx: Context | None) -> None` `src/click/exceptions.py:277`
- `NoSuchCommand.format_message() -> str` `src/click/exceptions.py:298`
- `BadOptionUsage.__init__(option_name: str, message: str, ctx: Context | None) -> None` `src/click/exceptions.py:316`
- `NoArgsIsHelpError.__init__(ctx: Context) -> None` `src/click/exceptions.py:335`
- `NoArgsIsHelpError.show(file: t.IO[t.Any] | None) -> None` `src/click/exceptions.py:338`
- `FileError.__init__(filename: str, hint: str | None) -> None` `src/click/exceptions.py:348`
- `FileError.format_message() -> str` `src/click/exceptions.py:356`
- `Exit.__init__(code: int) -> None` `src/click/exceptions.py:377`

## Depends on
- [click._compat](/modules/click._compat.md) `src/click/exceptions.py:8`
- [click.core](/modules/click.core.md) `src/click/exceptions.py:14`
- [click.globals](/modules/click.globals.md) `src/click/exceptions.py:9`
- [click.utils](/modules/click.utils.md) `src/click/exceptions.py:10`

## Calls
- `BadParameter.format_message` calls [click.core](/modules/click.core.md) `Parameter.get_error_hint` `src/click/exceptions.py:150`
- `ClickException.__init__` calls [click.globals](/modules/click.globals.md) `resolve_color_default` `src/click/exceptions.py:48`
- `ClickException.show` calls [click._compat](/modules/click._compat.md) `get_text_stderr` `src/click/exceptions.py:59`
- `ClickException.show` calls [click.utils](/modules/click.utils.md) `echo` `src/click/exceptions.py:61`
- `FileError.__init__` calls [click.utils](/modules/click.utils.md) `format_filename` `src/click/exceptions.py:353`
- `MissingParameter.format_message` calls [click.core](/modules/click.core.md) `Parameter.get_error_hint` `src/click/exceptions.py:188`
- `MissingParameter.format_message` calls [click.types](/modules/click.types.md) `ParamType.get_missing_message` `src/click/exceptions.py:201`
- `NoArgsIsHelpError.__init__` calls [click.core](/modules/click.core.md) `Context.get_help` `src/click/exceptions.py:336`
- `NoArgsIsHelpError.show` calls [click.utils](/modules/click.utils.md) `echo` `src/click/exceptions.py:339`
- `UsageError.show` calls [click._compat](/modules/click._compat.md) `get_text_stderr` `src/click/exceptions.py:89`
- `UsageError.show` calls [click.core](/modules/click.core.md) `Command.get_help_option` `src/click/exceptions.py:94`
- `UsageError.show` calls [click.core](/modules/click.core.md) `Command.get_help_option_names` `src/click/exceptions.py:96`
- `UsageError.show` calls [click.core](/modules/click.core.md) `Context.get_usage` `src/click/exceptions.py:106`
- `UsageError.show` calls [click.utils](/modules/click.utils.md) `echo` `src/click/exceptions.py:106`

## Tests
- `test_exceptions`
