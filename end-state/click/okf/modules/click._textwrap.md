---
type: Code Module
title: "click._textwrap"
description: "click._textwrap: TextWrapper"
resource: "repo:src/click/_textwrap.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "repo:src/click/_textwrap.py"
    id: "ed9d0ded59a7"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

# click._textwrap

Source: `src/click/_textwrap.py`

## Types
- `TextWrapper` (class) extends `textwrap.TextWrapper` `src/click/_textwrap.py:38`

## Functions and methods
- `_truncate_visible(text: str, n: int) -> str` `src/click/_textwrap.py:11`
- `TextWrapper._handle_long_word(reversed_chunks: list[str], cur_line: list[str], cur_len: int, width: int) -> None` `src/click/_textwrap.py:48`
- `TextWrapper._wrap_chunks(chunks: list[str]) -> list[str]` `src/click/_textwrap.py:66`
- `TextWrapper.extra_indent(indent: str) -> cabc.Iterator[None]` `src/click/_textwrap.py:165`
- `TextWrapper.indent_only(text: str) -> str` `src/click/_textwrap.py:177`

## Depends on
- [click._compat](/modules/click._compat.md) `src/click/_textwrap.py:7`

## Calls
- `TextWrapper._wrap_chunks` calls [click._compat](/modules/click._compat.md) `term_len` `src/click/_textwrap.py:89`
