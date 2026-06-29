from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
import datetime


@dataclass
class Task:
    """Represents a care task for a pet."""
    title: str
    description: Optional[str] = None
    duration_minutes: int = 0
    priority: int = 0
    scheduled_time: Optional[datetime.datetime] = None
    completed: bool = False

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True

    def is_overdue(self) -> bool:
        """Return True if scheduled and past now and not completed."""
        if self.scheduled_time is None:
            return False
        if self.completed:
            return False
        return self.scheduled_time < datetime.datetime.now()


@dataclass
class Pet:
    """A pet owned by an Owner, holding care tasks."""
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        self.tasks.append(task)

    def remove_task(self, task: Task) -> None:
        """Remove a task from this pet if it exists."""
        try:
            self.tasks.remove(task)
        except ValueError:
            # Task not found; ignore silently for simplicity
            return

    def get_tasks(self) -> List[Task]:
        """Return a list of this pet's tasks."""
        return list(self.tasks)


class Owner:
    """Represents a pet owner with contact info and pets."""
    def __init__(self, name: str, contact_info: str, pets: Optional[List[Pet]] = None) -> None:
        self.name = name
        self.contact_info = contact_info
        self.pets: List[Pet] = pets if pets is not None else []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's list of pets."""
        self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from the owner if present."""
        try:
            self.pets.remove(pet)
        except ValueError:
            return

    def get_pets(self) -> List[Pet]:
        """Return a list of the owner's pets."""
        return list(self.pets)


class Scheduler:
    """Generates schedules and assigns times for tasks."""
    def __init__(self, available_minutes_per_day: int = 480) -> None:
        self.available_minutes_per_day = available_minutes_per_day

    def generate_daily_schedule(self, owner: Owner, available_minutes: int) -> List[Task]:
        """Generate a list of incomplete tasks fitting within available minutes."""
        # Gather all incomplete tasks from all pets
        all_tasks: List[Task] = []
        for pet in owner.get_pets():
            for t in pet.get_tasks():
                if not t.completed:
                    all_tasks.append(t)

        # Prioritize tasks
        prioritized = self.prioritize_tasks(all_tasks)

        # Select tasks until we run out of available minutes
        schedule: List[Task] = []
        minutes_left = max(0, int(available_minutes))
        for task in prioritized:
            dur = max(0, int(task.duration_minutes))
            if dur <= minutes_left:
                schedule.append(task)
                minutes_left -= dur
            else:
                # Skip tasks that don't fit in remaining time
                continue

        return schedule

    def prioritize_tasks(self, tasks: List[Task]) -> List[Task]:
        """Return tasks sorted by priority (higher first)."""
        # Higher priority value should come first
        return sorted(tasks, key=lambda t: t.priority)

    def assign_task_time(self, task: Task, start_time: datetime.datetime) -> None:
        """Assign a scheduled start time to the task."""
        task.scheduled_time = start_time
