---
type: Code Module
title: "click.utils"
description: "click.utils: _LazyFile, _KeepOpenFile, _PacifyFlushWrapper"
resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/utils.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/utils.py"
    sha256: "4720e22c292047ff1a747546b1ba80e96d1d8e8158e2e21ff01cdddb6498db17"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

> `[high]` is stated directly in the source; `[medium]` is a deterministic inference.

# click.utils

Source: `src/click/utils.py`

## Types
- `_LazyFile` (class) `src/click/utils.py:103` `[high]`
- `_KeepOpenFile` (class) `src/click/utils.py:199` `[high]`
- `_PacifyFlushWrapper` (class) `src/click/utils.py:521` `[high]`

## Functions and methods
- `_posixify(name: str) -> str` `src/click/utils.py:32` `[high]`
- `_safecall(func: t.Callable[P, R]) -> t.Callable[P, R | None]` `src/click/utils.py:36` `[high]`
- `make_str(value: t.Any) -> str` `src/click/utils.py:52` `[high]`
- `_make_default_short_help(help: str, max_length: int) -> str` `src/click/utils.py:62` `[high]`
- `_LazyFile.__init__(filename: str | os.PathLike[str], mode: str, encoding: str | None, errors: str | None, atomic: bool) -> None` `src/click/utils.py:120` `[high]`
- `_LazyFile.__getattr__(name: str) -> t.Any` `src/click/utils.py:145` `[high]`
- `_LazyFile.__repr__() -> str` `src/click/utils.py:148` `[high]`
- `_LazyFile.open() -> t.IO[t.Any]` `src/click/utils.py:153` `[high]`
- `_LazyFile.close() -> None` `src/click/utils.py:171` `[high]`
- `_LazyFile.close_intelligently() -> None` `src/click/utils.py:176` `[high]`
- `_LazyFile.__enter__() -> _LazyFile` `src/click/utils.py:183` `[high]`
- `_LazyFile.__exit__(exc_type: type[BaseException] | None, exc_value: BaseException | None, tb: TracebackType | None) -> None` `src/click/utils.py:186` `[high]`
- `_LazyFile.__iter__() -> cabc.Iterator[t.AnyStr]` `src/click/utils.py:194` `[high]`
- `_KeepOpenFile.__init__(file: t.IO[t.Any]) -> None` `src/click/utils.py:216` `[high]`
- `_KeepOpenFile.__getattr__(name: str) -> t.Any` `src/click/utils.py:219` `[high]`
- `_KeepOpenFile.__enter__() -> _KeepOpenFile` `src/click/utils.py:222` `[high]`
- `_KeepOpenFile.__exit__(exc_type: type[BaseException] | None, exc_value: BaseException | None, tb: TracebackType | None) -> None` `src/click/utils.py:225` `[high]`
- `_KeepOpenFile.__repr__() -> str` `src/click/utils.py:233` `[high]`
- `_KeepOpenFile.__iter__() -> cabc.Iterator[t.AnyStr]` `src/click/utils.py:236` `[high]`
- `echo(message: object, file: t.IO[t.Any] | None, nl: bool, err: bool, color: bool | None) -> None` `src/click/utils.py:240` `[high]`
- `_get_binary_stream(name: t.Literal['stdin', 'stdout', 'stderr']) -> t.BinaryIO` `src/click/utils.py:337` `[high]`
- `_get_text_stream(name: t.Literal['stdin', 'stdout', 'stderr'], encoding: str | None, errors: str | None) -> t.TextIO` `src/click/utils.py:354` `[high]`
- `open_file(filename: str | os.PathLike[str], mode: str, encoding: str | None, errors: str | None, lazy: bool, atomic: bool) -> t.IO[t.Any]` `src/click/utils.py:381` `[high]`
- `format_filename(filename: str | bytes | os.PathLike[str] | os.PathLike[bytes], shorten: bool) -> str` `src/click/utils.py:430` `[high]`
- `get_app_dir(app_name: str, roaming: bool, force_posix: bool) -> str` `src/click/utils.py:472` `[high]`
- `_PacifyFlushWrapper.__init__(wrapped: t.IO[t.Any]) -> None` `src/click/utils.py:534` `[high]`
- `_PacifyFlushWrapper.flush() -> None` `src/click/utils.py:537` `[high]`
- `_PacifyFlushWrapper.__getattr__(attr: str) -> t.Any` `src/click/utils.py:546` `[high]`
- `_detect_program_name(path: str | None, _main: ModuleType | None) -> str` `src/click/utils.py:550` `[high]`
- `_expand_args(args: cabc.Iterable[str], user: bool, env: bool, glob_recursive: bool) -> list[str]` `src/click/utils.py:605` `[high]`
- `__getattr__(name: str) -> object` `src/click/utils.py:657` `[high]`

## Depends on
- [click._compat](/modules/click._compat.md) `src/click/utils.py:13` `[high]`
- [click.globals](/modules/click.globals.md) `src/click/utils.py:22` `[high]`

## Calls
- `echo` calls [click._compat](/modules/click._compat.md) `_find_binary_writer` `src/click/utils.py:321` `[medium]`
- `echo` calls [click._compat](/modules/click._compat.md) `should_strip_ansi` `src/click/utils.py:330` `[medium]`
- `echo` calls [click._compat](/modules/click._compat.md) `strip_ansi` `src/click/utils.py:331` `[medium]`
- `echo` calls [click.globals](/modules/click.globals.md) `resolve_color_default` `src/click/utils.py:330` `[medium]`
- `open_file` calls [click._compat](/modules/click._compat.md) `open_stream` `src/click/utils.py:422` `[medium]`
- `_LazyFile.__init__` calls [click._compat](/modules/click._compat.md) `open_stream` `src/click/utils.py:135` `[medium]`
- `_LazyFile.open` calls [click._compat](/modules/click._compat.md) `open_stream` `src/click/utils.py:161` `[medium]`

## Tests
- `test_utils`
