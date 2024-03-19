import streamlit as st
import matplotlib.pyplot as plt

def display_progress_dashboard(task_manager):
    st.title("Progress Dashboard")

    completed_tasks = [task for task in task_manager.tasks if task["completed"]]
    incomplete_tasks = [task for task in task_manager.tasks if not task["completed"]]

    st.subheader("Completed")
    st.write(len(completed_tasks))

    st.subheader("Incomplete")
    st.write(len(incomplete_tasks))

    if task_manager.tasks:
        progress_data = {
            "Completed\n": len(completed_tasks),
            "Total\n": len(task_manager.tasks)
        }
        
        fig, ax = plt.subplots()
        ax.bar(progress_data.keys(), progress_data.values())
        ax.set_ylim(0, len(task_manager.tasks) * 1.2)  # 縦軸のスケールを調整
        
        st.subheader("Overall Progress")
        st.pyplot(fig)