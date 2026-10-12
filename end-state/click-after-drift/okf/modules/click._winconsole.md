---
type: Code Module
title: "click._winconsole"
description: "click._winconsole: Py_buffer, _WindowsConsoleRawIOBase, _WindowsConsoleReader, _WindowsConsoleWriter"
resource: "repo:src/click/_winconsole.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "repo:src/click/_winconsole.py"
    id: "a6f0d49ef0be"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

# click._winconsole

Source: `src/click/_winconsole.py`

## Types
- `Py_buffer` (class) extends `ctypes.Structure` `src/click/_winconsole.py:83`
- `_WindowsConsoleRawIOBase` (class) extends `io.RawIOBase` `src/click/_winconsole.py:114`
- `_WindowsConsoleReader` (class) extends `click._winconsole._WindowsConsoleRawIOBase` `src/click/_winconsole.py:123`
- `_WindowsConsoleWriter` (class) extends `click._winconsole._WindowsConsoleRawIOBase` `src/click/_winconsole.py:158`
- `ConsoleStream` (class) `src/click/_winconsole.py:190`

## Functions and methods
- `get_buffer(obj: Buffer, writable: bool) -> Array[c_char]` `src/click/_winconsole.py:101`
- `_WindowsConsoleRawIOBase.__init__(handle: int | None) -> None` `src/click/_winconsole.py:115`
- `_WindowsConsoleRawIOBase.isatty() -> t.Literal[True]` `src/click/_winconsole.py:118`
- `_WindowsConsoleReader.readable() -> t.Literal[True]` `src/click/_winconsole.py:124`
- `_WindowsConsoleReader.readinto(b: Buffer) -> int` `src/click/_winconsole.py:127`
- `_WindowsConsoleWriter.writable() -> t.Literal[True]` `src/click/_winconsole.py:159`
- `_WindowsConsoleWriter._get_error_message(errno: int) -> str` `src/click/_winconsole.py:163`
- `_WindowsConsoleWriter.write(b: Buffer) -> int` `src/click/_winconsole.py:170`
- `ConsoleStream.__init__(text_stream: t.TextIO, byte_stream: t.BinaryIO) -> None` `src/click/_winconsole.py:191`
- `ConsoleStream.name() -> str` `src/click/_winconsole.py:196`
- `ConsoleStream.write(x: t.AnyStr) -> int` `src/click/_winconsole.py:199`
- `ConsoleStream.writelines(lines: cabc.Iterable[t.AnyStr]) -> None` `src/click/_winconsole.py:208`
- `ConsoleStream.__getattr__(name: str) -> t.Any` `src/click/_winconsole.py:212`
- `ConsoleStream.isatty() -> bool` `src/click/_winconsole.py:215`
- `ConsoleStream.__repr__() -> str` `src/click/_winconsole.py:218`
- `_get_text_stdin(buffer_stream: t.BinaryIO) -> t.TextIO` `src/click/_winconsole.py:222`
- `_get_text_stdout(buffer_stream: t.BinaryIO) -> t.TextIO` `src/click/_winconsole.py:232`
- `_get_text_stderr(buffer_stream: t.BinaryIO) -> t.TextIO` `src/click/_winconsole.py:242`
- `_is_console(f: t.TextIO) -> bool` `src/click/_winconsole.py:259`
- `_get_windows_console_stream(f: t.TextIO, encoding: str | None, errors: str | None) -> t.TextIO | None` `src/click/_winconsole.py:272`

## Depends on
- [click._compat](/modules/click._compat.md) `src/click/_winconsole.py:33`
