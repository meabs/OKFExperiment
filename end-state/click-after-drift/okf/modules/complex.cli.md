---
type: Code Module
title: "complex.cli"
description: "complex.cli: Environment, ComplexCLI"
resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/examples/complex/complex/cli.py"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2026-10-04T15:19:53-07:00"
sources:
  - resource: "https://github.com/pallets/click/blob/2247b35ea1c47c727d7a06e51fa280e12a863ff6/examples/complex/complex/cli.py"
    sha256: "2042ffdb1e77f0f937036f3f0a33c67bacbad90477873d7576cc297674a55de7"
    last_modified: "2026-10-04T15:19:53-07:00"
status: stable
---

# complex.cli

Source: `examples/complex/complex/cli.py`

## Types
- `Environment` (class) `examples/complex/complex/cli.py:10`
- `ComplexCLI` (class) extends `click.core.Group` `examples/complex/complex/cli.py:31`

## Functions and methods
- `Environment.__init__()` `examples/complex/complex/cli.py:11`
- `Environment.log(msg)` `examples/complex/complex/cli.py:15`
- `Environment.vlog(msg)` `examples/complex/complex/cli.py:21`
- `ComplexCLI.list_commands(ctx)` `examples/complex/complex/cli.py:32`
- `ComplexCLI.get_command(ctx, name)` `examples/complex/complex/cli.py:40`
- `cli(ctx, verbose, home)` `examples/complex/complex/cli.py:56`

## Depends on
- [click](/modules/click.md) `examples/complex/complex/cli.py:4`

## Calls
- `cli` calls [click.decorators](/modules/click.decorators.md) `command` `examples/complex/complex/cli.py:48`
- `cli` calls [click.decorators](/modules/click.decorators.md) `option` `examples/complex/complex/cli.py:49`
- `Environment.log` calls [click.utils](/modules/click.utils.md) `echo` `examples/complex/complex/cli.py:19`
