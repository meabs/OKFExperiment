---
type: Code Module
title: "click.formatting"
description: "click.formatting: HelpFormatter"
resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/formatting.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/formatting.py"
    sha256: "f125b628692f8dfcfd43535b7a88cc1ee64137471f9d0243b389aa0cfea85e6b"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

> `[high]` is stated directly in the source; `[medium]` is a deterministic inference.

# click.formatting

Source: `src/click/formatting.py`

## Types
- `HelpFormatter` (class) `src/click/formatting.py:110` `[high]`

## Functions and methods
- `measure_table(rows: cabc.Iterable[tuple[str, str]]) -> tuple[int, ...]` `src/click/formatting.py:14` `[high]`
- `iter_rows(rows: cabc.Iterable[tuple[str, str]], col_count: int) -> cabc.Iterator[tuple[str, ...]]` `src/click/formatting.py:24` `[high]`
- `wrap_text(text: str, width: int, initial_indent: str, subsequent_indent: str, preserve_paragraphs: bool) -> str` `src/click/formatting.py:31` `[high]`
- `HelpFormatter.__init__(indent_increment: int, width: int | None, max_width: int | None) -> None` `src/click/formatting.py:127` `[high]`
- `HelpFormatter.write(string: str) -> None` `src/click/formatting.py:146` `[high]`
- `HelpFormatter.indent() -> None` `src/click/formatting.py:150` `[high]`
- `HelpFormatter.dedent() -> None` `src/click/formatting.py:154` `[high]`
- `HelpFormatter.write_usage(prog: str, args: str, prefix: str | None) -> None` `src/click/formatting.py:158` `[high]`
- `HelpFormatter.write_heading(heading: str) -> None` `src/click/formatting.py:204` `[high]`
- `HelpFormatter.write_paragraph() -> None` `src/click/formatting.py:208` `[high]`
- `HelpFormatter.write_text(text: str) -> None` `src/click/formatting.py:213` `[high]`
- `HelpFormatter.write_dl(rows: cabc.Iterable[tuple[str, str]], col_max: int, col_spacing: int) -> None` `src/click/formatting.py:229` `[high]`
- `HelpFormatter.section(name: str) -> cabc.Generator[None]` `src/click/formatting.py:274` `[high]`
- `HelpFormatter.indentation() -> cabc.Generator[None]` `src/click/formatting.py:289` `[high]`
- `HelpFormatter.getvalue() -> str` `src/click/formatting.py:297` `[high]`
- `join_options(options: cabc.Iterable[str]) -> tuple[str, bool]` `src/click/formatting.py:302` `[high]`

## Depends on
- [click._compat](/modules/click._compat.md) `src/click/formatting.py:7` `[high]`
- [click.parser](/modules/click.parser.md) `src/click/formatting.py:8` `[high]`

## Calls
- `join_options` calls [click.parser](/modules/click.parser.md) `_split_opt` `src/click/formatting.py:312` `[medium]`
- `measure_table` calls [click._compat](/modules/click._compat.md) `term_len` `src/click/formatting.py:19` `[medium]`
- `wrap_text` calls [click._compat](/modules/click._compat.md) `term_len` `src/click/formatting.py:93` `[medium]`
- `HelpFormatter.write_dl` calls [click._compat](/modules/click._compat.md) `term_len` `src/click/formatting.py:255` `[medium]`
- `HelpFormatter.write_usage` calls [click._compat](/modules/click._compat.md) `term_len` `src/click/formatting.py:180` `[medium]`

## Tests
- `test_formatting`
