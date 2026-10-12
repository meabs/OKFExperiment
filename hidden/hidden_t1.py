import click
from click.testing import CliRunner


def _ctx_of(args):
    seen = {}

    @click.command()
    @click.option("--name", default="x")
    @click.option("--n", default=1)
    @click.pass_context
    def cli(ctx, name, n):
        seen["ctx"] = ctx

    CliRunner().invoke(cli, args)
    return seen["ctx"]


def test_names_the_source_in_lowercase():
    ctx = _ctx_of(["--name", "a"])
    assert ctx.get_parameter_source_name("name") == "commandline"
    assert ctx.get_parameter_source_name("n") == "default"


def test_unknown_parameter_is_none():
    assert _ctx_of([]).get_parameter_source_name("nope") is None
