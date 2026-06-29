# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

The initial design includes four main classes: Owner, Pet, Task and Scheduler. The Owner class represents the pet owner and stores their pets. The Pet class represents each pet and stores basic pet information and related care tasks. The Task class represents a care activity such as feeding, walking, medication, grooming or appointments. The Scheduler class is responsible for organizing tasks into a daily plan based on constraints like priority and available time.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

The scheduler currently detects conflicts only when two tasks are scheduled at exactly the same time. It does not check for overlapping task durations or travel time between tasks. This keeps the scheduling logic simple and easy to understand while still providing useful warnings when obvious scheduling conflicts occur.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
