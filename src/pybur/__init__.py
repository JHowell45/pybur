from io import StringIO
from pathlib import Path
from typing import Annotated

import typer
from mako.runtime import Context
from mako.template import Template

cli = typer.Typer(no_args_is_help=True)


@cli.command(
    # no_args_is_help=True,
    help="Commands for building at the scaffolding for a new project type.",
)
def build(
    rootpath: Annotated[
        Path, typer.Argument(help="the root pathto create the directory within.")
    ] = Path("."),
) -> None:
    print("Building...")
    print(rootpath.resolve())
    template = Template("Hello, ${name}!")
    buf = StringIO()
    ctx = Context(buf, name="Jacob")
    template.render_context(ctx)
    print(buf.getvalue())


@cli.command()
def run() -> None:
    print("Running....")
