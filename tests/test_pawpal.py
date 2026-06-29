from pawpal_system import Pet, Task


def test_mark_complete_changes_status():
    task = Task("Walk Dog")

    task.mark_complete()

    assert task.completed is True


def test_add_task_increases_task_count():
    pet = Pet("Biscuit", "Dog", 3)

    initial_count = len(pet.tasks)

    task = Task("Morning Walk")
    pet.add_task(task)

    assert len(pet.tasks) == initial_count + 1