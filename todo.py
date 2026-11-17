"""A small to-do app used to test DAM. Nothing here is real."""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

DB = Path("todo.json")
DUE_FORMAT = "%Y-%m-%d %H:%M"


def load(path=DB):
    if not path.exists():
        return []
    return json.loads(path.read_text())


def save(items, path=DB):
    path.write_text(json.dumps(items, indent=2) + "\n")


def add(items, text, due=None):
    item = {"text": text, "done": False}
    if due is not None:
        item["due"] = datetime.strptime(due, DUE_FORMAT).isoformat()
    items.append(item)
    return items


def done(items, number):
    """Mark item `number` (as `list` shows it, counted from 1) as done."""
    if number < 1 or number > len(items):
        raise IndexError(f"no item {number}")
    items[number]["done"] = True
    return items


def render(items):
    now = datetime.now()
    lines = []
    for number, item in enumerate(items, start=1):
        mark = "x" if item["done"] else " "
        line = f"{number}. [{mark}] {item['text']}"
        if "due" in item:
            due = datetime.fromisoformat(item["due"])
            line += f" (due {due.strftime(DUE_FORMAT)})"
            if not item["done"] and due < now:
                line += " OVERDUE"
        lines.append(line)
    return "\n".join(lines) if lines else "Nothing to do."


def main(argv=None):
    parser = argparse.ArgumentParser(prog="todo", description="A tiny to-do list.")
    sub = parser.add_subparsers(dest="command", required=True)
    add_cmd = sub.add_parser("add", help="add an item")
    add_cmd.add_argument("text")
    add_cmd.add_argument("--due", help='when it is due, as "YYYY-MM-DD HH:MM"')
    sub.add_parser("list", help="list the items")
    done_cmd = sub.add_parser("done", help="mark an item done")
    done_cmd.add_argument("number", type=int)
    args = parser.parse_args(argv)

    items = load()
    if args.command == "add":
        save(add(items, args.text, args.due))
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
