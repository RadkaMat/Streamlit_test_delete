from collections import defaultdict
import streamlit as st


def render_to_do_list(grouped_tasks: defaultdict, checkbox_state: dict) -> None:
    """
    Render grouped tasks in Streamlit with checkboxes.

    Parameters:
        grouped_tasks (dict): A dictionary with dates as keys and lists of (task, datetime) as values.
        checkbox_state (dict): A dictionary to track the checkbox state for each task.
    """
    for full_date, tasks_for_date in grouped_tasks.items():
        st.subheader(full_date.strftime('%d. %m. %Y'))  # Display the date as a header
        for task, dt in tasks_for_date:
            # Create a unique label for each task with its datetime
            task_label = task+' '+str(dt.strftime('%d. %m. %Y %H:%M'))[:18]+'\n'
            # Render a checkbox for the task
            checkbox_state[task_label] = st.checkbox(label=task, key=task_label)
