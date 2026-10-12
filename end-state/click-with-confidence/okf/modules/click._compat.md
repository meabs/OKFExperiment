---
type: Code Module
title: "click._compat"
description: "click._compat: _NonClosingTextIOWrapper, _FixupStream, _AtomicFile"
resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/_compat.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/_compat.py"
    sha256: "8db1da2965cf3e5dc66c6c53833cbc613ea1cd2440b9d0eb6aa8360eb46d4913"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

> `[high]` is stated directly in the source; `[medium]` is a deterministic inference.

# click._compat

Source: `src/click/_compat.py`

## Types
- `_NonClosingTextIOWrapper` (class) extends `io.TextIOWrapper` `src/click/_compat.py:59` `[high]`
- `_FixupStream` (class) `src/click/_compat.py:85` `[high]`
- `_AtomicFile` (class) `src/click/_compat.py:455` `[high]`

## Functions and methods
- `_make_text_stream(stream: t.BinaryIO, encoding: str | None, errors: str | None, force_readable: bool, force_writable: bool) -> t.TextIO` `src/click/_compat.py:22` `[high]`
- `is_ascii_encoding(encoding: str) -> bool` `src/click/_compat.py:43` `[high]`
- `get_best_encoding(stream: t.IO[t.Any]) -> str` `src/click/_compat.py:51` `[high]`
- `_NonClosingTextIOWrapper.__init__(stream: t.BinaryIO, encoding: str | None, errors: str | None, force_readable: bool, force_writable: bool) -> None` `src/click/_compat.py:60` `[high]`
- `_NonClosingTextIOWrapper.__del__() -> None` `src/click/_compat.py:74` `[high]`
- `_NonClosingTextIOWrapper.isatty() -> bool` `src/click/_compat.py:80` `[high]`
- `_FixupStream.__init__(stream: t.BinaryIO, force_readable: bool, force_writable: bool)` `src/click/_compat.py:95` `[high]`
- `_FixupStream.__getattr__(name: str) -> t.Any` `src/click/_compat.py:105` `[high]`
- `_FixupStream.read1(size: int) -> bytes` `src/click/_compat.py:108` `[high]`
- `_FixupStream.readable() -> bool` `src/click/_compat.py:116` `[high]`
- `_FixupStream.writable() -> bool` `src/click/_compat.py:128` `[high]`
- `_FixupStream.seekable() -> bool` `src/click/_compat.py:143` `[high]`
- `_is_binary_reader(stream: t.IO[t.Any], default: bool) -> bool` `src/click/_compat.py:154` `[high]`
- `_is_binary_writer(stream: t.IO[t.Any], default: bool) -> bool` `src/click/_compat.py:163` `[high]`
- `_find_binary_reader(stream: t.IO[t.Any]) -> t.BinaryIO | None` `src/click/_compat.py:176` `[high]`
- `_find_binary_writer(stream: t.IO[t.Any]) -> t.BinaryIO | None` `src/click/_compat.py:194` `[high]`
- `_stream_is_misconfigured(stream: t.TextIO) -> bool` `src/click/_compat.py:212` `[high]`
- `_is_compat_stream_attr(stream: t.TextIO, attr: str, value: str | None) -> bool` `src/click/_compat.py:221` `[high]`
- `_is_compatible_text_stream(stream: t.TextIO, encoding: str | None, errors: str | None) -> bool` `src/click/_compat.py:230` `[high]`
- `_force_correct_text_stream(text_stream: t.IO[t.Any], encoding: str | None, errors: str | None, is_binary: t.Callable[[t.IO[t.Any], bool], bool], find_binary: t.Callable[[t.IO[t.Any]], t.BinaryIO | None], force_readable: bool, force_writable: bool) -> t.TextIO` `src/click/_compat.py:241` `[high]`
- `_force_correct_text_reader(text_reader: t.IO[t.Any], encoding: str | None, errors: str | None, force_readable: bool) -> t.TextIO` `src/click/_compat.py:287` `[high]`
- `_force_correct_text_writer(text_writer: t.IO[t.Any], encoding: str | None, errors: str | None, force_writable: bool) -> t.TextIO` `src/click/_compat.py:303` `[high]`
- `get_binary_stdin() -> t.BinaryIO` `src/click/_compat.py:319` `[high]`
- `get_binary_stdout() -> t.BinaryIO` `src/click/_compat.py:326` `[high]`
- `get_binary_stderr() -> t.BinaryIO` `src/click/_compat.py:333` `[high]`
- `get_text_stdin(encoding: str | None, errors: str | None) -> t.TextIO` `src/click/_compat.py:340` `[high]`
- `get_text_stdout(encoding: str | None, errors: str | None) -> t.TextIO` `src/click/_compat.py:347` `[high]`
- `get_text_stderr(encoding: str | None, errors: str | None) -> t.TextIO` `src/click/_compat.py:354` `[high]`
- `_wrap_io_open(file: str | os.PathLike[str] | int, mode: str, encoding: str | None, errors: str | None) -> t.IO[t.Any]` `src/click/_compat.py:361` `[high]`
- `open_stream(filename: str | os.PathLike[str], mode: str, encoding: str | None, errors: str | None, atomic: bool) -> tuple[t.IO[t.Any], bool]` `src/click/_compat.py:374` `[high]`
- `_AtomicFile.__init__(f: t.IO[t.Any], tmp_filename: str, real_filename: str) -> None` `src/click/_compat.py:456` `[high]`
- `_AtomicFile.name() -> str` `src/click/_compat.py:463` `[high]`
- `_AtomicFile.close(delete: bool) -> None` `src/click/_compat.py:466` `[high]`
- `_AtomicFile.__getattr__(name: str) -> t.Any` `src/click/_compat.py:473` `[high]`
- `_AtomicFile.__enter__() -> _AtomicFile` `src/click/_compat.py:476` `[high]`
- `_AtomicFile.__exit__(exc_type: type[BaseException] | None, exc_value: BaseException | None, tb: TracebackType | None) -> None` `src/click/_compat.py:479` `[high]`
- `_AtomicFile.__repr__() -> str` `src/click/_compat.py:487` `[high]`
- `strip_ansi(value: str) -> str` `src/click/_compat.py:491` `[high]`
- `_is_jupyter_kernel_output(stream: t.IO[t.Any]) -> bool` `src/click/_compat.py:495` `[high]`
- `should_strip_ansi(stream: t.IO[t.Any] | None, color: bool | None) -> bool` `src/click/_compat.py:502` `[high]`
- `_get_argv_encoding() -> str` `src/click/_compat.py:527` `[high]`
- `_get_windows_console_stream(f: t.TextIO, encoding: str | None, errors: str | None) -> t.TextIO | None` `src/click/_compat.py:530` `[high]`
- `term_len(x: str) -> int` `src/click/_compat.py:536` `[high]`
- `isatty(stream: t.IO[t.Any]) -> bool` `src/click/_compat.py:540` `[high]`
- `_make_cached_stream_func(src_func: t.Callable[[], t.TextIO | None], wrapper_func: t.Callable[[], t.TextIO]) -> t.Callable[[], t.TextIO | None]` `src/click/_compat.py:547` `[high]`

## Depends on
- [click._winconsole](/modules/click._winconsole.md) `src/click/_compat.py:518` `[high]`

## Calls
- `get_text_stderr` calls [click._winconsole](/modules/click._winconsole.md) `_get_windows_console_stream` `src/click/_compat.py:355` `[medium]`
- `get_text_stdin` calls [click._winconsole](/modules/click._winconsole.md) `_get_windows_console_stream` `src/click/_compat.py:341` `[medium]`
- `get_text_stdout` calls [click._winconsole](/modules/click._winconsole.md) `_get_windows_console_stream` `src/click/_compat.py:348` `[medium]`
