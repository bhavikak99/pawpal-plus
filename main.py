import datetime

from pawpal_system import Owner, Pet, Scheduler, Task

PRIORITY_LABELS = {
    1: "High",
    2: "Medium",
    3: "Low",
}


def format_task_title(title: str) -> str:
    lower_title = title.lower()

    if "walk" in lower_title:
        return f"🐕 {title}"
    if "feed" in lower_title or "breakfast" in lower_title or "dinner" in lower_title:
        return f"🍽️ {title}"
    if "medicine" in lower_title or "medication" in lower_title or "pill" in lower_title:
        return f"💊 {title}"
    if "groom" in lower_title or "bath" in lower_title:
        return f"🛁 {title}"
    if "vet" in lower_title or "vaccine" in lower_title or "doctor" in lower_title:
        return f"🏥 {title}"

    return f"🐾 {title}"


def format_status(completed: bool) -> str:
    return "✅ Complete" if completed else "⏳ Pending"

def print_tasks(title, tasks):
    print(f"\n{title}")
    print("-" * len(title))

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        time_text = task.scheduled_time.strftime("%I:%M %p") if task.scheduled_time else "No time"
        status = format_status(task.completed)
        priority = PRIORITY_LABELS.get(task.priority, "Unknown")
        task_title = format_task_title(task.title)

        print(
            f"- {time_text} | {task_title} | "
            f"{task.duration_minutes} min | Priority: {priority} | {status}"
        )

owner = Owner("Bhavika", "bhavika@example.com")

dog = Pet("Biscuit", "Dog", 3)
cat = Pet("Mochi", "Cat", 2)

walk = Task("Morning Walk", "Take Biscuit for a walk", 30, 3)
feeding = Task("Breakfast", "Feed Biscuit", 15, 1, frequency="daily")
medicine = Task("Medication", "Give Mochi medicine", 10, 2)

dog.add_task(walk)
dog.add_task(feeding)
cat.add_task(medicine)

owner.add_pet(dog)
owner.add_pet(cat)

scheduler = Scheduler()

today = datetime.datetime.now()
scheduler.assign_task_time(walk, today.replace(hour=9, minute=0, second=0, microsecond=0))
scheduler.assign_task_time(feeding, today.replace(hour=7, minute=30, second=0, microsecond=0))
scheduler.assign_task_time(medicine, today.replace(hour=9, minute=0, second=0, microsecond=0))

medicine.mark_complete()

feeding.mark_complete()
next_feeding = scheduler.create_next_recurring_task(feeding)

if next_feeding:
    dog.add_task(next_feeding)

all_tasks = scheduler.get_all_tasks(owner)
completed_tasks = scheduler.filter_tasks_by_status(all_tasks, True)
incomplete_tasks = scheduler.filter_tasks_by_status(all_tasks, False)
biscuit_tasks = scheduler.filter_tasks_by_pet(owner, "Biscuit")
tasks_by_time = scheduler.sort_by_time(all_tasks)
today_schedule = scheduler.generate_daily_schedule(owner, 1440)

next_slot = scheduler.find_next_available_slot(
    owner,
    today.replace(hour=9, minute=0, second=0, microsecond=0),
)

print("\nNext Available Slot")
print("-------------------")
print(next_slot.strftime("%I:%M %p"))

print_tasks("All Tasks", all_tasks)
print_tasks("Completed Tasks", completed_tasks)
print_tasks("Incomplete Tasks", incomplete_tasks)
print_tasks("Biscuit's Tasks", biscuit_tasks)
print_tasks("Tasks Sorted by Time", tasks_by_time)

conflicts = scheduler.detect_conflicts(owner)

print("\nConflict Warnings")
print("-----------------")
if conflicts:
    for warning in conflicts:
        print(f"⚠️ {warning}")
else:
    print("No conflicts found.")
    
print_tasks("Today's Schedule", today_schedule)

scheduler.save_to_json(owner, "data.json")
loaded_owner = scheduler.load_from_json("data.json")

print("\nPersistence Check")
print("-----------------")
print(f"Loaded owner: {loaded_owner.name}")
print(f"Loaded pets: {len(loaded_owner.get_pets())}")

