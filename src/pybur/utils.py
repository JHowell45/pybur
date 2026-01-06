from pathlib import Path

from mako.template import Template


def get_template(filepath: Path) -> Template:
    return Template(filename=filepath.resolve())
