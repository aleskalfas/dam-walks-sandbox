"""A small to-do app used to test DAM. Nothing here is real."""

import argparse
import json
import sys
from pathlib import Path

DB = Path("todo.json")


def load(path=DB):
    if not path.exists():
        return []
    return json.loads(path.read_text())


def save(items, path=DB):
    path.write_text(json.dumps(items, indent=2) + "\n")


def add(items, text):
    items.append({"text": text, "done": False})
    return items


def done(items, number):
    """Mark item `number` (as `list` shows it, counted from 1) as done."""
    if number < 1 or number > len(items):
        raise IndexError(f"no item {number}")
    items[number]["done"] = True
    return items


def render(items):
    lines = []
    for number, item in enumerate(items, start=1):
        mark = "x" if item["done"] else " "
        lines.append(f"{number}. [{mark}] {item['text']}")
    return "\n".join(lines) if lines else "Nothing to do."


def main(argv=None):
    parser = argparse.ArgumentParser(prog="todo", description="A tiny to-do list.")
    sub = parser.add_subparsers(dest="command", required=True)
    add_cmd = sub.add_parser("add", help="add an item")
    add_cmd.add_argument("text")
    sub.add_parser("list", help="list the items")
    done_cmd = sub.add_parser("done", help="mark an item done")
    done_cmd.add_argument("number", type=int)
    args = parser.parse_args(argv)

    items = load()
    if args.command == "add":
        save(add(items, args.text))
    elif args.command == "done":
        try:
            save(done(items, args.number))
        except IndexError as error:
            print(f"todo: {error}", file=sys.stderr)
            return 1
    print(render(items))
    return 0


if __name__ == "__main__":
    sys.exit(main())
