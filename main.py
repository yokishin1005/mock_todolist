import streamlit as st
from task_manager import TaskManager
from task_display import display_tasks
from progress_tracker import display_progress_dashboard

def main():
    st.set_page_config(page_title="Smart ToDo List", layout="wide")
    task_manager = TaskManager()

    st.sidebar.title("Navigation")
    menu = st.sidebar.radio("Go to", ["Tasks", "Progress Dashboard"])

    if menu == "Tasks":
        display_tasks(task_manager)
    elif menu == "Progress Dashboard":
        display_progress_dashboard(task_manager)

if __name__ == "__main__":
    main()