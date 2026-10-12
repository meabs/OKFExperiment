---
type: Code Module
title: "click.shell_completion"
description: "click.shell_completion: CompletionItem, _SourceVarsDict, ShellComplete, BashComplete"
resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/shell_completion.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/shell_completion.py"
    sha256: "18522f75ddffe655e943978d1953255c447842867d3fd67fbdc1543d3df7da09"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

> `[high]` is stated directly in the source; `[medium]` is a deterministic inference.

# click.shell_completion

Source: `src/click/shell_completion.py`

## Types
- `CompletionItem` (class) extends `typing.Generic[_ValueT_co]` `src/click/shell_completion.py:67` `[high]`
- `_SourceVarsDict` (class) extends `typing.TypedDict` `src/click/shell_completion.py:272` `[high]`
- `ShellComplete` (class) `src/click/shell_completion.py:278` `[high]`
- `BashComplete` (class) extends `click.shell_completion.ShellComplete` `src/click/shell_completion.py:389` `[high]`
- `ZshComplete` (class) extends `click.shell_completion.ShellComplete` `src/click/shell_completion.py:448` `[high]`
- `FishComplete` (class) extends `click.shell_completion.ShellComplete` `src/click/shell_completion.py:484` `[high]`
- `PowerShellComplete` (class) extends `click.shell_completion.ShellComplete` `src/click/shell_completion.py:521` `[high]`

## Functions and methods
- `shell_complete(cli: Command, ctx_args: cabc.MutableMapping[str, t.Any], prog_name: str, complete_var: str, instruction: str) -> t.Literal[0, 1]` `src/click/shell_completion.py:19` `[high]`
- `CompletionItem.__init__(value: _ValueT_co, type: str, help: str | None) -> None` `src/click/shell_completion.py:88` `[high]`
- `CompletionItem.__getattr__(name: str) -> t.Any` `src/click/shell_completion.py:100` `[high]`
- `ShellComplete.__init__(cli: Command, ctx_args: cabc.MutableMapping[str, t.Any], prog_name: str, complete_var: str) -> None` `src/click/shell_completion.py:307` `[high]`
- `ShellComplete.func_name() -> str` `src/click/shell_completion.py:320` `[high]`
- `ShellComplete.source_vars() -> _SourceVarsDict` `src/click/shell_completion.py:327` `[high]`
- `ShellComplete.source() -> str` `src/click/shell_completion.py:339` `[high]`
- `ShellComplete.get_completion_args() -> tuple[list[str], str]` `src/click/shell_completion.py:347` `[high]`
- `ShellComplete.get_completions(args: list[str], incomplete: str) -> list[CompletionItem[str]]` `src/click/shell_completion.py:354` `[high]`
- `ShellComplete.format_completion(item: CompletionItem[str]) -> str` `src/click/shell_completion.py:368` `[high]`
- `ShellComplete.complete() -> str` `src/click/shell_completion.py:376` `[high]`
- `BashComplete._check_version() -> None` `src/click/shell_completion.py:396` `[high]`
- `BashComplete.source() -> str` `src/click/shell_completion.py:428` `[high]`
- `BashComplete.get_completion_args() -> tuple[list[str], str]` `src/click/shell_completion.py:432` `[high]`
- `BashComplete.format_completion(item: CompletionItem[t.Any]) -> str` `src/click/shell_completion.py:444` `[high]`
- `ZshComplete.get_completion_args() -> tuple[list[str], str]` `src/click/shell_completion.py:454` `[high]`
- `ZshComplete.format_completion(item: CompletionItem[str]) -> str` `src/click/shell_completion.py:466` `[high]`
- `FishComplete.get_completion_args() -> tuple[list[str], str]` `src/click/shell_completion.py:490` `[high]`
- `FishComplete.format_completion(item: CompletionItem[str]) -> str` `src/click/shell_completion.py:504` `[high]`
- `PowerShellComplete.get_completion_args() -> tuple[list[str], str]` `src/click/shell_completion.py:530` `[high]`
- `PowerShellComplete.format_completion(item: CompletionItem[str]) -> str` `src/click/shell_completion.py:542` `[high]`
- `add_completion_class(name: str | None) -> type[_ShellCompleteT]` `src/click/shell_completion.py:565` `[high]`
- `get_completion_class(shell: str) -> type[ShellComplete] | None` `src/click/shell_completion.py:593` `[high]`
- `split_arg_string(string: str) -> list[str]` `src/click/shell_completion.py:603` `[high]`
- `_is_incomplete_argument(ctx: Context, param: Parameter) -> bool` `src/click/shell_completion.py:639` `[high]`
- `_start_of_option(ctx: Context, value: str) -> bool` `src/click/shell_completion.py:662` `[high]`
- `_is_incomplete_option(ctx: Context, args: list[str], param: Parameter) -> bool` `src/click/shell_completion.py:671` `[high]`
- `_resolve_context(cli: Command, ctx_args: cabc.MutableMapping[str, t.Any], prog_name: str, args: list[str]) -> Context` `src/click/shell_completion.py:696` `[high]`
- `_resolve_incomplete(ctx: Context, args: list[str], incomplete: str) -> tuple[Command | Parameter, str]` `src/click/shell_completion.py:757` `[high]`

## Depends on
- [click.core](/modules/click.core.md) `src/click/shell_completion.py:9` `[high]`
- [click.utils](/modules/click.utils.md) `src/click/shell_completion.py:16` `[high]`

## Calls
- `_is_incomplete_argument` calls [click.core](/modules/click.core.md) `Context.get_parameter_source` `src/click/shell_completion.py:653` `[medium]`
- `_resolve_context` calls [click.core](/modules/click.core.md) `Command.make_context` `src/click/shell_completion.py:711` `[medium]`
- `_resolve_incomplete` calls [click.core](/modules/click.core.md) `Command.get_params` `src/click/shell_completion.py:785` `[medium]`
- `shell_complete` calls [click.utils](/modules/click.utils.md) `echo` `src/click/shell_completion.py:48` `[medium]`
- `BashComplete._check_version` calls [click.utils](/modules/click.utils.md) `echo` `src/click/shell_completion.py:415` `[medium]`

## Tests
- `test_shell_completion`
