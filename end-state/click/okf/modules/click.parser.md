---
type: Code Module
title: "click.parser"
description: "click.parser: _Option, _Argument, _ParsingState, _OptionParser"
resource: "repo:src/click/parser.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "repo:src/click/parser.py"
    id: "a09f9f53fde6"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

# click.parser

Source: `src/click/parser.py`

## Types
- `_Option` (class) `src/click/parser.py:127`
- `_Argument` (class) `src/click/parser.py:185`
- `_ParsingState` (class) `src/click/parser.py:216`
- `_OptionParser` (class) `src/click/parser.py:224`

## Functions and methods
- `_unpack_args(args: cabc.Sequence[str], nargs_spec: cabc.Sequence[int]) -> tuple[cabc.Sequence[str | cabc.Sequence[str | T_UNSET] | T_UNSET], list[str]]` `src/click/parser.py:51`
- `_split_opt(opt: str) -> tuple[str, str]` `src/click/parser.py:111`
- `_normalize_opt(opt: str, ctx: Context | None) -> str` `src/click/parser.py:120`
- `_Option.__init__(obj: CoreOption, opts: cabc.Sequence[str], dest: str | None, action: str | None, nargs: int, const: t.Any | None)` `src/click/parser.py:128`
- `_Option.takes_value() -> bool` `src/click/parser.py:166`
- `_Option.process(value: t.Any, state: _ParsingState) -> None` `src/click/parser.py:169`
- `_Argument.__init__(obj: CoreArgument, dest: str | None, nargs: int)` `src/click/parser.py:186`
- `_Argument.process(value: str | cabc.Sequence[str | T_UNSET] | T_UNSET, state: _ParsingState) -> None` `src/click/parser.py:191`
- `_ParsingState.__init__(rargs: list[str]) -> None` `src/click/parser.py:217`
- `_OptionParser.__init__(ctx: Context | None) -> None` `src/click/parser.py:241`
- `_OptionParser.add_option(obj: CoreOption, opts: cabc.Sequence[str], dest: str | None, action: str | None, nargs: int, const: t.Any | None) -> None` `src/click/parser.py:265`
- `_OptionParser.add_argument(obj: CoreArgument, dest: str | None, nargs: int) -> None` `src/click/parser.py:290`
- `_OptionParser.parse_args(args: list[str]) -> tuple[dict[str, t.Any], list[str], list[CoreParameter]]` `src/click/parser.py:298`
- `_OptionParser._process_args_for_args(state: _ParsingState) -> None` `src/click/parser.py:316`
- `_OptionParser._process_args_for_options(state: _ParsingState) -> None` `src/click/parser.py:327`
- `_OptionParser._match_long_opt(opt: str, explicit_value: str | None, state: _ParsingState) -> None` `src/click/parser.py:363`
- `_OptionParser._match_short_opt(arg: str, state: _ParsingState) -> None` `src/click/parser.py:390`
- `_OptionParser._get_value_from_state(option_name: str, option: _Option, state: _ParsingState) -> str | cabc.Sequence[str] | T_UNSET | T_FLAG_NEEDS_VALUE` `src/click/parser.py:430`
- `_OptionParser._process_opts(arg: str, state: _ParsingState) -> None` `src/click/parser.py:470`
- `__getattr__(name: str) -> object` `src/click/parser.py:503`

## Depends on
- [click._utils](/modules/click._utils.md) `src/click/parser.py:33`
- [click.core](/modules/click.core.md) `src/click/parser.py:43`
- [click.exceptions](/modules/click.exceptions.md) `src/click/parser.py:35`

## Tests
- `test_parser`
