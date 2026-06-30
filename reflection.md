# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

The initial design includes four main classes: Owner, Pet, Task and Scheduler. The Owner class represents the pet owner and stores their pets. The Pet class represents each pet and stores basic pet information and related care tasks. The Task class represents a care activity such as feeding, walking, medication, grooming or appointments. The Scheduler class is responsible for organizing tasks into a daily plan based on constraints like priority and available time.

**b. Design changes**

Initially, tasks only stored their duration and priority. During implementation, I added a scheduled time attribute so that tasks could be organized by time as well as priority. After making this change, I realized that multiple tasks could be assigned the same scheduled time, creating scheduling conflicts. To address this, I implemented conflict detection in the `Scheduler` class, which displays a warning whenever two tasks are scheduled for the same time. This made the scheduling system more practical and user friendly while keeping the overall design simple.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

My scheduler considers several constraints, including scheduled time, task priority, completion status and the amount of time available during the day. I considered scheduled time to be the most important because it determines when a task should be performed and allows the system to sort tasks chronologically and detect scheduling conflicts. Priority is then used to ensure that more important tasks are completed first, while completed tasks are excluded from the daily schedule.

**b. Tradeoffs**

The scheduler currently detects conflicts only when two tasks are scheduled at exactly the same time. It does not check for overlapping task durations or travel time between tasks. This keeps the scheduling logic simple and easy to understand while still providing useful warnings when obvious scheduling conflicts occur.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI for brainstorming system design ideas, generating an initial UML diagram and creating class skeletons. It was also very helpful for explaining error messages, debugging my code and helping me understand Git commands and the purpose of different Python functions. The most helpful prompts were those asking the AI to explain why an error occurred or to suggest ways to improve the design while keeping the implementation simple. AI helped me learn the reasoning behind the code instead of only providing solutions.


**b. Judgment and verification**

One example where I did not accept an AI suggestion immediately was when deciding how to display the pet name for each task. One option was to store the pet's name directly inside every `Task` object. After thinking through the design, I decided to keep the existing relationship where each `Pet` owns its tasks and retrieve the pet name when displaying the table. This avoided duplicating data and kept the object-oriented design cleaner. I evaluated the suggestion by considering how future changes would affect the system.

---

## 4. Testing and Verification

**a. What you tested**

I tested the core behaviors of the PawPal+ system, including task completion, adding tasks to a pet, sorting tasks by scheduled time, creating recurring daily tasks, and detecting scheduling conflicts. These tests were important because they verified that the main scheduling features worked correctly and ensured that changes to one part of the system did not break other functionality. Running automated tests also increased my confidence that the application behaved as expected.

**b. Confidence**

I am confident that the scheduler works correctly for the features implemented because all five automated tests pass successfully and I also verified the application's behavior through the Streamlit interface and the CLI demo. If I had more time, I would test additional edge cases such as overlapping task durations, larger numbers of pets and tasks, more complex recurring schedules and editing or deleting scheduled tasks after they have been created.

---

## 5. Reflection

**a. What went well**

The part of the project I am most satisfied with is successfully connecting the backend logic to the Streamlit user interface. It was rewarding to see the application evolve from a UML diagram into a fully working system where users can add pets, create tasks, generate schedules, detect conflicts and mark tasks as complete.

**b. What you would improve**

If I were to continue developing this project, I would improve the scheduler by supporting overlapping duration conflict detection instead of only exact time matches. I would also allow users to edit or delete existing tasks, support more recurring schedule options and enhance the interface with additional filtering and calendar-style views.

**c. Key takeaway**

One of the biggest lessons I learned is that designing a system requires making thoughtful architectural decisions before writing code. AI was extremely useful for brainstorming ideas, explaining concepts, debugging errors and generating initial implementations, but I still needed to evaluate its suggestions and decide what best fit my own design. I learned that the developer remains the lead architect, while AI works best as a collaborative assistant.
