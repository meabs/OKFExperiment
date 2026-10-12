---
type: Code Module
title: "click._winconsole"
description: "click._winconsole: Py_buffer, _WindowsConsoleRawIOBase, _WindowsConsoleReader, _WindowsConsoleWriter"
resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/_winconsole.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/_winconsole.py"
    sha256: "a6f0d49ef0be806a9730bd64a2e5b373a95d49de91fd7728595ff31d773f2db7"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

> `[high]` is stated directly in the source; `[medium]` is a deterministic inference.

# click._winconsole

Source: `src/click/_winconsole.py`

## Types
- `Py_buffer` (class) extends `ctypes.Structure` `src/click/_winconsole.py:83` `[high]`
- `_WindowsConsoleRawIOBase` (class) extends `io.RawIOBase` `src/click/_winconsole.py:114` `[high]`
- `_WindowsConsoleReader` (class) extends `click._winconsole._WindowsConsoleRawIOBase` `src/click/_winconsole.py:123` `[high]`
- `_WindowsConsoleWriter` (class) extends `click._winconsole._WindowsConsoleRawIOBase` `src/click/_winconsole.py:158` `[high]`
- `ConsoleStream` (class) `src/click/_winconsole.py:190` `[high]`

## Functions and methods
- `get_buffer(obj: Buffer, writable: bool) -> Array[c_char]` `src/click/_winconsole.py:101` `[high]`
- `_WindowsConsoleRawIOBase.__init__(handle: int | None) -> None` `src/click/_winconsole.py:115` `[high]`
- `_WindowsConsoleRawIOBase.isatty() -> t.Literal[True]` `src/click/_winconsole.py:118` `[high]`
- `_WindowsConsoleReader.readable() -> t.Literal[True]` `src/click/_winconsole.py:124` `[high]`
- `_WindowsConsoleReader.readinto(b: Buffer) -> int` `src/click/_winconsole.py:127` `[high]`
- `_WindowsConsoleWriter.writable() -> t.Literal[True]` `src/click/_winconsole.py:159` `[high]`
- `_WindowsConsoleWriter._get_error_message(errno: int) -> str` `src/click/_winconsole.py:163` `[high]`
- `_WindowsConsoleWriter.write(b: Buffer) -> int` `src/click/_winconsole.py:170` `[high]`
- `ConsoleStream.__init__(text_stream: t.TextIO, byte_stream: t.BinaryIO) -> None` `src/click/_winconsole.py:191` `[high]`
- `ConsoleStream.name() -> str` `src/click/_winconsole.py:196` `[high]`
- `ConsoleStream.write(x: t.AnyStr) -> int` `src/click/_winconsole.py:199` `[high]`
- `ConsoleStream.writelines(lines: cabc.Iterable[t.AnyStr]) -> None` `src/click/_winconsole.py:208` `[high]`
- `ConsoleStream.__getattr__(name: str) -> t.Any` `src/click/_winconsole.py:212` `[high]`
- `ConsoleStream.isatty() -> bool` `src/click/_winconsole.py:215` `[high]`
- `ConsoleStream.__repr__() -> str` `src/click/_winconsole.py:218` `[high]`
- `_get_text_stdin(buffer_stream: t.BinaryIO) -> t.TextIO` `src/click/_winconsole.py:222` `[high]`
- `_get_text_stdout(buffer_stream: t.BinaryIO) -> t.TextIO` `src/click/_winconsole.py:232` `[high]`
- `_get_text_stderr(buffer_stream: t.BinaryIO) -> t.TextIO` `src/click/_winconsole.py:242` `[high]`
- `_is_console(f: t.TextIO) -> bool` `src/click/_winconsole.py:259` `[high]`
- `_get_windows_console_stream(f: t.TextIO, encoding: str | None, errors: str | None) -> t.TextIO | None` `src/click/_winconsole.py:272` `[high]`

## Depends on
- [click._compat](/modules/click._compat.md) `src/click/_winconsole.py:33` `[high]`
