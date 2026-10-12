---
type: Code Module
title: "click.utils"
description: "click.utils: _LazyFile, _KeepOpenFile, _PacifyFlushWrapper"
resource: "repo:src/click/utils.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "repo:src/click/utils.py"
    id: "4720e22c2920"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

# click.utils

Source: `src/click/utils.py`

## Types
- `_LazyFile` (class) `src/click/utils.py:103`
- `_KeepOpenFile` (class) `src/click/utils.py:199`
- `_PacifyFlushWrapper` (class) `src/click/utils.py:521`

## Functions and methods
- `_posixify(name: str) -> str` `src/click/utils.py:32`
- `_safecall(func: t.Callable[P, R]) -> t.Callable[P, R | None]` `src/click/utils.py:36`
- `make_str(value: t.Any) -> str` `src/click/utils.py:52`
- `_make_default_short_help(help: str, max_length: int) -> str` `src/click/utils.py:62`
- `_LazyFile.__init__(filename: str | os.PathLike[str], mode: str, encoding: str | None, errors: str | None, atomic: bool) -> None` `src/click/utils.py:120`
- `_LazyFile.__getattr__(name: str) -> t.Any` `src/click/utils.py:145`
- `_LazyFile.__repr__() -> str` `src/click/utils.py:148`
- `_LazyFile.open() -> t.IO[t.Any]` `src/click/utils.py:153`
- `_LazyFile.close() -> None` `src/click/utils.py:171`
- `_LazyFile.close_intelligently() -> None` `src/click/utils.py:176`
- `_LazyFile.__enter__() -> _LazyFile` `src/click/utils.py:183`
- `_LazyFile.__exit__(exc_type: type[BaseException] | None, exc_value: BaseException | None, tb: TracebackType | None) -> None` `src/click/utils.py:186`
- `_LazyFile.__iter__() -> cabc.Iterator[t.AnyStr]` `src/click/utils.py:194`
- `_KeepOpenFile.__init__(file: t.IO[t.Any]) -> None` `src/click/utils.py:216`
- `_KeepOpenFile.__getattr__(name: str) -> t.Any` `src/click/utils.py:219`
- `_KeepOpenFile.__enter__() -> _KeepOpenFile` `src/click/utils.py:222`
- `_KeepOpenFile.__exit__(exc_type: type[BaseException] | None, exc_value: BaseException | None, tb: TracebackType | None) -> None` `src/click/utils.py:225`
- `_KeepOpenFile.__repr__() -> str` `src/click/utils.py:233`
- `_KeepOpenFile.__iter__() -> cabc.Iterator[t.AnyStr]` `src/click/utils.py:236`
- `echo(message: object, file: t.IO[t.Any] | None, nl: bool, err: bool, color: bool | None) -> None` `src/click/utils.py:240`
- `_get_binary_stream(name: t.Literal['stdin', 'stdout', 'stderr']) -> t.BinaryIO` `src/click/utils.py:337`
- `_get_text_stream(name: t.Literal['stdin', 'stdout', 'stderr'], encoding: str | None, errors: str | None) -> t.TextIO` `src/click/utils.py:354`
- `open_file(filename: str | os.PathLike[str], mode: str, encoding: str | None, errors: str | None, lazy: bool, atomic: bool) -> t.IO[t.Any]` `src/click/utils.py:381`
- `format_filename(filename: str | bytes | os.PathLike[str] | os.PathLike[bytes], shorten: bool) -> str` `src/click/utils.py:430`
- `get_app_dir(app_name: str, roaming: bool, force_posix: bool) -> str` `src/click/utils.py:472`
- `_PacifyFlushWrapper.__init__(wrapped: t.IO[t.Any]) -> None` `src/click/utils.py:534`
- `_PacifyFlushWrapper.flush() -> None` `src/click/utils.py:537`
- `_PacifyFlushWrapper.__getattr__(attr: str) -> t.Any` `src/click/utils.py:546`
- `_detect_program_name(path: str | None, _main: ModuleType | None) -> str` `src/click/utils.py:550`
- `_expand_args(args: cabc.Iterable[str], user: bool, env: bool, glob_recursive: bool) -> list[str]` `src/click/utils.py:605`
- `__getattr__(name: str) -> object` `src/click/utils.py:657`

## Depends on
- [click._compat](/modules/click._compat.md) `src/click/utils.py:13`
- [click.globals](/modules/click.globals.md) `src/click/utils.py:22`

## Calls
- `echo` calls [click._compat](/modules/click._compat.md) `_find_binary_writer` `src/click/utils.py:321`
- `echo` calls [click._compat](/modules/click._compat.md) `should_strip_ansi` `src/click/utils.py:330`
- `echo` calls [click._compat](/modules/click._compat.md) `strip_ansi` `src/click/utils.py:331`
- `echo` calls [click.globals](/modules/click.globals.md) `resolve_color_default` `src/click/utils.py:330`
- `open_file` calls [click._compat](/modules/click._compat.md) `open_stream` `src/click/utils.py:422`
- `_LazyFile.__init__` calls [click._compat](/modules/click._compat.md) `open_stream` `src/click/utils.py:135`
- `_LazyFile.open` calls [click._compat](/modules/click._compat.md) `open_stream` `src/click/utils.py:161`

## Tests
- `test_utils`
