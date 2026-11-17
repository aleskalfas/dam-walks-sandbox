# Usage

The app needs Python 3.10 or newer and nothing else. It keeps the list in `todo.json` in the current directory.

```sh
python todo.py add "Buy milk"
python todo.py list
python todo.py done 1
```

Run the tests with pytest:

```sh
python -m pip install pytest
python -m pytest
```
