import json

import todo


def test_add_appends_an_open_item():
    items = todo.add([], "Buy milk")
    assert items == [{"text": "Buy milk", "done": False}]


def test_add_keeps_the_order():
    items = todo.add(todo.add([], "First"), "Second")
    assert [item["text"] for item in items] == ["First", "Second"]


def test_render_numbers_items_from_one():
    items = todo.add(todo.add([], "First"), "Second")
    assert todo.render(items) == "1. [ ] First\n2. [ ] Second"


def test_render_an_empty_list():
    assert todo.render([]) == "Nothing to do."


def test_save_and_load_round_trip(tmp_path):
    path = tmp_path / "todo.json"
    todo.save([{"text": "Buy milk", "done": True}], path)
    assert todo.load(path) == [{"text": "Buy milk", "done": True}]


def test_load_without_a_file(tmp_path):
    assert todo.load(tmp_path / "missing.json") == []


def test_main_add_then_list(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    assert todo.main(["add", "Buy milk"]) == 0
    assert todo.main(["list"]) == 0
    assert capsys.readouterr().out.splitlines()[-1] == "1. [ ] Buy milk"
    assert json.loads((tmp_path / "todo.json").read_text())[0]["text"] == "Buy milk"
