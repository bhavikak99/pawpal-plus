# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

* Track pet care tasks (walks, feeding, medication, enrichment, grooming, etc.)
* Consider constraints (time available, priority, owner preferences)
* Produce a daily plan and explain why it chose that plan.

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

---

## What you will build

Your final app should:

* Let a user enter basic owner and pet information.
* Let a user add and manage pet care tasks.
* Generate a daily schedule based on task priority and available time.
* Display the schedule clearly while highlighting scheduling conflicts.
* Include automated tests for the core scheduling behaviors.

---

# Getting Started

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Suggested Workflow

1. Read the scenario carefully and identify requirements.
2. Draft a UML diagram.
3. Create Python class stubs.
4. Implement scheduling logic.
5. Test the system.
6. Connect the backend to the Streamlit UI.
7. Refine the UML to match the final implementation.

---

# 🖥️ Sample Output

```text
All Tasks
---------
- 09:00 AM | Morning Walk | 30 min | priority High | incomplete
- 07:30 AM | Breakfast | 15 min | priority High | complete
- 07:30 AM | Breakfast | 15 min | priority High | incomplete
- 09:00 AM | Medication | 10 min | priority Medium | complete

Completed Tasks
---------------
- 07:30 AM | Breakfast | 15 min | priority High | complete
- 09:00 AM | Medication | 10 min | priority Medium | complete

Incomplete Tasks
----------------
- 09:00 AM | Morning Walk | 30 min | priority Low | incomplete
- 07:30 AM | Breakfast | 15 min | priority High | incomplete

Biscuit's Tasks
---------------
- 09:00 AM | Morning Walk | 30 min | priority Low | incomplete
- 07:30 AM | Breakfast | 15 min | priority High | complete
- 07:30 AM | Breakfast | 15 min | priority High | incomplete

Tasks Sorted by Time
--------------------
- 07:30 AM | Breakfast | 15 min | priority High | complete
- 09:00 AM | Morning Walk | 30 min | priority Low | incomplete
- 09:00 AM | Medication | 10 min | priority Medium | complete
- 07:30 AM | Breakfast | 15 min | priority High | incomplete

Conflict Warnings
-----------------
Conflict: 'Morning Walk' and 'Medication' are both scheduled at 09:00 AM.

Today's Schedule
----------------
- 07:30 AM | Breakfast | 15 min | priority High
- 09:00 AM | Morning Walk | 30 min | priority Low
```

---

# 🧪 Testing PawPal+

Run the automated test suite:

```bash
python3 -m pytest
```

The automated tests verify:

* Task completion
* Task addition
* Task sorting by scheduled time
* Daily recurring task creation
* Conflict detection

Successful test run:

```text
=================================================================================== test session starts ===================================================================================
platform darwin -- Python 3.14.5, pytest-9.1.1, pluggy-1.6.0
collected 5 items

tests/test_pawpal.py .....                                                                                                                                                           [100%]

==================================================================================== 5 passed in 0.02s ====================================================================================
```

**Confidence Level:** ⭐⭐⭐⭐☆ (4/5)

The automated test suite verifies the core scheduling functionality, including task completion, task management, sorting, recurring tasks, and conflict detection. While the implemented features work correctly, additional edge cases such as overlapping task durations and more advanced scheduling strategies could be explored in future improvements.

---

# 📐 Smarter Scheduling

| Feature           | Method(s)                                                                  | Notes                                                                               |
| ----------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Task sorting      | `Scheduler.sort_by_time()` and `Scheduler.prioritize_tasks()`              | Tasks can be sorted chronologically or by priority.                                 |
| Filtering         | `Scheduler.filter_tasks_by_status()` and `Scheduler.filter_tasks_by_pet()` | Tasks can be filtered by completion status or by pet name.                          |
| Conflict handling | `Scheduler.detect_conflicts()`                                             | Displays warnings when two tasks are scheduled at the same time.                    |
| Recurring tasks   | `Scheduler.create_next_recurring_task()`                                   | Daily and weekly tasks automatically generate the next occurrence after completion. |

---

# 📸 Demo Walkthrough

1. Enter the owner's name and contact information, then save the details.
2. Add one or more pets by providing the pet's name, species, and age.
3. Create care tasks for each pet by entering the task title, description, duration, scheduled time, and priority.
4. Mark completed tasks using the **Mark Complete** button to update their completion status.
5. Generate the daily schedule to view tasks prioritized for the day. Tasks are displayed in chronological order, and scheduling conflicts are highlighted with warning messages.

**Screenshot or video:**

![Owner Information](images/Demo1.png)

![Add a Pet](images/Demo2.png)

![Add a Task](images/Demo3.png)

![Daily Schedule](images/Demo4.png)
