import streamlit as st
from functions import list_utils, render_utils, task_utils

# Constants
PAGE_BG_STYLE = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1722082839802-18b18cb23a62");
    background-size: cover;
}
[data-testid="stAppViewBlockContainer"] {
    background-color: #262730;
}
</style>
"""

# Functions interacting with streamlit session
def add_new_to_do():
    """ Handle the event of adding a new to-do via Streamlit widget. """
    new_to_do = st.session_state['new_to_do_widget']
    if list_utils.check_valid_input(new_to_do):
        updated_to_do_list = list_utils.add_new_to_do_logic(to_do_list, new_to_do)
        st.session_state['new_to_do'] = new_to_do
    st.session_state['new_to_do_widget'] = ''


# Initialization
st.markdown(PAGE_BG_STYLE, unsafe_allow_html=True)
st.title("To-Do List")

if 'new_to_do' not in st.session_state:
    st.session_state.new_to_do = ''
to_do_list = list_utils.get_to_do_list(file_path=list_utils.FILE_PATHS['data'])
checkbox_state = {to_do: False for to_do in to_do_list}

# Parse and grop tasks
parsed_tasks = task_utils.parse_tasks(to_do_list)
grouped_tasks = task_utils.group_tasks_by_date(parsed_tasks)

# Render to-do list form
form = st.form('To-do form', clear_on_submit=True)
with form:
    render_utils.render_to_do_list(grouped_tasks, checkbox_state)

    if form.form_submit_button('Done'):
        # Separate tasks into undone and done categories in one iteration
        to_do_list_undone, to_do_list_done = [], []
        for to_do, checked in checkbox_state.items():
            if checked:
                to_do_list_done.append(to_do)
            else:
                to_do_list_undone.append(to_do)

        # Save the updated to-do list and history log
        list_utils.save_to_do_list(to_do_list_undone, file_path=list_utils.FILE_PATHS['data'], save_mode='w')
        list_utils.save_to_do_list(to_do_list_done, file_path=list_utils.FILE_PATHS['history'], save_mode='a')

        # Rerun the app to reflect changes
        st.rerun()

# Add new to-do
st.title('New to-do +')
st.text_input(label='Write new to-do:',
              value='',
              placeholder='Write new to-do... [press Enter to confirm]',
              on_change=add_new_to_do,
              key='new_to_do_widget')

# Message to write the last added to-do
st.write(f'The last added to-do: {st.session_state.new_to_do}')

# Show history of the finished to-does
if st.button('Show history 🕒'):
    list_utils.show_to_do_history()

# Delete history of the finished to-does
if st.button('Delete history', type='primary'):
    list_utils.delete_to_do_history()

# Code check
st.session_state
