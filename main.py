from pawpal_system import Owner, Pet, Task, Scheduler


owner = Owner("Bhavika", "bhavika@example.com")

dog = Pet("Biscuit", "Dog", 3)
cat = Pet("Mochi", "Cat", 2)

walk = Task("Morning Walk", "Take Biscuit for a walk", 30, 3)
feeding = Task("Breakfast", "Feed both pets", 15, 5)
medicine = Task("Medication", "Give Mochi her medicine", 10, 4)

dog.add_task(walk)
dog.add_task(feeding)
cat.add_task(medicine)

owner.add_pet(dog)
owner.add_pet(cat)

scheduler = Scheduler()
today_schedule = scheduler.generate_daily_schedule(owner, 60)

print("Today's Schedule")
print("----------------")

for task in today_schedule:
    print(f"- {task.title}: {task.duration_minutes} min, priority {task.priority}")