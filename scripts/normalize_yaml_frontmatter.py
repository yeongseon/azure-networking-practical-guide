#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.yaml_style import build_yaml, dump_frontmatter  # noqa: E402

FRONTMATTER = re.compile(r"^---[ \t]*\n(.*?)\n---[ \t]*\n", re.DOTALL)


def normalize_text(text: str) -> tuple[str, bool]:
    match = FRONTMATTER.match(text)
    if not match:
        return text, False

    yaml_text = match.group(1)
    body = text[match.end() :]

    data = build_yaml().load(yaml_text)
    if data is None:
        return text, False

    new_yaml = dump_frontmatter(data)
    new_text = f"---\n{new_yaml}---\n" + body
    return new_text, new_text != text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docs-dir", type=Path, default=Path("docs"))
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--apply", action="store_true")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    docs_dir = (project_root / args.docs_dir).resolve()
    if not docs_dir.exists():
        print(f"Error: docs directory not found: {docs_dir}", file=sys.stderr)
        return 1

    changed: list[Path] = []
    errors: list[tuple[Path, str]] = []
    scanned = 0

    for md_file in sorted(docs_dir.rglob("*.md")):
        scanned += 1
        text = md_file.read_text(encoding="utf-8")
        try:
            new_text, did_change = normalize_text(text)
        except Exception as exc:
            errors.append((md_file, str(exc)))
            if not args.quiet:
                print(f"  ERROR  {md_file.relative_to(project_root)}  [{exc}]")
            continue

        if not did_change:
            continue

        changed.append(md_file)
        rel = md_file.relative_to(project_root)
        if args.apply:
            md_file.write_text(new_text, encoding="utf-8")
            if not args.quiet:
                print(f"  FIXED  {rel}")
        elif not args.quiet:
            print(f"  DRIFT  {rel}")

    print("\nSummary:")
    print(f"  Files scanned: {scanned}")
    print(f"  Files with style drift: {len(changed)}")
    print(f"  Parse errors: {len(errors)}")

    if errors:
        return 1
    if changed and not args.apply:
        print(
            "\nDrift detected. Run `python3 scripts/normalize_yaml_frontmatter.py --apply` to fix."
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
