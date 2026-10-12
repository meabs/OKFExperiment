---
type: Code Module
title: "click.core"
description: "click.core: ParameterSource, Context, Command, _FakeSubclassCheck"
resource: "repo:src/click/core.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "repo:src/click/core.py"
    id: "26307e89b7b2"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

# click.core

Source: `src/click/core.py`

## Types
- `ParameterSource` (class) extends `enum.IntEnum` `src/click/core.py:199`
- `Context` (class) `src/click/core.py:238`
- `Command` (class) `src/click/core.py:989`
- `_FakeSubclassCheck` (class) extends `type` `src/click/core.py:1688`
- `_BaseCommand` (class) extends `click.core.Command` `src/click/core.py:1696`
- `Group` (class) extends `click.core.Command` `src/click/core.py:1703`
- `_MultiCommand` (class) extends `click.core.Group` `src/click/core.py:2166`
- `CommandCollection` (class) extends `click.core.Group` `src/click/core.py:2173`
- `Parameter` (class) extends `abc.ABC` `src/click/core.py:2241`
- `Option` (class) extends `click.core.Parameter` `src/click/core.py:3057`
- `Argument` (class) extends `click.core.Parameter` `src/click/core.py:3894`

## Functions and methods
- `_complete_visible_commands(ctx: Context, incomplete: str) -> cabc.Iterator[tuple[str, Command]]` `src/click/core.py:64`
- `_check_nested_chain(base_command: Group, cmd_name: str, cmd: Command, register: bool) -> None` `src/click/core.py:83`
- `_echo_aborted() -> None` `src/click/core.py:103`
- `_outside_click_stacklevel(skip: cabc.Container[str]) -> int` `src/click/core.py:108`
- `_format_deprecated_label(deprecated: bool | str) -> str` `src/click/core.py:132`
- `_format_deprecated_suffix(deprecated: bool | str) -> str` `src/click/core.py:140`
- `batch(iterable: cabc.Iterable[V], batch_size: int) -> list[tuple[V, ...]]` `src/click/core.py:149`
- `augment_usage_errors(ctx: Context, param: Parameter | None) -> cabc.Generator[None]` `src/click/core.py:154`
- `iter_params_for_processing(invocation_order: cabc.Sequence[Parameter], declaration_order: cabc.Sequence[Parameter]) -> list[Parameter]` `src/click/core.py:172`
- `Context.__init__(command: Command, parent: Context | None, info_name: str | None, obj: t.Any | None, auto_envvar_prefix: str | None, default_map: cabc.MutableMapping[str, t.Any] | None, terminal_width: int | None, max_content_width: int | None, resilient_parsing: bool, allow_extra_args: bool | None, allow_interspersed_args: bool | None, ignore_unknown_options: bool | None, help_option_names: list[str] | None, token_normalize_func: t.Callable[[str], str] | None, color: bool | None, show_default: bool | None) -> None` `src/click/core.py:370`
- `Context.protected_args() -> list[str]` `src/click/core.py:547`
- `Context.to_info_dict() -> dict[str, t.Any]` `src/click/core.py:558`
- `Context.__enter__() -> Self` `src/click/core.py:579`
- `Context.__exit__(exc_type: type[BaseException] | None, exc_value: BaseException | None, tb: TracebackType | None) -> bool | None` `src/click/core.py:584`
- `Context.scope(cleanup: bool) -> cabc.Generator[Context]` `src/click/core.py:599`
- `Context.meta() -> dict[str, t.Any]` `src/click/core.py:637`
- `Context.make_formatter() -> HelpFormatter` `src/click/core.py:664`
- `Context.with_resource(context_manager: AbstractContextManager[V]) -> V` `src/click/core.py:678`
- `Context.call_on_close(f: t.Callable[..., t.Any]) -> t.Callable[..., t.Any]` `src/click/core.py:707`
- `Context.close() -> None` `src/click/core.py:719`
- `Context._close_with_exception_info(exc_type: type[BaseException] | None, exc_value: BaseException | None, tb: TracebackType | None) -> bool | None` `src/click/core.py:726`
- `Context.command_path() -> str` `src/click/core.py:745`
- `Context.find_root() -> Context` `src/click/core.py:763`
- `Context.find_object(object_type: type[V]) -> V | None` `src/click/core.py:770`
- `Context.ensure_object(object_type: type[V]) -> V` `src/click/core.py:782`
- `Context._default_map_has(name: str | None) -> bool` `src/click/core.py:791`
- `Context.lookup_default(name: str, call: bool) -> t.Any | None` `src/click/core.py:815`
- `Context.fail(message: str) -> t.NoReturn` `src/click/core.py:837`
- `Context.abort() -> t.NoReturn` `src/click/core.py:845`
- `Context.exit(code: int) -> t.NoReturn` `src/click/core.py:849`
- `Context.get_usage() -> str` `src/click/core.py:859`
- `Context.get_help() -> str` `src/click/core.py:865`
- `Context._make_sub_context(command: Command) -> Context` `src/click/core.py:871`
- `Context.invoke(callback: Command | t.Callable[..., V]) -> t.Any | V` `src/click/core.py:887`
- `Context.forward(cmd: Command) -> t.Any` `src/click/core.py:942`
- `Context.set_parameter_source(name: str, source: ParameterSource) -> None` `src/click/core.py:961`
- `Context.get_parameter_source(name: str) -> ParameterSource | None` `src/click/core.py:970`
- `Command.__init__(name: str | None, context_settings: cabc.MutableMapping[str, t.Any] | None, callback: t.Callable[..., t.Any] | None, params: list[Parameter] | None, help: str | None, epilog: str | None, short_help: str | None, options_metavar: str | None, add_help_option: bool, no_args_is_help: bool, hidden: bool, deprecated: bool | str) -> None` `src/click/core.py:1065`
- `Command.to_info_dict(ctx: Context) -> dict[str, t.Any]` `src/click/core.py:1109`
- `Command.__repr__() -> str` `src/click/core.py:1120`
- `Command.get_usage(ctx: Context) -> str` `src/click/core.py:1123`
- `Command.get_params(ctx: Context) -> list[Parameter]` `src/click/core.py:1132`
- `Command.format_usage(ctx: Context, formatter: HelpFormatter) -> None` `src/click/core.py:1188`
- `Command.collect_usage_pieces(ctx: Context) -> list[str]` `src/click/core.py:1196`
- `Command.get_help_option_names(ctx: Context) -> list[str]` `src/click/core.py:1207`
- `Command.get_help_option(ctx: Context) -> Option | None` `src/click/core.py:1222`
- `Command.make_parser(ctx: Context) -> _OptionParser` `src/click/core.py:1256`
- `Command.get_help(ctx: Context) -> str` `src/click/core.py:1263`
- `Command.get_short_help_str(limit: int) -> str` `src/click/core.py:1272`
- `Command.format_help(ctx: Context, formatter: HelpFormatter) -> None` `src/click/core.py:1288`
- `Command.format_help_text(ctx: Context, formatter: HelpFormatter) -> None` `src/click/core.py:1307`
- `Command.format_options(ctx: Context, formatter: HelpFormatter) -> None` `src/click/core.py:1325`
- `Command.format_arguments(ctx: Context, formatter: HelpFormatter) -> None` `src/click/core.py:1337`
- `Command.format_epilog(ctx: Context, formatter: HelpFormatter) -> None` `src/click/core.py:1350`
- `Command.make_context(info_name: str | None, args: list[str], parent: Context | None) -> Context` `src/click/core.py:1359`
- `Command.parse_args(ctx: Context, args: list[str]) -> list[str]` `src/click/core.py:1396`
- `Command.invoke(ctx: Context) -> t.Any` `src/click/core.py:1432`
- `Command.shell_complete(ctx: Context, incomplete: str) -> list[CompletionItem]` `src/click/core.py:1448`
- `Command.main(args: cabc.Sequence[str] | None, prog_name: str | None, complete_var: str | None, standalone_mode: bool, windows_expand_args: bool) -> t.Any` `src/click/core.py:1515`
- `Command._main_shell_completion(ctx_args: cabc.MutableMapping[str, t.Any], prog_name: str, complete_var: str | None) -> None` `src/click/core.py:1651`
- `Command.__call__() -> t.Any` `src/click/core.py:1683`
- `_FakeSubclassCheck.__subclasscheck__(subclass: type) -> bool` `src/click/core.py:1689`
- `_FakeSubclassCheck.__instancecheck__(instance: t.Any) -> bool` `src/click/core.py:1692`
- `Group.__init__(name: str | None, commands: cabc.MutableMapping[str, Command] | cabc.Sequence[Command] | None, invoke_without_command: bool, no_args_is_help: bool | None, subcommand_metavar: str | None, chain: bool, result_callback: t.Callable[..., t.Any] | None) -> None` `src/click/core.py:1762`
- `Group.to_info_dict(ctx: Context) -> dict[str, t.Any]` `src/click/core.py:1817`
- `Group.add_command(cmd: Command, name: str | None) -> None` `src/click/core.py:1835`
- `Group.command() -> t.Callable[[t.Callable[..., t.Any]], Command] | Command` `src/click/core.py:1853`
- `Group.group() -> t.Callable[[t.Callable[..., t.Any]], Group] | Group` `src/click/core.py:1902`
- `Group.result_callback(replace: bool) -> t.Callable[[F], F]` `src/click/core.py:1946`
- `Group.get_command(ctx: Context, cmd_name: str) -> Command | None` `src/click/core.py:1991`
- `Group.list_commands(ctx: Context) -> list[str]` `src/click/core.py:1997`
- `Group.collect_usage_pieces(ctx: Context) -> list[str]` `src/click/core.py:2001`
- `Group.format_options(ctx: Context, formatter: HelpFormatter) -> None` `src/click/core.py:2006`
- `Group.format_commands(ctx: Context, formatter: HelpFormatter) -> None` `src/click/core.py:2010`
- `Group.parse_args(ctx: Context, args: list[str]) -> list[str]` `src/click/core.py:2038`
- `Group.invoke(ctx: Context) -> t.Any` `src/click/core.py:2052`
- `Group.resolve_command(ctx: Context, args: list[str]) -> tuple[str | None, Command | None, list[str]]` `src/click/core.py:2120`
- `Group.shell_complete(ctx: Context, incomplete: str) -> list[CompletionItem]` `src/click/core.py:2146`
- `CommandCollection.__init__(name: str | None, sources: list[Group] | None) -> None` `src/click/core.py:2191`
- `CommandCollection.add_source(group: Group) -> None` `src/click/core.py:2201`
- `CommandCollection.get_command(ctx: Context, cmd_name: str) -> Command | None` `src/click/core.py:2205`
- `CommandCollection.list_commands(ctx: Context) -> list[str]` `src/click/core.py:2222`
- `_check_iter(value: cabc.Iterable[V]) -> cabc.Iterator[V]` `src/click/core.py:2231`
- `Parameter.__init_subclass__() -> None` `src/click/core.py:2392`
- `Parameter.__init__(param_decls: cabc.Sequence[str] | None, type: types.ParamType[t.Any] | t.Any | None, required: bool, default: t.Any | t.Callable[[], t.Any] | None, callback: t.Callable[[Context, Parameter, t.Any], t.Any] | None, nargs: int | None, multiple: bool, metavar: str | None, expose_value: bool, is_eager: bool, envvar: str | cabc.Sequence[str] | None, shell_complete: t.Callable[[Context, Parameter, str], list[CompletionItem] | list[str]] | None, deprecated: bool | str, help: str | None) -> None` `src/click/core.py:2406`
- `Parameter._hide_unset(value: t.Any) -> t.Any` `src/click/core.py:2491`
- `Parameter.to_info_dict() -> dict[str, t.Any]` `src/click/core.py:2498`
- `Parameter.__repr__() -> str` `src/click/core.py:2524`
- `Parameter._parse_decls(decls: cabc.Sequence[str], expose_value: bool) -> tuple[str, list[str], list[str]]` `src/click/core.py:2528`
- `Parameter._check_name_is_usable(name: str, decls: cabc.Sequence[str]) -> None` `src/click/core.py:2532`
- `Parameter.spec() -> str` `src/click/core.py:2570`
- `Parameter.human_readable_name() -> str` `src/click/core.py:2586`
- `Parameter.get_help_spec(ctx: Context) -> str` `src/click/core.py:2605`
- `Parameter.make_metavar(ctx: Context) -> str` `src/click/core.py:2620`
- `Parameter.get_default(ctx: Context, call: bool) -> t.Any | t.Callable[[], t.Any] | None` `src/click/core.py:2644`
- `Parameter.add_to_parser(parser: _OptionParser, ctx: Context) -> None` `src/click/core.py:2678`
- `Parameter.consume_value(ctx: Context, opts: cabc.Mapping[str, t.Any]) -> tuple[t.Any, ParameterSource]` `src/click/core.py:2680`
- `Parameter.type_cast_value(ctx: Context, value: t.Any) -> t.Any` `src/click/core.py:2728`
- `Parameter.value_is_missing(value: t.Any) -> bool` `src/click/core.py:2784`
- `Parameter.process_value(ctx: Context, value: t.Any) -> t.Any` `src/click/core.py:2802`
- `Parameter.resolve_envvar_value(ctx: Context) -> str | None` `src/click/core.py:2868`
- `Parameter.value_from_envvar(ctx: Context) -> str | cabc.Sequence[str] | None` `src/click/core.py:2913`
- `Parameter.handle_parse_result(ctx: Context, opts: cabc.Mapping[str, t.Any], args: list[str]) -> tuple[t.Any, list[str]]` `src/click/core.py:2929`
- `Parameter.get_help_record(ctx: Context) -> tuple[str, str] | None` `src/click/core.py:3017`
- `Parameter.get_usage_pieces(ctx: Context) -> list[str]` `src/click/core.py:3020`
- `Parameter.get_error_hint(ctx: Context | None) -> str` `src/click/core.py:3023`
- `Parameter.shell_complete(ctx: Context, incomplete: str) -> list[CompletionItem]` `src/click/core.py:3033`
- `Option.__init__(param_decls: cabc.Sequence[str] | None, show_default: bool | str | None, prompt: bool | str, confirmation_prompt: bool | str, prompt_required: bool, hide_input: bool, is_flag: bool | None, flag_value: t.Any, multiple: bool, count: bool, allow_from_autoenv: bool, type: types.ParamType[t.Any] | t.Any | None, help: str | None, hidden: bool, show_choices: bool, show_envvar: bool, deprecated: bool | str) -> None` `src/click/core.py:3149`
- `Option.is_bool_flag() -> bool` `src/click/core.py:3228`
- `Option.flag_activation_value() -> t.Any` `src/click/core.py:3237`
- `Option._infer_flag_kind(is_flag: bool | None, flag_value: t.Any) -> tuple[bool, bool]` `src/click/core.py:3249`
- `Option._pick_type(type_arg: t.Any, flag_value: t.Any, count: bool, is_flag: bool) -> types.ParamType[t.Any]` `src/click/core.py:3282`
- `Option._resolve_lazy_default(value: t.Any) -> t.Any` `src/click/core.py:3321`
- `Option._validate(prompt: bool | str, deprecated: bool | str) -> None` `src/click/core.py:3345`
- `Option.to_info_dict() -> dict[str, t.Any]` `src/click/core.py:3367`
- `Option.get_default(ctx: Context, call: bool) -> t.Any | t.Callable[[], t.Any] | None` `src/click/core.py:3389`
- `Option.get_error_hint(ctx: Context | None) -> str` `src/click/core.py:3423`
- `Option._check_name_is_normalized(name: str, decls: cabc.Sequence[str]) -> None` `src/click/core.py:3429`
- `Option._parse_decls(decls: cabc.Sequence[str], expose_value: bool) -> tuple[str, list[str], list[str]]` `src/click/core.py:3449`
- `Option.add_to_parser(parser: _OptionParser, ctx: Context) -> None` `src/click/core.py:3516`
- `Option.get_help_spec(ctx: Context) -> str` `src/click/core.py:3558`
- `Option.get_help_record(ctx: Context) -> tuple[str, str] | None` `src/click/core.py:3589`
- `Option.get_help_extra(ctx: Context) -> types.OptionHelpExtra` `src/click/core.py:3614`
- `Option.prompt_for_value(ctx: Context) -> t.Any` `src/click/core.py:3698`
- `Option.resolve_envvar_value(ctx: Context) -> str | None` `src/click/core.py:3748`
- `Option.value_from_envvar(ctx: Context) -> t.Any` `src/click/core.py:3772`
- `Option.consume_value(ctx: Context, opts: cabc.Mapping[str, Parameter]) -> tuple[t.Any, ParameterSource]` `src/click/core.py:3820`
- `Option.process_value(ctx: Context, value: t.Any) -> t.Any` `src/click/core.py:3876`
- `Argument.__init__(param_decls: cabc.Sequence[str], required: bool | None, help: str | None) -> None` `src/click/core.py:3909`
- `Argument.spec() -> str` `src/click/core.py:3932`
- `Argument.make_metavar(ctx: Context) -> str` `src/click/core.py:3944`
- `Argument._parse_decls(decls: cabc.Sequence[str], expose_value: bool) -> tuple[str, list[str], list[str]]` `src/click/core.py:3963`
- `Argument.get_usage_pieces(ctx: Context) -> list[str]` `src/click/core.py:3984`
- `Argument.get_help_spec(ctx: Context) -> str` `src/click/core.py:3987`
- `Argument.get_help_record(ctx: Context) -> tuple[str, str]` `src/click/core.py:3995`
- `Argument.get_error_hint(ctx: Context | None) -> str` `src/click/core.py:4008`
- `Argument.add_to_parser(parser: _OptionParser, ctx: Context) -> None` `src/click/core.py:4013`
- `__getattr__(name: str) -> object` `src/click/core.py:4017`

