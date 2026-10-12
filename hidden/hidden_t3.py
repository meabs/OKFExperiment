import click


def test_is_positional():
    assert click.Argument(["x"]).is_positional is True
    assert click.Option(["--x"]).is_positional is False
