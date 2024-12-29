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

st.title("Big Title")

form1 = st.form('Checking form', clear_on_submit=True)
with form1:
    check = st.checkbox(label='Check the button', key='check')
    confirmed = form1.form_submit_button('Done')
    if check and confirmed:
        st.write('Good job!')
    else:
        st.write('Check the button, plese.')
      
