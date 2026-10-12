---
type: Code Module
title: "click._termui_impl"
description: "click._termui_impl: ProgressBar, _PagerWriter, Editor"
resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/_termui_impl.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/_termui_impl.py"
    sha256: "88b97d9b7a5b947b10a16d8ab269837bc84c7e55c28ba72ea5f2fb339112336a"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

> `[high]` is stated directly in the source; `[medium]` is a deterministic inference.

# click._termui_impl

Source: `src/click/_termui_impl.py`

## Types
- `ProgressBar` (class) extends `typing.Generic[V]` `src/click/_termui_impl.py:43` `[high]`
- `_PagerWriter` (class) `src/click/_termui_impl.py:383` `[high]`
- `Editor` (class) `src/click/_termui_impl.py:683` `[high]`

## Functions and methods
- `ProgressBar.__init__(iterable: cabc.Iterable[V] | None, length: int | None, fill_char: str, empty_char: str, bar_template: str, info_sep: str, hidden: bool, show_eta: bool, show_percent: bool | None, show_pos: bool, item_show_func: t.Callable[[V | None], str | None] | None, label: str | None, file: t.TextIO | None, color: bool | None, update_min_steps: int, width: int) -> None` `src/click/_termui_impl.py:44` `[high]`
- `ProgressBar.__enter__() -> ProgressBar[V]` `src/click/_termui_impl.py:115` `[high]`
- `ProgressBar.__exit__(exc_type: type[BaseException] | None, exc_value: BaseException | None, tb: TracebackType | None) -> None` `src/click/_termui_impl.py:120` `[high]`
- `ProgressBar.__iter__() -> cabc.Iterator[V]` `src/click/_termui_impl.py:128` `[high]`
- `ProgressBar.__next__() -> V` `src/click/_termui_impl.py:134` `[high]`
- `ProgressBar.render_finish() -> None` `src/click/_termui_impl.py:142` `[high]`
- `ProgressBar.pct() -> float` `src/click/_termui_impl.py:157` `[high]`
- `ProgressBar.time_per_iteration() -> float` `src/click/_termui_impl.py:163` `[high]`
- `ProgressBar.eta() -> float` `src/click/_termui_impl.py:169` `[high]`
- `ProgressBar.format_eta() -> str` `src/click/_termui_impl.py:174` `[high]`
- `ProgressBar.format_pos() -> str` `src/click/_termui_impl.py:195` `[high]`
- `ProgressBar.format_pct() -> str` `src/click/_termui_impl.py:201` `[high]`
- `ProgressBar.format_bar() -> str` `src/click/_termui_impl.py:204` `[high]`
- `ProgressBar.format_progress_line() -> str` `src/click/_termui_impl.py:223` `[high]`
- `ProgressBar.render_progress() -> None` `src/click/_termui_impl.py:250` `[high]`
- `ProgressBar.make_step(n_steps: int) -> None` `src/click/_termui_impl.py:296` `[high]`
- `ProgressBar.update(n_steps: int, current_item: V | None) -> None` `src/click/_termui_impl.py:318` `[high]`
- `ProgressBar.finish() -> None` `src/click/_termui_impl.py:344` `[high]`
- `ProgressBar.generator() -> cabc.Iterator[V]` `src/click/_termui_impl.py:349` `[high]`
- `_PagerWriter.__init__(stream: t.TextIO, color: bool) -> None` `src/click/_termui_impl.py:397` `[high]`
- `_PagerWriter.write(text: str) -> int` `src/click/_termui_impl.py:401` `[high]`
- `_PagerWriter.writelines(lines: cabc.Iterable[str]) -> None` `src/click/_termui_impl.py:407` `[high]`
- `_PagerWriter.flush() -> None` `src/click/_termui_impl.py:411` `[high]`
- `_PagerWriter.close() -> None` `src/click/_termui_impl.py:414` `[high]`
- `_PagerWriter.__getattr__(name: str) -> t.Any` `src/click/_termui_impl.py:419` `[high]`
- `_resolve_pager_command(cmd_parts: list[str]) -> tuple[Path, list[str]] | None` `src/click/_termui_impl.py:423` `[high]`
- `_pager_contextmanager(color: bool | None) -> t.ContextManager[tuple[t.TextIO, bool | None]]` `src/click/_termui_impl.py:451` `[high]`
- `get_pager_file(color: bool | None) -> t.Generator[t.TextIO, None, None]` `src/click/_termui_impl.py:497` `[high]`
- `_less_uses_raw_mode(less_env: str, cmd_params: list[str]) -> bool` `src/click/_termui_impl.py:520` `[high]`
- `_pipepager(cmd_path: Path, cmd_params: list[str], color: bool | None) -> t.Iterator[tuple[t.TextIO, bool | None]]` `src/click/_termui_impl.py:549` `[high]`
- `_tempfilepager(cmd_path: Path, cmd_params: list[str], color: bool | None) -> t.Iterator[tuple[t.TextIO, bool | None]]` `src/click/_termui_impl.py:636` `[high]`
- `_nullpager(stream: t.TextIO, color: bool | None) -> t.Iterator[tuple[t.TextIO, bool | None]]` `src/click/_termui_impl.py:671` `[high]`
- `Editor.__init__(editor: str | None, env: cabc.Mapping[str, str] | None, require_save: bool, extension: str) -> None` `src/click/_termui_impl.py:684` `[high]`
- `Editor.get_editor() -> str` `src/click/_termui_impl.py:696` `[high]`
- `Editor.edit_files(filenames: cabc.Iterable[str | os.PathLike[str]]) -> None` `src/click/_termui_impl.py:713` `[high]`
- `Editor.edit(text: str | bytes | bytearray | None) -> str | bytes | None` `src/click/_termui_impl.py:751` `[high]`
- `open_url(url: str, wait: bool, locate: bool) -> int` `src/click/_termui_impl.py:799` `[high]`
- `_translate_ch_to_exc(ch: str) -> None` `src/click/_termui_impl.py:869` `[high]`
- `raw_terminal() -> cabc.Iterator[int]` `src/click/_termui_impl.py:938` `[high]`
- `getchar(echo: bool) -> str` `src/click/_termui_impl.py:964` `[high]`

