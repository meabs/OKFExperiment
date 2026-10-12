---
type: Code Module
title: "click.termui"
description: "click.termui: _mask_hidden_input, hidden_prompt_func, _readline_prompt, _build_prompt"
resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/termui.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/termui.py"
    sha256: "16f6546b36d647d191788fc912e32d93e8b64289517f004e6d9604f4896ad1ca"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

# click.termui

Source: `src/click/termui.py`

## Functions and methods
- `_mask_hidden_input(message: str, value: str) -> str` `src/click/termui.py:61`
- `hidden_prompt_func(prompt: str) -> str` `src/click/termui.py:79`
- `_readline_prompt(func: t.Callable[[str], str], text: str, err: bool) -> str` `src/click/termui.py:85`
- `_build_prompt(text: str, suffix: str, show_default: bool | str, default: object | None, show_choices: bool, type: object | None) -> str` `src/click/termui.py:108`
- `_format_default(default: V) -> V | str` `src/click/termui.py:128`
- `prompt(text: str, default: V | str | None, hide_input: bool, confirmation_prompt: bool | str, type: ParamType[V, str] | type[V] | None, value_proc: t.Callable[[str], V] | None, prompt_suffix: str, show_default: bool | str, err: bool, show_choices: bool) -> V` `src/click/termui.py:168`
- `confirm(text: str, default: bool | None, abort: bool, prompt_suffix: str, show_default: bool, err: bool) -> bool` `src/click/termui.py:289`
- `get_pager_file(color: bool | None) -> t.ContextManager[t.TextIO]` `src/click/termui.py:348`
- `echo_via_pager(text_or_generator: cabc.Iterable[str] | t.Callable[[], cabc.Iterable[str]] | str, color: bool | None) -> None` `src/click/termui.py:367`
- `progressbar(iterable: cabc.Iterable[V] | None, length: int | None, label: str | None, hidden: bool, show_eta: bool, show_percent: bool | None, show_pos: bool, item_show_func: t.Callable[[V | None], str | None] | None, fill_char: str, empty_char: str, bar_template: str, info_sep: str, width: int, file: t.TextIO | None, color: bool | None, update_min_steps: int) -> ProgressBar[V]` `src/click/termui.py:443`
- `clear() -> None` `src/click/termui.py:602`
- `_interpret_color(color: int | tuple[int, int, int] | str, offset: int) -> str` `src/click/termui.py:616`
- `style(text: t.Any, fg: int | tuple[int, int, int] | str | None, bg: int | tuple[int, int, int] | str | None, bold: bool | None, dim: bool | None, underline: bool | None, overline: bool | None, italic: bool | None, blink: bool | None, reverse: bool | None, strikethrough: bool | None, reset: bool) -> str` `src/click/termui.py:641`
- `unstyle(text: str) -> str` `src/click/termui.py:768`
- `secho(message: t.Any | None, file: t.IO[t.AnyStr] | None, nl: bool, err: bool, color: bool | None) -> None` `src/click/termui.py:780`
- `edit(text: str | bytes | bytearray | None, editor: str | None, env: cabc.Mapping[str, str] | None, require_save: bool, extension: str, filename: str | os.PathLike[str] | cabc.Iterable[str | os.PathLike[str]] | None) -> str | bytes | bytearray | None` `src/click/termui.py:848`
- `launch(url: str, wait: bool, locate: bool) -> int` `src/click/termui.py:923`
- `getchar(echo: bool) -> str` `src/click/termui.py:957`
- `raw_terminal() -> AbstractContextManager[int]` `src/click/termui.py:987`
- `pause(info: str | None, err: bool) -> None` `src/click/termui.py:993`

## Depends on
- [click._compat](/modules/click._compat.md) `src/click/termui.py:15`
- [click._termui_impl](/modules/click._termui_impl.md) `src/click/termui.py:28`
- [click.exceptions](/modules/click.exceptions.md) `src/click/termui.py:18`
- [click.globals](/modules/click.globals.md) `src/click/termui.py:20`
- [click.types](/modules/click.types.md) `src/click/termui.py:21`
- [click.utils](/modules/click.utils.md) `src/click/termui.py:24`

## Calls
- `_readline_prompt` calls [click._compat](/modules/click._compat.md) `should_strip_ansi` `src/click/termui.py:99`
- `_readline_prompt` calls [click._compat](/modules/click._compat.md) `strip_ansi` `src/click/termui.py:100`
- `_readline_prompt` calls [click.globals](/modules/click.globals.md) `resolve_color_default` `src/click/termui.py:99`
- `clear` calls [click._compat](/modules/click._compat.md) `isatty` `src/click/termui.py:609`
- `clear` calls [click.utils](/modules/click.utils.md) `echo` `src/click/termui.py:613`
- `confirm` calls [click.utils](/modules/click.utils.md) `echo` `src/click/termui.py:340`
- `get_pager_file` calls [click.globals](/modules/click.globals.md) `resolve_color_default` `src/click/termui.py:362`
- `pause` calls [click._compat](/modules/click._compat.md) `isatty` `src/click/termui.py:1009`
- `pause` calls [click.utils](/modules/click.utils.md) `echo` `src/click/termui.py:1017`
- `progressbar` calls [click.globals](/modules/click.globals.md) `resolve_color_default` `src/click/termui.py:581`
- `prompt` calls [click.types](/modules/click.types.md) `convert_type` `src/click/termui.py:248`
- `prompt` calls [click.utils](/modules/click.utils.md) `echo` `src/click/termui.py:244`
- `secho` calls [click.utils](/modules/click.utils.md) `echo` `src/click/termui.py:811`
- `unstyle` calls [click._compat](/modules/click._compat.md) `strip_ansi` `src/click/termui.py:777`
