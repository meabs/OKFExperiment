---
type: Code Module
title: "click.types"
description: "click.types: ParamTypeInfoDict, ParamType, CompositeParamType, FuncParamTypeInfoDict"
resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/types.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/src/click/types.py"
    sha256: "30a39185da37bbd98ef47153f7bfd310b04eac44bd9b9b2fe15998406337757e"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

# click.types

Source: `src/click/types.py`

## Types
- `ParamTypeInfoDict` (class) extends `typing.TypedDict` `src/click/types.py:60`
- `ParamType` (class) extends `abc.ABC`, `typing.Generic[_ValueT_co, _InputT_contra]` `src/click/types.py:65`
- `CompositeParamType` (class) extends `ParamType[_ValueT_co]` `src/click/types.py:242`
- `FuncParamTypeInfoDict` (class) extends `click.types.ParamTypeInfoDict` `src/click/types.py:260`
- `FuncParamType` (class) extends `ParamType[_ValueT_co]`, `typing.Generic[_ValueT_contra, _ValueT_co]` `src/click/types.py:264`
- `UnprocessedParamType` (class) extends `ParamType[t.Any]` `src/click/types.py:292`
- `StringParamType` (class) extends `ParamType[str]` `src/click/types.py:304`
- `ChoiceInfoDict` (class) extends `click.types.ParamTypeInfoDict` `src/click/types.py:337`
- `Choice` (class) extends `ParamType[_ValueT_co]`, `typing.Generic[_ValueT_co]` `src/click/types.py:342`
- `DateTimeInfoDict` (class) extends `click.types.ParamTypeInfoDict` `src/click/types.py:518`
- `DateTime` (class) extends `ParamType[datetime]` `src/click/types.py:522`
- `_NumberParamTypeBase` (class) extends `ParamType[_ValueT_co]`, `typing.Generic[_ValueT_contra, _ValueT_co]` `src/click/types.py:593`
- `NumberRangeInfoDict` (class) extends `click.types.ParamTypeInfoDict` `src/click/types.py:624`
- `_NumberRangeBase` (class) extends `_NumberParamTypeBase[_ValueT_contra, _FloatValueT_co]`, `typing.Generic[_ValueT_contra, _FloatValueT_co]` `src/click/types.py:632`
- `IntParamType` (class) extends `_NumberParamTypeBase[t.SupportsInt | t.SupportsIndex, int]` `src/click/types.py:736`
- `IntRange` (class) extends `_NumberRangeBase[int, int]`, `click.types.IntParamType` `src/click/types.py:744`
- `FloatParamType` (class) extends `_NumberParamTypeBase[t.SupportsFloat | t.SupportsIndex, float]` `src/click/types.py:768`
- `FloatRange` (class) extends `_NumberRangeBase[float, float]`, `click.types.FloatParamType` `src/click/types.py:776`
- `BoolParamType` (class) extends `ParamType[bool]` `src/click/types.py:819`
- `UUIDParameterType` (class) extends `ParamType[uuid.UUID]` `src/click/types.py:888`
- `FileInfoDict` (class) extends `click.types.ParamTypeInfoDict` `src/click/types.py:910`
- `File` (class) extends `ParamType[t.IO[t.Any]]` `src/click/types.py:915`
- `PathInfoDict` (class) extends `click.types.ParamTypeInfoDict` `src/click/types.py:1050`
- `Path` (class) extends `ParamType[_PathT_co, str | os.PathLike[str]]`, `typing.Generic[_PathT_co]` `src/click/types.py:1059`
- `TupleInfoDict` (class) extends `click.types.ParamTypeInfoDict` `src/click/types.py:1254`
- `Tuple` (class) extends `CompositeParamType[tuple[t.Any, ...]]` `src/click/types.py:1258`
- `OptionHelpExtra` (class) extends `typing.TypedDict` `src/click/types.py:1433`

