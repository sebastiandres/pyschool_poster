# Streamlit app that displays the info of PySchool
# Light Blue: #29a6f8
# Dark Blue: #06578e

import streamlit as st
from data import content_dict, button_dict
from photo_carousel import carousel_dialog, test_items
from streamlit_carousel import carousel

st.set_page_config(page_title="PySchool", page_icon="images/pyschool.png")
if "show_photos" not in st.session_state:
    st.session_state["show_photos"] = False

# Select the language
ic, tc = st.columns([1, 3])
ic.image("images/pyschool.png")
options = ["English", "Español"]
st.session_state["lang"] = tc.segmented_control("Language", options, selection_mode="single", default=options[0], label_visibility="hidden")
tc.markdown("## PySchool")
tc.caption(content_dict["subtitle"][st.session_state["lang"]])
lang = st.session_state["lang"]

# Create a callback function for the button
def button_callback(keyword):
    lang = st.session_state["lang"]
    st.session_state["title"] = button_dict[keyword][lang]
    st.session_state["content"] = content_dict[keyword][lang]

def carousel_callback():
    st.session_state["show_photos"] = not st.session_state["show_photos"]

# A generic modal
@st.dialog(title="PySchool", width="large")
def dynamic_dialog():
    st.subheader(st.session_state["title"])
    st.markdown(st.session_state["content"])

# Display the buttons
button_properties = { "use_container_width": True, "type": "primary" }
for keyword in button_dict.keys():
    if keyword != "photos":
        if st.button(button_dict[keyword][lang], on_click=button_callback, args=[keyword], **button_properties):
            dynamic_dialog()
    else:
        if st.button(button_dict[keyword][lang], on_click=carousel_callback, **button_properties):
            if st.session_state["show_photos"]:
                carousel(items=test_items)

# Images: Python Chile and Duoc Valparaiso
_, c1, _, c2, _ = st.columns([1, 2, 1, 2, 1])
c1.image("images/pythonchile.png")
c2.image("images/duoc_valparaiso.png")

# Share buttons
sh1, sh2, sh3 = st.columns([1, 1, 1])
import streamlit.components.v1 as components

# Add a share button for twitter / x
with sh1:
    st.page_link("https://twitter.com/share?ref_src=twsrc%5Etfw", label="Share on Twitter", icon=None)

# Add a share button for linkedin
with sh2:
    st.page_link("https://www.linkedin.com/sharing/share-offsite/?url=https://pyschool.streamlit.app/", label="Share on LinkedIn", icon=None)

# Add a share button for whatsapp
with sh3:
    st.page_link("https://wa.me/?text=Checkout this cool PySchool project! https://pyschool.streamlit.app/", label="Share on WhatsApp", icon=None)
