---
type: Code Module
title: "click.formatting"
description: "click.formatting: HelpFormatter"
resource: "repo:src/click/formatting.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "repo:src/click/formatting.py"
    id: "f125b628692f"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

# click.formatting

Source: `src/click/formatting.py`

## Types
- `HelpFormatter` (class) `src/click/formatting.py:110`

## Functions and methods
- `measure_table(rows: cabc.Iterable[tuple[str, str]]) -> tuple[int, ...]` `src/click/formatting.py:14`
- `iter_rows(rows: cabc.Iterable[tuple[str, str]], col_count: int) -> cabc.Iterator[tuple[str, ...]]` `src/click/formatting.py:24`
- `wrap_text(text: str, width: int, initial_indent: str, subsequent_indent: str, preserve_paragraphs: bool) -> str` `src/click/formatting.py:31`
- `HelpFormatter.__init__(indent_increment: int, width: int | None, max_width: int | None) -> None` `src/click/formatting.py:127`
- `HelpFormatter.write(string: str) -> None` `src/click/formatting.py:146`
- `HelpFormatter.indent() -> None` `src/click/formatting.py:150`
- `HelpFormatter.dedent() -> None` `src/click/formatting.py:154`
- `HelpFormatter.write_usage(prog: str, args: str, prefix: str | None) -> None` `src/click/formatting.py:158`
- `HelpFormatter.write_heading(heading: str) -> None` `src/click/formatting.py:204`
- `HelpFormatter.write_paragraph() -> None` `src/click/formatting.py:208`
- `HelpFormatter.write_text(text: str) -> None` `src/click/formatting.py:213`
- `HelpFormatter.write_dl(rows: cabc.Iterable[tuple[str, str]], col_max: int, col_spacing: int) -> None` `src/click/formatting.py:229`
- `HelpFormatter.section(name: str) -> cabc.Generator[None]` `src/click/formatting.py:274`
- `HelpFormatter.indentation() -> cabc.Generator[None]` `src/click/formatting.py:289`
- `HelpFormatter.getvalue() -> str` `src/click/formatting.py:297`
- `join_options(options: cabc.Iterable[str]) -> tuple[str, bool]` `src/click/formatting.py:302`

## Depends on
- [click._compat](/modules/click._compat.md) `src/click/formatting.py:7`
- [click.parser](/modules/click.parser.md) `src/click/formatting.py:8`

## Calls
- `join_options` calls [click.parser](/modules/click.parser.md) `_split_opt` `src/click/formatting.py:312`
- `measure_table` calls [click._compat](/modules/click._compat.md) `term_len` `src/click/formatting.py:19`
- `wrap_text` calls [click._compat](/modules/click._compat.md) `term_len` `src/click/formatting.py:93`
- `HelpFormatter.write_dl` calls [click._compat](/modules/click._compat.md) `term_len` `src/click/formatting.py:255`
- `HelpFormatter.write_usage` calls [click._compat](/modules/click._compat.md) `term_len` `src/click/formatting.py:180`

## Tests
- `test_formatting`
