import streamlit as st
from dependencies import get_essay_list
import random

st.set_page_config(page_title='Check Student\'s Essay', page_icon='✏️')

# Open Style Sheet and apply
with open('check_cessay_style.css', encoding='UTF-8') as f:
    st.html(f"<style>{f.read()}</style>")

if 'initialized' not in st.session_state:
    # Get essay list from dependencies.py
    st.session_state.essay_list = get_essay_list()
    st.session_state.initialized = True

essay_list = st.session_state.essay_list

st.title('Check Student\'s Essay')
st.divider()

for x in essay_list:
    # Define a button for each essay
    essay_button = st.button(x.replace('.docx', ''), use_container_width=True)
    if essay_button:
        st.session_state["target"] = x
        st.switch_page('pages/check.py')

# Removing everything in st.session_state dictionary
for x in st.session_state:
    del st.session_state[x]
