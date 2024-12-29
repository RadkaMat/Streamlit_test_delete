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

form1 = st.form('Checking form', clear_on_submit=True)
with form1:
  for index, item in enumerate(test_list):
    checkbox1 = st.checkbox(label=item, key=index)
    if checkbox1:
        test_list.pop(index)
        st.rerun
  confirm = form1.form_submit_button('Done')
  
