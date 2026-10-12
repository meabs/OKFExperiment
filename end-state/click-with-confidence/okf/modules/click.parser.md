---
type: Code Module
title: "click.parser"
description: "click.parser: _Option, _Argument, _ParsingState, _OptionParser"
resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/parser.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/parser.py"
    sha256: "a09f9f53fde6bf1ba022e36d1da0804d9e7a9601261d18208c9892a84818ae30"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

> `[high]` is stated directly in the source; `[medium]` is a deterministic inference.

# click.parser

Source: `src/click/parser.py`

## Types
- `_Option` (class) `src/click/parser.py:127` `[high]`
- `_Argument` (class) `src/click/parser.py:185` `[high]`
- `_ParsingState` (class) `src/click/parser.py:216` `[high]`
- `_OptionParser` (class) `src/click/parser.py:224` `[high]`

## Functions and methods
- `_unpack_args(args: cabc.Sequence[str], nargs_spec: cabc.Sequence[int]) -> tuple[cabc.Sequence[str | cabc.Sequence[str | T_UNSET] | T_UNSET], list[str]]` `src/click/parser.py:51` `[high]`
- `_split_opt(opt: str) -> tuple[str, str]` `src/click/parser.py:111` `[high]`
- `_normalize_opt(opt: str, ctx: Context | None) -> str` `src/click/parser.py:120` `[high]`
- `_Option.__init__(obj: CoreOption, opts: cabc.Sequence[str], dest: str | None, action: str | None, nargs: int, const: t.Any | None)` `src/click/parser.py:128` `[high]`
- `_Option.takes_value() -> bool` `src/click/parser.py:166` `[high]`
- `_Option.process(value: t.Any, state: _ParsingState) -> None` `src/click/parser.py:169` `[high]`
- `_Argument.__init__(obj: CoreArgument, dest: str | None, nargs: int)` `src/click/parser.py:186` `[high]`
- `_Argument.process(value: str | cabc.Sequence[str | T_UNSET] | T_UNSET, state: _ParsingState) -> None` `src/click/parser.py:191` `[high]`
- `_ParsingState.__init__(rargs: list[str]) -> None` `src/click/parser.py:217` `[high]`
- `_OptionParser.__init__(ctx: Context | None) -> None` `src/click/parser.py:241` `[high]`
- `_OptionParser.add_option(obj: CoreOption, opts: cabc.Sequence[str], dest: str | None, action: str | None, nargs: int, const: t.Any | None) -> None` `src/click/parser.py:265` `[high]`
- `_OptionParser.add_argument(obj: CoreArgument, dest: str | None, nargs: int) -> None` `src/click/parser.py:290` `[high]`
- `_OptionParser.parse_args(args: list[str]) -> tuple[dict[str, t.Any], list[str], list[CoreParameter]]` `src/click/parser.py:298` `[high]`
- `_OptionParser._process_args_for_args(state: _ParsingState) -> None` `src/click/parser.py:316` `[high]`
- `_OptionParser._process_args_for_options(state: _ParsingState) -> None` `src/click/parser.py:327` `[high]`
- `_OptionParser._match_long_opt(opt: str, explicit_value: str | None, state: _ParsingState) -> None` `src/click/parser.py:363` `[high]`
- `_OptionParser._match_short_opt(arg: str, state: _ParsingState) -> None` `src/click/parser.py:390` `[high]`
- `_OptionParser._get_value_from_state(option_name: str, option: _Option, state: _ParsingState) -> str | cabc.Sequence[str] | T_UNSET | T_FLAG_NEEDS_VALUE` `src/click/parser.py:430` `[high]`
- `_OptionParser._process_opts(arg: str, state: _ParsingState) -> None` `src/click/parser.py:470` `[high]`
- `__getattr__(name: str) -> object` `src/click/parser.py:503` `[high]`

## Depends on
- [click._utils](/modules/click._utils.md) `src/click/parser.py:33` `[high]`
- [click.core](/modules/click.core.md) `src/click/parser.py:43` `[high]`
- [click.exceptions](/modules/click.exceptions.md) `src/click/parser.py:35` `[high]`

## Tests
- `test_parser`
