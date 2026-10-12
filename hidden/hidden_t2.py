import click


def test_eager_first_then_declaration_order():
    @click.command()
    @click.option("--a")
    @click.option("--b", is_eager=True)
    @click.option("--c")
    def cli(a, b, c):
        pass

    ctx = click.Context(cli)
    names = [n for n in cli.params_by_priority(ctx) if not n.startswith("_")]
    assert names == ["b", "a", "c"]


def test_returns_names_not_objects():
    @click.command()
    @click.argument("src")
    @click.option("--v")
    def cli(src, v):
        pass

    names = cli.params_by_priority(click.Context(cli))
    assert all(isinstance(n, str) for n in names) and {"src", "v"} <= set(names)
