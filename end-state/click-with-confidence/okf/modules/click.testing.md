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

> `[high]` is stated directly in the source; `[medium]` is a deterministic inference.

# click.testing

Source: `src/click/testing.py`

## Types
- `EchoingStdin` (class) `src/click/testing.py:32` `[high]`
- `_FDCapture` (class) `src/click/testing.py:80` `[high]`
- `BytesIOCopy` (class) extends `io.BytesIO` `src/click/testing.py:117` `[high]`
- `StreamMixer` (class) `src/click/testing.py:138` `[high]`
- `_NamedTextIOWrapper` (class) extends `io.TextIOWrapper` `src/click/testing.py:156` `[high]`
- `Result` (class) `src/click/testing.py:231` `[high]`
- `CliRunner` (class) `src/click/testing.py:317` `[high]`

## Functions and methods
- `EchoingStdin.__init__(input: t.BinaryIO, output: t.BinaryIO) -> None` `src/click/testing.py:37` `[high]`
- `EchoingStdin.__getattr__(x: str) -> t.Any` `src/click/testing.py:42` `[high]`
- `EchoingStdin._echo(rv: bytes) -> bytes` `src/click/testing.py:45` `[high]`
- `EchoingStdin.read(n: int) -> bytes` `src/click/testing.py:51` `[high]`
- `EchoingStdin.read1(n: int) -> bytes` `src/click/testing.py:54` `[high]`
- `EchoingStdin.readline(n: int) -> bytes` `src/click/testing.py:57` `[high]`
- `EchoingStdin.readlines() -> list[bytes]` `src/click/testing.py:60` `[high]`
- `EchoingStdin.__iter__() -> cabc.Iterator[bytes]` `src/click/testing.py:63` `[high]`
- `EchoingStdin.__repr__() -> str` `src/click/testing.py:66` `[high]`
- `_pause_echo(stream: EchoingStdin | None) -> cabc.Generator[None]` `src/click/testing.py:71` `[high]`
- `_FDCapture.__init__(targetfd: int) -> None` `src/click/testing.py:95` `[high]`
- `_FDCapture.start() -> None` `src/click/testing.py:100` `[high]`
- `_FDCapture.stop() -> bytes` `src/click/testing.py:105` `[high]`
- `BytesIOCopy.__init__(copy_to: io.BytesIO) -> None` `src/click/testing.py:125` `[high]`
- `BytesIOCopy.flush() -> None` `src/click/testing.py:129` `[high]`
- `BytesIOCopy.write(b: ReadableBuffer) -> int` `src/click/testing.py:133` `[high]`
- `StreamMixer.__init__() -> None` `src/click/testing.py:150` `[high]`
- `_NamedTextIOWrapper.__init__(buffer: t.BinaryIO, name: str, mode: str) -> None` `src/click/testing.py:172` `[high]`
- `_NamedTextIOWrapper.close() -> None` `src/click/testing.py:184` `[high]`
- `_NamedTextIOWrapper.fileno() -> int` `src/click/testing.py:192` `[high]`
- `_NamedTextIOWrapper.name() -> str` `src/click/testing.py:203` `[high]`
- `_NamedTextIOWrapper.mode() -> str` `src/click/testing.py:207` `[high]`
- `make_input_stream(input: str | bytes | t.IO[t.Any] | None, charset: str) -> t.BinaryIO` `src/click/testing.py:211` `[high]`
- `Result.__init__(runner: CliRunner, stdout_bytes: bytes, stderr_bytes: bytes, output_bytes: bytes, return_value: t.Any, exit_code: int, exception: BaseException | None, exc_info: ExceptionInfo | None) -> None` `src/click/testing.py:262` `[high]`
- `Result.output() -> str` `src/click/testing.py:283` `[high]`
- `Result.stdout() -> str` `src/click/testing.py:295` `[high]`
- `Result.stderr() -> str` `src/click/testing.py:302` `[high]`
- `Result.__repr__() -> str` `src/click/testing.py:312` `[high]`
- `CliRunner.__init__(charset: str, env: cabc.Mapping[str, str | None] | None, echo_stdin: bool, catch_exceptions: bool, capture: CaptureMode) -> None` `src/click/testing.py:360` `[high]`
- `CliRunner.get_default_prog_name(cli: Command) -> str` `src/click/testing.py:382` `[high]`
- `CliRunner.make_env(overrides: cabc.Mapping[str, str | None] | None) -> cabc.Mapping[str, str | None]` `src/click/testing.py:389` `[high]`
- `CliRunner.isolation(input: str | bytes | t.IO[t.Any] | None, env: cabc.Mapping[str, str | None] | None, color: bool) -> cabc.Generator[tuple[io.BytesIO, io.BytesIO, io.BytesIO]]` `src/click/testing.py:399` `[high]`
- `CliRunner.invoke(cli: Command, args: str | cabc.Sequence[str] | None, input: str | bytes | t.IO[t.Any] | None, env: cabc.Mapping[str, str | None] | None, catch_exceptions: bool | None, color: bool) -> Result` `src/click/testing.py:596` `[high]`
- `CliRunner.isolated_filesystem(temp_dir: str | os.PathLike[str] | None) -> cabc.Generator[str]` `src/click/testing.py:742` `[high]`

## Depends on
- [click._compat](/modules/click._compat.md) `src/click/testing.py:14` `[high]`
- [click.core](/modules/click.core.md) `src/click/testing.py:23` `[high]`
- [click.formatting](/modules/click.formatting.md) `src/click/testing.py:15` `[high]`
- [click.termui](/modules/click.termui.md) `src/click/testing.py:16` `[high]`
- [click.utils](/modules/click.utils.md) `src/click/testing.py:17` `[high]`

## Calls
- `make_input_stream` calls [click._compat](/modules/click._compat.md) `_find_binary_reader` `src/click/testing.py:216` `[medium]`
- `CliRunner.invoke` calls [click.core](/modules/click.core.md) `Command.main` `src/click/testing.py:687` `[medium]`

## Tests
- `test_testing`