## Depends on
- [click._utils](/modules/click._utils.md) `src/click/core.py:25`
- [click.exceptions](/modules/click.exceptions.md) `src/click/core.py:27`
- [click.formatting](/modules/click.formatting.md) `src/click/core.py:35`
- [click.globals](/modules/click.globals.md) `src/click/core.py:37`
- [click.parser](/modules/click.parser.md) `src/click/core.py:39`
- [click.shell_completion](/modules/click.shell_completion.md) `src/click/core.py:54`
- [click.termui](/modules/click.termui.md) `src/click/core.py:41`
- [click.types](/modules/click.types.md) `src/click/core.py:24`
- [click.utils](/modules/click.utils.md) `src/click/core.py:44`

## Calls
- `_echo_aborted` calls [click.utils](/modules/click.utils.md) `echo` `src/click/core.py:105`
- `Argument.add_to_parser` calls [click.parser](/modules/click.parser.md) `_OptionParser.add_argument` `src/click/core.py:4014`
- `Argument.make_metavar` calls [click.types](/modules/click.types.md) `ParamType.get_metavar` `src/click/core.py:3947`
- `Command.format_arguments` calls [click.formatting](/modules/click.formatting.md) `HelpFormatter.section` `src/click/core.py:1347`
- `Command.format_arguments` calls [click.formatting](/modules/click.formatting.md) `HelpFormatter.write_dl` `src/click/core.py:1348`
- `Command.format_epilog` calls [click.formatting](/modules/click.formatting.md) `HelpFormatter.indentation` `src/click/core.py:1356`
- `Command.format_epilog` calls [click.formatting](/modules/click.formatting.md) `HelpFormatter.write_paragraph` `src/click/core.py:1354`
- `Command.format_epilog` calls [click.formatting](/modules/click.formatting.md) `HelpFormatter.write_text` `src/click/core.py:1357`
- `Command.format_help_text` calls [click.formatting](/modules/click.formatting.md) `HelpFormatter.indentation` `src/click/core.py:1322`
- `Command.format_help_text` calls [click.formatting](/modules/click.formatting.md) `HelpFormatter.write_paragraph` `src/click/core.py:1320`
- `Command.format_help_text` calls [click.formatting](/modules/click.formatting.md) `HelpFormatter.write_text` `src/click/core.py:1323`
- `Command.format_options` calls [click.formatting](/modules/click.formatting.md) `HelpFormatter.section` `src/click/core.py:1334`
- `Command.format_options` calls [click.formatting](/modules/click.formatting.md) `HelpFormatter.write_dl` `src/click/core.py:1335`
- `Command.format_usage` calls [click.formatting](/modules/click.formatting.md) `HelpFormatter.write_usage` `src/click/core.py:1194`
- `Command.get_help` calls [click.formatting](/modules/click.formatting.md) `HelpFormatter.getvalue` `src/click/core.py:1270`
- `Command.get_short_help_str` calls [click.utils](/modules/click.utils.md) `_make_default_short_help` `src/click/core.py:1279`
- `Command.get_usage` calls [click.formatting](/modules/click.formatting.md) `HelpFormatter.getvalue` `src/click/core.py:1130`
- `Command.invoke` calls [click.termui](/modules/click.termui.md) `style` `src/click/core.py:1443`
- `Command.invoke` calls [click.utils](/modules/click.utils.md) `echo` `src/click/core.py:1443`
- `Command.main` calls [click.utils](/modules/click.utils.md) `_detect_program_name` `src/click/core.py:1575`
- `Command.main` calls [click.utils](/modules/click.utils.md) `_expand_args` `src/click/core.py:1570`
- `Command.main` calls [click.utils](/modules/click.utils.md) `echo` `src/click/core.py:1623`
- `Command.parse_args` calls [click.parser](/modules/click.parser.md) `_OptionParser.parse_args` `src/click/core.py:1401`
- `Context.__enter__` calls [click.globals](/modules/click.globals.md) `push_context` `src/click/core.py:581`
- `Context.__exit__` calls [click.globals](/modules/click.globals.md) `pop_context` `src/click/core.py:594`
- `Group.format_commands` calls [click.formatting](/modules/click.formatting.md) `HelpFormatter.section` `src/click/core.py:2035`
- `Group.format_commands` calls [click.formatting](/modules/click.formatting.md) `HelpFormatter.write_dl` `src/click/core.py:2036`
- `Group.resolve_command` calls [click.parser](/modules/click.parser.md) `_split_opt` `src/click/core.py:2141`
- `Group.resolve_command` calls [click.utils](/modules/click.utils.md) `make_str` `src/click/core.py:2123`
- `Option._parse_decls` calls [click.parser](/modules/click.parser.md) `_split_opt` `src/click/core.py:3469`
- `Option._pick_type` calls [click.types](/modules/click.types.md) `convert_type` `src/click/core.py:3309`
- `Option.add_to_parser` calls [click.parser](/modules/click.parser.md) `_OptionParser.add_option` `src/click/core.py:3528`
- `Option.get_help_extra` calls [click.parser](/modules/click.parser.md) `_split_opt` `src/click/core.py:3670`
- `Option.get_help_spec` calls [click.formatting](/modules/click.formatting.md) `join_options` `src/click/core.py:3572`
- `Option.prompt_for_value` calls [click.termui](/modules/click.termui.md) `confirm` `src/click/core.py:3727`
- `Option.prompt_for_value` calls [click.termui](/modules/click.termui.md) `prompt` `src/click/core.py:3735`
- `Option.value_from_envvar` calls [click.types](/modules/click.types.md) `BoolParamType.str_to_bool` `src/click/core.py:3804`
- `Option.value_from_envvar` calls [click.types](/modules/click.types.md) `ParamType.split_envvar_value` `src/click/core.py:3812`
- `Parameter.__init__` calls [click.types](/modules/click.types.md) `convert_type` `src/click/core.py:2439`
- `Parameter.consume_value` calls [click.types](/modules/click.types.md) `ParamType.split_envvar_value` `src/click/core.py:2718`
- `Parameter.handle_parse_result` calls [click.termui](/modules/click.termui.md) `style` `src/click/core.py:2973`
- `Parameter.handle_parse_result` calls [click.utils](/modules/click.utils.md) `echo` `src/click/core.py:2973`
- `Parameter.make_metavar` calls [click.types](/modules/click.types.md) `ParamType.get_metavar` `src/click/core.py:2624`
- `Parameter.shell_complete` calls [click.types](/modules/click.types.md) `ParamType.shell_complete` `src/click/core.py:3054`
- `Parameter.spec` calls [click.parser](/modules/click.parser.md) `_split_opt` `src/click/core.py:2583`
- `Parameter.to_info_dict` calls [click.types](/modules/click.types.md) `ParamType.to_info_dict` `src/click/core.py:2515`
- `Parameter.value_from_envvar` calls [click.types](/modules/click.types.md) `ParamType.split_envvar_value` `src/click/core.py:2925`
