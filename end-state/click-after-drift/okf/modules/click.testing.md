---
type: Code Module
title: "click.testing"
description: "click.testing: EchoingStdin, _FDCapture, BytesIOCopy, StreamMixer"
resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/testing.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/testing.py"
    sha256: "76f4e649bc53000d667c8c0deff1591970fa034b0f085a207165839b2301019a"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

# click.testing

Source: `src/click/testing.py`

## Types
- `EchoingStdin` (class) `src/click/testing.py:32`
- `_FDCapture` (class) `src/click/testing.py:80`
- `BytesIOCopy` (class) extends `io.BytesIO` `src/click/testing.py:117`
- `StreamMixer` (class) `src/click/testing.py:138`
- `_NamedTextIOWrapper` (class) extends `io.TextIOWrapper` `src/click/testing.py:156`
- `Result` (class) `src/click/testing.py:231`
- `CliRunner` (class) `src/click/testing.py:317`

## Functions and methods
- `EchoingStdin.__init__(input: t.BinaryIO, output: t.BinaryIO) -> None` `src/click/testing.py:37`
- `EchoingStdin.__getattr__(x: str) -> t.Any` `src/click/testing.py:42`
- `EchoingStdin._echo(rv: bytes) -> bytes` `src/click/testing.py:45`
- `EchoingStdin.read(n: int) -> bytes` `src/click/testing.py:51`
- `EchoingStdin.read1(n: int) -> bytes` `src/click/testing.py:54`
- `EchoingStdin.readline(n: int) -> bytes` `src/click/testing.py:57`
- `EchoingStdin.readlines() -> list[bytes]` `src/click/testing.py:60`
- `EchoingStdin.__iter__() -> cabc.Iterator[bytes]` `src/click/testing.py:63`
- `EchoingStdin.__repr__() -> str` `src/click/testing.py:66`
- `_pause_echo(stream: EchoingStdin | None) -> cabc.Generator[None]` `src/click/testing.py:71`
- `_FDCapture.__init__(targetfd: int) -> None` `src/click/testing.py:95`
- `_FDCapture.start() -> None` `src/click/testing.py:100`
- `_FDCapture.stop() -> bytes` `src/click/testing.py:105`
- `BytesIOCopy.__init__(copy_to: io.BytesIO) -> None` `src/click/testing.py:125`
- `BytesIOCopy.flush() -> None` `src/click/testing.py:129`
- `BytesIOCopy.write(b: ReadableBuffer) -> int` `src/click/testing.py:133`
- `StreamMixer.__init__() -> None` `src/click/testing.py:150`
- `_NamedTextIOWrapper.__init__(buffer: t.BinaryIO, name: str, mode: str) -> None` `src/click/testing.py:172`
- `_NamedTextIOWrapper.close() -> None` `src/click/testing.py:184`
- `_NamedTextIOWrapper.fileno() -> int` `src/click/testing.py:192`
- `_NamedTextIOWrapper.name() -> str` `src/click/testing.py:203`
- `_NamedTextIOWrapper.mode() -> str` `src/click/testing.py:207`
- `make_input_stream(input: str | bytes | t.IO[t.Any] | None, charset: str) -> t.BinaryIO` `src/click/testing.py:211`
- `Result.__init__(runner: CliRunner, stdout_bytes: bytes, stderr_bytes: bytes, output_bytes: bytes, return_value: t.Any, exit_code: int, exception: BaseException | None, exc_info: ExceptionInfo | None) -> None` `src/click/testing.py:262`
- `Result.output() -> str` `src/click/testing.py:283`
- `Result.stdout() -> str` `src/click/testing.py:295`
- `Result.stderr() -> str` `src/click/testing.py:302`
- `Result.__repr__() -> str` `src/click/testing.py:312`
- `CliRunner.__init__(charset: str, env: cabc.Mapping[str, str | None] | None, echo_stdin: bool, catch_exceptions: bool, capture: CaptureMode) -> None` `src/click/testing.py:360`
- `CliRunner.get_default_prog_name(cli: Command) -> str` `src/click/testing.py:382`
- `CliRunner.make_env(overrides: cabc.Mapping[str, str | None] | None) -> cabc.Mapping[str, str | None]` `src/click/testing.py:389`
- `CliRunner.isolation(input: str | bytes | t.IO[t.Any] | None, env: cabc.Mapping[str, str | None] | None, color: bool) -> cabc.Generator[tuple[io.BytesIO, io.BytesIO, io.BytesIO]]` `src/click/testing.py:399`
- `CliRunner.invoke(cli: Command, args: str | cabc.Sequence[str] | None, input: str | bytes | t.IO[t.Any] | None, env: cabc.Mapping[str, str | None] | None, catch_exceptions: bool | None, color: bool) -> Result` `src/click/testing.py:596`
- `CliRunner.isolated_filesystem(temp_dir: str | os.PathLike[str] | None) -> cabc.Generator[str]` `src/click/testing.py:742`

## Depends on
- [click._compat](/modules/click._compat.md) `src/click/testing.py:14`
- [click.core](/modules/click.core.md) `src/click/testing.py:23`
- [click.formatting](/modules/click.formatting.md) `src/click/testing.py:15`
- [click.termui](/modules/click.termui.md) `src/click/testing.py:16`
- [click.utils](/modules/click.utils.md) `src/click/testing.py:17`

## Calls
- `make_input_stream` calls [click._compat](/modules/click._compat.md) `_find_binary_reader` `src/click/testing.py:216`
- `CliRunner.invoke` calls [click.core](/modules/click.core.md) `Command.main` `src/click/testing.py:687`

## Tests
- `test_testing`
