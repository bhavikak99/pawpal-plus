import streamlit as st

from pawpal_system import Owner, Pet, Scheduler, Task


PRIORITY_MAP = {
    "High": 1,
    "Medium": 2,
    "Low": 3,
}


st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to PawPal+.

This app helps pet owners manage pets, add care tasks, and generate a daily care schedule.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.
"""
    )

st.divider()

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan", "jordan@example.com")

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()

st.subheader("Owner Info")

owner_name = st.text_input(
    "Owner name",
    value="",
    placeholder="Enter owner's name"
)
contact_info = st.text_input(
    "Contact info",
    value="",
    placeholder="Enter email or phone number"
)

if st.button("Save owner info"):
    st.session_state.owner.name = owner_name
    st.session_state.owner.contact_info = contact_info
    st.success("Owner info saved.")

st.divider()

st.subheader("Add a Pet")

with st.form("add_pet_form", clear_on_submit=True):
    pet_name = st.text_input(
    "Pet name",
    placeholder="Enter pet's name"
    )
    species = st.selectbox(
    "Species",
    ["Select a species", "Dog", "Cat", "Other"]
    )
    age = st.number_input("Age", min_value=0, max_value=100, value=1)
    submitted_pet = st.form_submit_button("Add pet")

if submitted_pet:
    if not pet_name or species == "Select a species":
        st.error("Please enter the pet's name and select a species.")
    else:
        new_pet = Pet(pet_name, species, int(age))
        st.session_state.owner.add_pet(new_pet)
        st.success(f"Added pet: {pet_name}")

pets = st.session_state.owner.get_pets()

if pets:
    st.write("Current pets:")
    pet_rows = [
        {"name": pet.name, "species": pet.species, "age": pet.age}
        for pet in pets
    ]
    st.table(pet_rows)
else:
    st.info("No pets added yet.")

st.divider()

st.subheader("Add a Task")

if pets:
    selected_pet_index = st.selectbox(
        "Choose pet",
        range(len(pets)),
        format_func=lambda i: pets[i].name,
    )
    selected_pet = pets[selected_pet_index]

    with st.form("add_task_form", clear_on_submit=True):
        task_title = st.text_input("Task title", placeholder="Enter task title")
        task_description = st.text_input("Task description", placeholder="Enter task description")
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
        priority_label = st.selectbox("Priority", ["High", "Medium", "Low"])
        submitted_task = st.form_submit_button("Add task")

        if submitted_task:
            if not task_title:
                st.error("Please enter a task title.")
            else:
                task = Task(
                    title=task_title,
                    description=task_description,
                    duration_minutes=int(duration),
                    priority=PRIORITY_MAP[priority_label],
                )
                selected_pet.add_task(task)
                st.success(f"Added task '{task_title}' to {selected_pet.name}")
                st.rerun()

    all_task_rows = []
    for pet in pets:
        for task in pet.get_tasks():
            all_task_rows.append(
                {
                    "pet": pet.name,
                    "task": task.title,
                    "duration": task.duration_minutes,
                    "priority": task.priority,
                    "completed": "Yes" if task.completed else "No",
                }
            )

    if all_task_rows:
        st.write("Current tasks:")
        st.table(all_task_rows)

        incomplete_tasks = []
        for pet in pets:
            for task in pet.get_tasks():
                if not task.completed:
                    incomplete_tasks.append((pet, task))

        if incomplete_tasks:
            task_to_complete = st.selectbox(
                "Choose a task to mark complete",
                range(len(incomplete_tasks)),
                format_func=lambda i: f"{incomplete_tasks[i][0].name}: {incomplete_tasks[i][1].title}",
            )

            if st.button("Mark complete"):
                incomplete_tasks[task_to_complete][1].mark_complete()
                st.success("Task marked complete.")
                st.rerun()
        else:
            st.info("All tasks are complete.")
    else:
        st.info("No tasks added yet.")
else:
    st.info("Add a pet before adding tasks.")
st.divider()

st.subheader("Build Schedule")

available_minutes = st.number_input(
    "Available minutes today",
    min_value=1,
    max_value=1440,
    value=1440,
)

if st.button("Generate schedule"):
    schedule = st.session_state.scheduler.generate_daily_schedule(
        st.session_state.owner,
        int(available_minutes),
    )

    if schedule:
        st.success("Today's Schedule")
        for task in schedule:
            st.write(
                f"- {task.title}: {task.duration_minutes} min, priority {task.priority}"
            )
    else:
        st.warning("No tasks fit into the available time.")