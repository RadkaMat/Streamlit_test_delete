import streamlit as st

# Constants
PAGE_BG_STYLE = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1722082839802-18b18cb23a62");
    background-size: cover;
}
[data-testid="stAppViewBlockContainer"] {
    background-color: #262626;
}
</style>
"""
test_list = ['first', 'second', 'third']

st.title("Big Title")

form = st.form('Checking form', clear_on_submit=True)
with form:
  for index, item in enumerate(test_list):
    checkbox_state[item] = st.checkbox(label=item, key=index)
    if checkbox_state[item]:
        test_list.pop(index)
        st.rerun
  confirm = form.form_submit_button('Done')
  
