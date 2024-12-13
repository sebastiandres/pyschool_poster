import streamlit as st
from streamlit_carousel import carousel
from data import content_dict, button_dict

test_items = [
    dict(
        title="PySchool",
        text="",
        img="carousel/pyschool_00.jpg",
    ),
    dict(
        title="PySchool",
        text="",
        img="carousel/pyschool_01.jpg",
    ),
    dict(
        title="PySchool",
        text="",
        img="carousel/pyschool_02.jpg",
    ),
]

# Using https://github.com/thomasbs17/streamlit-contributions/tree/master/bootstrap_carousel
keyword = "photos"
@st.dialog(title="PySchool", width="large")
def carousel_dialog():
    lang = st.session_state["lang"]
    st.session_state["title"] = button_dict[keyword][lang]
    st.session_state["content"] = content_dict[keyword][lang]
    carousel(items=test_items)

