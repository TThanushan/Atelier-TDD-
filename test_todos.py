from todos import TaskManager, Action


def test_can_create_an_action():
    action = Action("add", "first task")
    assert action.name == "add"
    assert action.description == "first task"


def test_can_create_a_task_manager():
    task_manager = TaskManager()


def test_task_manager_starts_with_no_tasks():
    task_manager = TaskManager()

    assert task_manager.tasks == []


def test_parse_delete():
    # Adding the task.
    command = "+ first task"
    task_manager = TaskManager()
    action = task_manager.parse(command)

    task_manager.parse_logic(action)
    task_added = task_manager.tasks[0]

    # Remove the task.
    command = "- first task"
    action = task_manager.parse(command)
    task_manager.parse_logic(action)

    # Check if task has been deleted.
    for _task in task_manager.tasks:
        if _task.id == task_added.id:
            AssertionError
