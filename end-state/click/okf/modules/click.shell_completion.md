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

# click.shell_completion

Source: `src/click/shell_completion.py`

## Types
- `CompletionItem` (class) extends `typing.Generic[_ValueT_co]` `src/click/shell_completion.py:67`
- `_SourceVarsDict` (class) extends `typing.TypedDict` `src/click/shell_completion.py:272`
- `ShellComplete` (class) `src/click/shell_completion.py:278`
- `BashComplete` (class) extends `click.shell_completion.ShellComplete` `src/click/shell_completion.py:389`
- `ZshComplete` (class) extends `click.shell_completion.ShellComplete` `src/click/shell_completion.py:448`
- `FishComplete` (class) extends `click.shell_completion.ShellComplete` `src/click/shell_completion.py:484`
- `PowerShellComplete` (class) extends `click.shell_completion.ShellComplete` `src/click/shell_completion.py:521`

## Functions and methods
- `shell_complete(cli: Command, ctx_args: cabc.MutableMapping[str, t.Any], prog_name: str, complete_var: str, instruction: str) -> t.Literal[0, 1]` `src/click/shell_completion.py:19`
- `CompletionItem.__init__(value: _ValueT_co, type: str, help: str | None) -> None` `src/click/shell_completion.py:88`
- `CompletionItem.__getattr__(name: str) -> t.Any` `src/click/shell_completion.py:100`
- `ShellComplete.__init__(cli: Command, ctx_args: cabc.MutableMapping[str, t.Any], prog_name: str, complete_var: str) -> None` `src/click/shell_completion.py:307`
- `ShellComplete.func_name() -> str` `src/click/shell_completion.py:320`
- `ShellComplete.source_vars() -> _SourceVarsDict` `src/click/shell_completion.py:327`
- `ShellComplete.source() -> str` `src/click/shell_completion.py:339`
- `ShellComplete.get_completion_args() -> tuple[list[str], str]` `src/click/shell_completion.py:347`
- `ShellComplete.get_completions(args: list[str], incomplete: str) -> list[CompletionItem[str]]` `src/click/shell_completion.py:354`
- `ShellComplete.format_completion(item: CompletionItem[str]) -> str` `src/click/shell_completion.py:368`
- `ShellComplete.complete() -> str` `src/click/shell_completion.py:376`
- `BashComplete._check_version() -> None` `src/click/shell_completion.py:396`
- `BashComplete.source() -> str` `src/click/shell_completion.py:428`
- `BashComplete.get_completion_args() -> tuple[list[str], str]` `src/click/shell_completion.py:432`
- `BashComplete.format_completion(item: CompletionItem[t.Any]) -> str` `src/click/shell_completion.py:444`
- `ZshComplete.get_completion_args() -> tuple[list[str], str]` `src/click/shell_completion.py:454`
- `ZshComplete.format_completion(item: CompletionItem[str]) -> str` `src/click/shell_completion.py:466`
- `FishComplete.get_completion_args() -> tuple[list[str], str]` `src/click/shell_completion.py:490`
- `FishComplete.format_completion(item: CompletionItem[str]) -> str` `src/click/shell_completion.py:504`
- `PowerShellComplete.get_completion_args() -> tuple[list[str], str]` `src/click/shell_completion.py:530`
- `PowerShellComplete.format_completion(item: CompletionItem[str]) -> str` `src/click/shell_completion.py:542`
- `add_completion_class(name: str | None) -> type[_ShellCompleteT]` `src/click/shell_completion.py:565`
- `get_completion_class(shell: str) -> type[ShellComplete] | None` `src/click/shell_completion.py:593`
- `split_arg_string(string: str) -> list[str]` `src/click/shell_completion.py:603`
- `_is_incomplete_argument(ctx: Context, param: Parameter) -> bool` `src/click/shell_completion.py:639`
- `_start_of_option(ctx: Context, value: str) -> bool` `src/click/shell_completion.py:662`
- `_is_incomplete_option(ctx: Context, args: list[str], param: Parameter) -> bool` `src/click/shell_completion.py:671`
- `_resolve_context(cli: Command, ctx_args: cabc.MutableMapping[str, t.Any], prog_name: str, args: list[str]) -> Context` `src/click/shell_completion.py:696`
- `_resolve_incomplete(ctx: Context, args: list[str], incomplete: str) -> tuple[Command | Parameter, str]` `src/click/shell_completion.py:757`

## Depends on
- [click.core](/modules/click.core.md) `src/click/shell_completion.py:9`
- [click.utils](/modules/click.utils.md) `src/click/shell_completion.py:16`

## Calls
- `_is_incomplete_argument` calls [click.core](/modules/click.core.md) `Context.get_parameter_source` `src/click/shell_completion.py:653`
- `_resolve_context` calls [click.core](/modules/click.core.md) `Command.make_context` `src/click/shell_completion.py:711`
- `_resolve_incomplete` calls [click.core](/modules/click.core.md) `Command.get_params` `src/click/shell_completion.py:785`
- `shell_complete` calls [click.utils](/modules/click.utils.md) `echo` `src/click/shell_completion.py:48`
- `BashComplete._check_version` calls [click.utils](/modules/click.utils.md) `echo` `src/click/shell_completion.py:415`

## Tests
- `test_shell_completion`
