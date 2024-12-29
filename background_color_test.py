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
TEXT = """
NameError: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).
"""

st.markdown(PAGE_BG_STYLE, unsafe_allow_html=True)
st.title("Big Title")

st.write(TEXT)
      
