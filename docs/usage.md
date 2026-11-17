# Usage

The app needs Python 3.10 or newer and nothing else. It keeps the list in `todo.json` in the current directory.

```sh
python todo.py add "Buy milk"
python todo.py list
python todo.py done 1
```

An item can have a due date. `list` shows it, and marks an open item that is past it as `OVERDUE`:

```sh
python todo.py add "Send the invoice" --due "2026-12-01 17:00"
```

Run the tests with pytest:

```sh
python -m pip install pytest
python -m pytest
```
