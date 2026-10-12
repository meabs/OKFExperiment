---
type: Code Module
title: "click._termui_impl"
description: "click._termui_impl: ProgressBar, _PagerWriter, Editor"
resource: "repo:src/click/_termui_impl.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "repo:src/click/_termui_impl.py"
    id: "88b97d9b7a5b"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

# click._termui_impl

Source: `src/click/_termui_impl.py`

## Types
- `ProgressBar` (class) extends `typing.Generic[V]` `src/click/_termui_impl.py:43`
- `_PagerWriter` (class) `src/click/_termui_impl.py:383`
- `Editor` (class) `src/click/_termui_impl.py:683`

## Functions and methods
- `ProgressBar.__init__(iterable: cabc.Iterable[V] | None, length: int | None, fill_char: str, empty_char: str, bar_template: str, info_sep: str, hidden: bool, show_eta: bool, show_percent: bool | None, show_pos: bool, item_show_func: t.Callable[[V | None], str | None] | None, label: str | None, file: t.TextIO | None, color: bool | None, update_min_steps: int, width: int) -> None` `src/click/_termui_impl.py:44`
- `ProgressBar.__enter__() -> ProgressBar[V]` `src/click/_termui_impl.py:115`
- `ProgressBar.__exit__(exc_type: type[BaseException] | None, exc_value: BaseException | None, tb: TracebackType | None) -> None` `src/click/_termui_impl.py:120`
- `ProgressBar.__iter__() -> cabc.Iterator[V]` `src/click/_termui_impl.py:128`
- `ProgressBar.__next__() -> V` `src/click/_termui_impl.py:134`
- `ProgressBar.render_finish() -> None` `src/click/_termui_impl.py:142`
- `ProgressBar.pct() -> float` `src/click/_termui_impl.py:157`
- `ProgressBar.time_per_iteration() -> float` `src/click/_termui_impl.py:163`
- `ProgressBar.eta() -> float` `src/click/_termui_impl.py:169`
- `ProgressBar.format_eta() -> str` `src/click/_termui_impl.py:174`
- `ProgressBar.format_pos() -> str` `src/click/_termui_impl.py:195`
- `ProgressBar.format_pct() -> str` `src/click/_termui_impl.py:201`
- `ProgressBar.format_bar() -> str` `src/click/_termui_impl.py:204`
- `ProgressBar.format_progress_line() -> str` `src/click/_termui_impl.py:223`
- `ProgressBar.render_progress() -> None` `src/click/_termui_impl.py:250`
- `ProgressBar.make_step(n_steps: int) -> None` `src/click/_termui_impl.py:296`
- `ProgressBar.update(n_steps: int, current_item: V | None) -> None` `src/click/_termui_impl.py:318`
- `ProgressBar.finish() -> None` `src/click/_termui_impl.py:344`
- `ProgressBar.generator() -> cabc.Iterator[V]` `src/click/_termui_impl.py:349`
- `_PagerWriter.__init__(stream: t.TextIO, color: bool) -> None` `src/click/_termui_impl.py:397`
- `_PagerWriter.write(text: str) -> int` `src/click/_termui_impl.py:401`
- `_PagerWriter.writelines(lines: cabc.Iterable[str]) -> None` `src/click/_termui_impl.py:407`
- `_PagerWriter.flush() -> None` `src/click/_termui_impl.py:411`
- `_PagerWriter.close() -> None` `src/click/_termui_impl.py:414`
- `_PagerWriter.__getattr__(name: str) -> t.Any` `src/click/_termui_impl.py:419`
- `_resolve_pager_command(cmd_parts: list[str]) -> tuple[Path, list[str]] | None` `src/click/_termui_impl.py:423`
- `_pager_contextmanager(color: bool | None) -> t.ContextManager[tuple[t.TextIO, bool | None]]` `src/click/_termui_impl.py:451`
- `get_pager_file(color: bool | None) -> t.Generator[t.TextIO, None, None]` `src/click/_termui_impl.py:497`
- `_less_uses_raw_mode(less_env: str, cmd_params: list[str]) -> bool` `src/click/_termui_impl.py:520`
- `_pipepager(cmd_path: Path, cmd_params: list[str], color: bool | None) -> t.Iterator[tuple[t.TextIO, bool | None]]` `src/click/_termui_impl.py:549`
- `_tempfilepager(cmd_path: Path, cmd_params: list[str], color: bool | None) -> t.Iterator[tuple[t.TextIO, bool | None]]` `src/click/_termui_impl.py:636`
- `_nullpager(stream: t.TextIO, color: bool | None) -> t.Iterator[tuple[t.TextIO, bool | None]]` `src/click/_termui_impl.py:671`
- `Editor.__init__(editor: str | None, env: cabc.Mapping[str, str] | None, require_save: bool, extension: str) -> None` `src/click/_termui_impl.py:684`
- `Editor.get_editor() -> str` `src/click/_termui_impl.py:696`
- `Editor.edit_files(filenames: cabc.Iterable[str | os.PathLike[str]]) -> None` `src/click/_termui_impl.py:713`
- `Editor.edit(text: str | bytes | bytearray | None) -> str | bytes | None` `src/click/_termui_impl.py:751`
- `open_url(url: str, wait: bool, locate: bool) -> int` `src/click/_termui_impl.py:799`
- `_translate_ch_to_exc(ch: str) -> None` `src/click/_termui_impl.py:869`
- `raw_terminal() -> cabc.Iterator[int]` `src/click/_termui_impl.py:938`
- `getchar(echo: bool) -> str` `src/click/_termui_impl.py:964`

## Depends on
- [click._compat](/modules/click._compat.md) `src/click/_termui_impl.py:22`
- [click.exceptions](/modules/click.exceptions.md) `src/click/_termui_impl.py:29`
- [click.utils](/modules/click.utils.md) `src/click/_termui_impl.py:30`

## Calls
- `_pager_contextmanager` calls [click._compat](/modules/click._compat.md) `isatty` `src/click/_termui_impl.py:462`
- `_tempfilepager` calls [click._compat](/modules/click._compat.md) `get_best_encoding` `src/click/_termui_impl.py:649`
- `getchar` calls [click._compat](/modules/click._compat.md) `get_best_encoding` `src/click/_termui_impl.py:966`
- `getchar` calls [click._compat](/modules/click._compat.md) `isatty` `src/click/_termui_impl.py:968`
- `raw_terminal` calls [click._compat](/modules/click._compat.md) `isatty` `src/click/_termui_impl.py:942`
- `ProgressBar.__init__` calls [click._compat](/modules/click._compat.md) `isatty` `src/click/_termui_impl.py:112`
- `ProgressBar.render_progress` calls [click._compat](/modules/click._compat.md) `term_len` `src/click/_termui_impl.py:268`
- `ProgressBar.render_progress` calls [click.utils](/modules/click.utils.md) `echo` `src/click/_termui_impl.py:258`
- `_PagerWriter.write` calls [click._compat](/modules/click._compat.md) `strip_ansi` `src/click/_termui_impl.py:403`
