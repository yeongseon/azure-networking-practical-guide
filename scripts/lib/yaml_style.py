from __future__ import annotations

from io import StringIO

from ruamel.yaml import YAML

__all__ = ["build_yaml", "dump_frontmatter", "CANONICAL_INDENT"]

CANONICAL_INDENT: dict[str, int] = {
    "mapping": 2,
    "sequence": 4,
    "offset": 2,
}


def build_yaml() -> YAML:
    yaml = YAML(typ="rt")
    yaml.indent(**CANONICAL_INDENT)
    yaml.preserve_quotes = True
    yaml.width = 4096
    yaml.explicit_end = False
    return yaml


def dump_frontmatter(data: object, *, trailing_newline: bool = True) -> str:
    yaml = build_yaml()
    buffer = StringIO()
    yaml.dump(data, buffer)
    text = buffer.getvalue()
    if trailing_newline and not text.endswith("\n"):
        text += "\n"
    return text
