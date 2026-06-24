from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
import datetime


@dataclass
class Task:
    title: str
    description: Optional[str] = None
    duration_minutes: int = 0
    priority: int = 0
    scheduled_time: Optional[datetime.datetime] = None
    completed: bool = False

    def mark_complete(self) -> None:
        pass

    def is_overdue(self) -> bool:
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, task: Task) -> None:
        pass

    def get_tasks(self) -> List[Task]:
        pass


class Owner:
    def __init__(self, name: str, contact_info: str, pets: Optional[List[Pet]] = None) -> None:
        self.name = name
        self.contact_info = contact_info
        self.pets: List[Pet] = pets if pets is not None else []

    def add_pet(self, pet: Pet) -> None:
        pass

    def remove_pet(self, pet: Pet) -> None:
        pass

    def get_pets(self) -> List[Pet]:
        pass


class Scheduler:
    def __init__(self, available_minutes_per_day: int = 480) -> None:
        self.available_minutes_per_day = available_minutes_per_day

    def generate_daily_schedule(self, owner: Owner, available_minutes: int) -> List[Task]:
        pass

    def prioritize_tasks(self, tasks: List[Task]) -> List[Task]:
        pass

    def assign_task_time(self, task: Task, start_time: datetime.datetime) -> None:
        pass
