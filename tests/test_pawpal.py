import datetime

from pawpal_system import Owner, Pet, Scheduler, Task
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

def test_sort_by_time_returns_chronological_order():
    scheduler = Scheduler()

    task1 = Task("Walk")
    task2 = Task("Feed")

    today = datetime.datetime.now()

    scheduler.assign_task_time(task1, today.replace(hour=10, minute=0))
    scheduler.assign_task_time(task2, today.replace(hour=8, minute=0))

    sorted_tasks = scheduler.sort_by_time([task1, task2])

    assert sorted_tasks[0].title == "Feed"
    assert sorted_tasks[1].title == "Walk"


def test_daily_recurring_task_creates_new_task():
    scheduler = Scheduler()

    today = datetime.datetime.now()

    task = Task(
        "Breakfast",
        duration_minutes=15,
        priority=1,
        scheduled_time=today,
        frequency="daily",
    )

    task.mark_complete()

    next_task = scheduler.create_next_recurring_task(task)

    assert next_task is not None
    assert next_task.completed is False
    assert next_task.scheduled_time.date() == (
        today + datetime.timedelta(days=1)
    ).date()


def test_detect_conflicts_returns_warning():
    scheduler = Scheduler()

    owner = Owner("Bhavika", "bhavika@example.com")
    pet = Pet("Biscuit", "Dog", 3)

    today = datetime.datetime.now()

    task1 = Task("Walk")
    task2 = Task("Feed")

    scheduler.assign_task_time(task1, today.replace(hour=9, minute=0))
    scheduler.assign_task_time(task2, today.replace(hour=9, minute=0))

    pet.add_task(task1)
    pet.add_task(task2)
    owner.add_pet(pet)

    conflicts = scheduler.detect_conflicts(owner)

    assert len(conflicts) == 1