## Functions and methods
- `ParamType.to_info_dict() -> ParamTypeInfoDict` `src/click/types.py:122`
- `ParamType.__call__(value: _InputT_contra | None, param: Parameter | None, ctx: Context | None) -> _ValueT_co | None` `src/click/types.py:159`
- `ParamType.get_metavar(param: Parameter, ctx: Context) -> str | None` `src/click/types.py:169`
- `ParamType.get_missing_message(param: Parameter, ctx: Context | None) -> str | None` `src/click/types.py:172`
- `ParamType.convert(value: _InputT_contra, param: Parameter | None, ctx: Context | None) -> _ValueT_co` `src/click/types.py:179`
- `ParamType.split_envvar_value(rv: str) -> cabc.Sequence[str]` `src/click/types.py:205`
- `ParamType.fail(message: str, param: Parameter | None, ctx: Context | None) -> t.NoReturn` `src/click/types.py:215`
- `ParamType.shell_complete(ctx: Context, param: Parameter, incomplete: str) -> list[CompletionItem]` `src/click/types.py:224`
- `CompositeParamType.arity() -> int` `src/click/types.py:247`
- `FuncParamType.__init__(func: t.Callable[[_ValueT_contra], _ValueT_co]) -> None` `src/click/types.py:268`
- `FuncParamType.to_info_dict() -> FuncParamTypeInfoDict[_ValueT_contra, _ValueT_co]` `src/click/types.py:272`
- `FuncParamType.convert(value: _ValueT_contra, param: Parameter | None, ctx: Context | None) -> _ValueT_co` `src/click/types.py:275`
- `UnprocessedParamType.convert(value: _ValueT, param: Parameter | None, ctx: Context | None) -> _ValueT` `src/click/types.py:295`
- `UnprocessedParamType.__repr__() -> str` `src/click/types.py:300`
- `StringParamType.convert(value: t.Any, param: Parameter | None, ctx: Context | None) -> str` `src/click/types.py:307`
- `StringParamType.__repr__() -> str` `src/click/types.py:325`
- `Choice.__init__(choices: cabc.Iterable[_ValueT_co], case_sensitive: bool) -> None` `src/click/types.py:375`
- `Choice.to_info_dict() -> ChoiceInfoDict[_ValueT_co]` `src/click/types.py:381`
- `Choice._normalized_mapping(ctx: Context | None) -> cabc.Mapping[_ValueT_co, str]` `src/click/types.py:388`
- `Choice.normalize_choice(choice: object, ctx: Context | None) -> str` `src/click/types.py:406`
- `Choice.get_metavar(param: Parameter, ctx: Context) -> str | None` `src/click/types.py:426`
- `Choice.get_missing_message(param: Parameter, ctx: Context | None) -> str` `src/click/types.py:444`
- `Choice.convert(value: t.Any, param: Parameter | None, ctx: Context | None) -> _ValueT_co` `src/click/types.py:454`
- `Choice.get_invalid_choice_message(value: t.Any, ctx: Context | None) -> str` `src/click/types.py:478`
- `Choice.__repr__() -> str` `src/click/types.py:492`
- `Choice.shell_complete(ctx: Context, param: Parameter, incomplete: str) -> list[CompletionItem]` `src/click/types.py:495`
- `DateTime.__init__(formats: cabc.Sequence[str] | None)` `src/click/types.py:547`
- `DateTime.to_info_dict() -> DateTimeInfoDict` `src/click/types.py:554`
- `DateTime.get_metavar(param: Parameter, ctx: Context) -> str` `src/click/types.py:557`
- `DateTime._try_to_convert_date(value: t.Any, format: str) -> datetime | None` `src/click/types.py:560`
- `DateTime.convert(value: t.Any, param: Parameter | None, ctx: Context | None) -> datetime` `src/click/types.py:566`
- `DateTime.__repr__() -> str` `src/click/types.py:589`
- `_NumberParamTypeBase.convert(value: _ValueT_contra, param: Parameter | None, ctx: Context | None) -> _ValueT_co` `src/click/types.py:598`
- `_NumberRangeBase.__init__(min: _FloatValueT_co | None, max: _FloatValueT_co | None, min_open: bool, max_open: bool, clamp: bool) -> None` `src/click/types.py:642`
- `_NumberRangeBase.to_info_dict() -> NumberRangeInfoDict[_FloatValueT_co]` `src/click/types.py:656`
- `_NumberRangeBase.convert(value: _ValueT_contra, param: Parameter | None, ctx: Context | None) -> _FloatValueT_co` `src/click/types.py:666`
- `_NumberRangeBase._clamp(bound: _FloatValueT, dir: t.Literal[1, -1], open: bool) -> _FloatValueT` `src/click/types.py:700`
- `_NumberRangeBase._describe_range() -> str` `src/click/types.py:717`
- `_NumberRangeBase.__repr__() -> str` `src/click/types.py:731`
- `IntParamType.__repr__() -> str` `src/click/types.py:740`
- `IntRange._clamp(bound: int, dir: t.Literal[1, -1], open: bool) -> int` `src/click/types.py:761`
- `FloatParamType.__repr__() -> str` `src/click/types.py:772`
- `FloatRange.__init__(min: float | None, max: float | None, min_open: bool, max_open: bool, clamp: bool) -> None` `src/click/types.py:794`
- `FloatRange._clamp(bound: float, dir: t.Literal[1, -1], open: bool) -> float` `src/click/types.py:809`
- `BoolParamType.str_to_bool(value: str | bool) -> bool | None` `src/click/types.py:856`
- `BoolParamType.convert(value: t.Any, param: Parameter | None, ctx: Context | None) -> bool` `src/click/types.py:870`
- `BoolParamType.__repr__() -> str` `src/click/types.py:884`
- `UUIDParameterType.convert(value: uuid.UUID | str, param: Parameter | None, ctx: Context | None) -> uuid.UUID` `src/click/types.py:891`
- `UUIDParameterType.__repr__() -> str` `src/click/types.py:906`
- `File.__init__(mode: str, encoding: str | None, errors: str | None, lazy: bool | None, atomic: bool) -> None` `src/click/types.py:954`
- `File.to_info_dict() -> FileInfoDict` `src/click/types.py:968`
- `File.resolve_lazy_flag(value: str | os.PathLike[str]) -> bool` `src/click/types.py:975`
- `File.convert(value: str | os.PathLike[str] | t.IO[t.Any], param: Parameter | None, ctx: Context | None) -> t.IO[t.Any]` `src/click/types.py:984`
- `File.shell_complete(ctx: Context, param: Parameter, incomplete: str) -> list[CompletionItem]` `src/click/types.py:1029`
- `_is_file_like(value: t.Any) -> te.TypeIs[t.IO[t.Any]]` `src/click/types.py:1046`
- `Path.__init__(exists: bool, file_okay: bool, dir_okay: bool, writable: bool, readable: bool, resolve_path: bool, allow_dash: bool, path_type: type[_PathT_co] | None, executable: bool) -> None` `src/click/types.py:1107`
- `Path.to_info_dict() -> PathInfoDict` `src/click/types.py:1136`
- `Path.coerce_path_result(value: str | os.PathLike[str]) -> _PathT_co` `src/click/types.py:1147`
- `Path.convert(value: str | os.PathLike[str], param: Parameter | None, ctx: Context | None) -> _PathT_co` `src/click/types.py:1161`
- `Path.shell_complete(ctx: Context, param: Parameter, incomplete: str) -> list[CompletionItem]` `src/click/types.py:1235`
- `Tuple.__init__(types: cabc.Sequence[type[t.Any] | ParamType[t.Any]]) -> None` `src/click/types.py:1272`
- `Tuple.to_info_dict() -> TupleInfoDict` `src/click/types.py:1275`
- `Tuple.name() -> str` `src/click/types.py:1282`
- `Tuple.arity() -> int` `src/click/types.py:1286`
- `Tuple.convert(value: t.Any, param: Parameter | None, ctx: Context | None) -> tuple[t.Any, ...]` `src/click/types.py:1289`
- `_guess_type(ty: type[t.Any] | ParamType[t.Any] | None, default: t.Any | None) -> type[t.Any] | tuple[type[t.Any], ...] | ParamType[t.Any] | None` `src/click/types.py:1311`
- `convert_type(ty: t.Any | None, default: t.Any | None) -> ParamType[t.Any]` `src/click/types.py:1356`

## Depends on
- [click._compat](/modules/click._compat.md) `src/click/types.py:15`
- [click.core](/modules/click.core.md) `src/click/types.py:25`
- [click.exceptions](/modules/click.exceptions.md) `src/click/types.py:17`
- [click.shell_completion](/modules/click.shell_completion.md) `src/click/types.py:27`
- [click.utils](/modules/click.utils.md) `src/click/types.py:18`

## Calls
- `File.convert` calls [click._compat](/modules/click._compat.md) `open_stream` `src/click/types.py:1006`
- `File.convert` calls [click.core](/modules/click.core.md) `Context.call_on_close` `src/click/types.py:1002`
- `File.convert` calls [click.utils](/modules/click.utils.md) `_safecall` `src/click/types.py:1017`
- `File.convert` calls [click.utils](/modules/click.utils.md) `format_filename` `src/click/types.py:1024`
- `Path.convert` calls [click.utils](/modules/click.utils.md) `format_filename` `src/click/types.py:1183`
- `StringParamType.convert` calls [click._compat](/modules/click._compat.md) `_get_argv_encoding` `src/click/types.py:311`

## Tests
- `test_types`
