import streamlit as st

def display_tasks(task_manager):
    st.title("Task List")

    with st.expander("Add a new task"):
        title = st.text_input("Title")
        description = st.text_area("Description")
        due_date = st.date_input("Due Date")

        if st.button("Add Task"):
            task_manager.create_task(title, description, due_date)

    for index, task in enumerate(task_manager.tasks):
        with st.expander(task["title"]):
            st.write(task["description"])
            st.write("Category:", task["category"])
            st.write("Due Date:", task["due_date"])

            if not task["completed"]:
                if st.button("Mark as Complete", key=f"complete_{index}"):
                    task_manager.complete_task(index)
                if st.button("Edit", key=f"edit_{index}"):
                    # Add code for editing the task
                    pass
                if st.button("Delete", key=f"delete_{index}"):
                    task_manager.delete_task(index)
            else:
                st.success("This task is completed!")