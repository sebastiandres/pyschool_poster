import streamlit as st
from streamlit_carousel import carousel
from data import content_dict, button_dict
from glob import glob

# Dynamically generate the carousel items
photo_list = sorted(glob("carousel/*.jpg") + glob("carousel/*.png") + glob("carousel/*.jpeg"))

test_items = [ {"title": "", "text": "", "img": photo} for photo in photo_list ]

# Using https://github.com/thomasbs17/streamlit-contributions/tree/master/bootstrap_carousel
keyword = "photos"
@st.dialog(title="PySchool", width="large")
def carousel_dialog():
    lang = st.session_state["lang"]
    st.session_state["title"] = button_dict[keyword][lang]
    st.session_state["content"] = content_dict[keyword][lang]
    carousel(items=test_items)

