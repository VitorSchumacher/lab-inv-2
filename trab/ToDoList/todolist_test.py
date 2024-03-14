from todolist import TodoList

def test_add_task():
    list = TodoList()
    list.add_task("Salve professor FElipe")
    assert "Salve professor FElipe" in list.tasks

def test_remove_task():
    list = TodoList()
    list.add_task("Salve professor FElipe")
    list.remove_task("Salve professor FElipe")
    assert "Salve professor FElipe" not in list.tasks

def test_clear_tasks():
    list = TodoList()
    list.add_task("Salve professor FElipe")
    list.add_task("so pra apagar esse")
    list.clear_tasks()
    assert len(list.tasks) == 0

def test_show_tasks(capsys):
    list = TodoList()
    list.add_task("Salve professor FElipe")
    list.show_tasks()
    captured = capsys.readouterr()
    assert "Salve professor FElipe" in captured.out