import typer

app = typer.Typer(no_args_is_help=True)


@app.command()
def build() -> None:
    print("Building...")


@app.command()
def run() -> None:
    print("Running....")


def main() -> None:
    app()
