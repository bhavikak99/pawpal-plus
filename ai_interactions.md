# AI Interactions Log

This document summarizes how AI tools were used throughout the PawPal+ project, including advanced features completed beyond the core requirements.

---

# Agent Workflow: Next Available Slot

### Task Given to the Agent

Implement an advanced scheduling feature that could suggest the next available time slot when an existing task time was already occupied.

### Files Modified

* `pawpal_system.py`
* `main.py`

### What the Agent Completed

* Suggested creating a `Scheduler.find_next_available_slot()` method.
* Implemented an algorithm that checks existing scheduled task start times and searches forward in 30-minute increments until an available slot is found.
* Updated `main.py` to demonstrate the new algorithm in the CLI output.

### Manual Corrections

I reviewed the generated algorithm to ensure it matched the overall scheduler design. I intentionally kept the implementation lightweight by checking only exact start-time conflicts rather than implementing more complex overlapping-duration scheduling.

---

# Prompt Comparison

### Task

Design the recurring task scheduling logic for PawPal+.

|                       | Option A                                                                                                                                                                                  | Option B                                                                                                            |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Model / Tool Used** | ChatGPT                                                                                                                                                                                   | GitHub Copilot                                                                                                      |
| **Prompt**            | *How should I implement recurring daily and weekly tasks while keeping the scheduler simple and maintainable?*                                                                            | *Generate a recurring task implementation for PawPal+ based on my current classes.*                                 |
| **Response Summary**  | Suggested creating a separate scheduler method to generate future recurring tasks while preserving completed task history.                                                                | Generated an initial implementation of recurring task logic based on the existing class structure.                  |
| **What Was Useful**   | Explained why recurring behavior belongs in the Scheduler instead of the Task class and emphasized maintaining completed tasks as history.                                                | Quickly generated a working implementation and reduced repetitive coding.                                           |
| **Problems Noticed**  | Some suggestions extended beyond the project requirements and needed to be simplified.                                                                                                    | The generated implementation still required manual review to ensure it matched the intended object-oriented design. |
| **Decision**          | Used the architectural ideas from ChatGPT while also using Copilot to scaffold the implementation. The final code was simplified and adjusted manually to match the project requirements. | Used as implementation support rather than copied directly.                                                         |

### Final Decision

I combined suggestions from both ChatGPT and GitHub Copilot while making the final architectural decisions myself. I chose to keep recurring task generation inside the `Scheduler` class because recurring behavior is part of scheduling rather than an individual task's responsibility. I also simplified the implementation to support daily and weekly recurrence, which matched the scope of the project.