## Depends on
- [click._compat](/modules/click._compat.md) `src/click/_termui_impl.py:22` `[high]`
- [click.exceptions](/modules/click.exceptions.md) `src/click/_termui_impl.py:29` `[high]`
- [click.utils](/modules/click.utils.md) `src/click/_termui_impl.py:30` `[high]`

## Calls
- `_pager_contextmanager` calls [click._compat](/modules/click._compat.md) `isatty` `src/click/_termui_impl.py:462` `[medium]`
- `_tempfilepager` calls [click._compat](/modules/click._compat.md) `get_best_encoding` `src/click/_termui_impl.py:649` `[medium]`
- `getchar` calls [click._compat](/modules/click._compat.md) `get_best_encoding` `src/click/_termui_impl.py:966` `[medium]`
- `getchar` calls [click._compat](/modules/click._compat.md) `isatty` `src/click/_termui_impl.py:968` `[medium]`
- `raw_terminal` calls [click._compat](/modules/click._compat.md) `isatty` `src/click/_termui_impl.py:942` `[medium]`
- `ProgressBar.__init__` calls [click._compat](/modules/click._compat.md) `isatty` `src/click/_termui_impl.py:112` `[medium]`
- `ProgressBar.render_progress` calls [click._compat](/modules/click._compat.md) `term_len` `src/click/_termui_impl.py:268` `[medium]`
- `ProgressBar.render_progress` calls [click.utils](/modules/click.utils.md) `echo` `src/click/_termui_impl.py:258` `[medium]`
- `_PagerWriter.write` calls [click._compat](/modules/click._compat.md) `strip_ansi` `src/click/_termui_impl.py:403` `[medium]`
