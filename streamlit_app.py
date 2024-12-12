# Streamlit app that displays the info of PySchool

import streamlit as st

st.set_page_config(page_title="PySchool", page_icon=":school:")

options = ["English", "Español"]
language_sel = st.segmented_control("Language", options, selection_mode="single", label_visibility="hidden", default=options[0])

# All the text definitions
title_dict = {
    "English": ["PySchool", "Breaking barriers to education"],
    "Español": ["PySchool", "Rompiendo barreras a la educación"]
}
authors_dict = {
    "English": "Authors",
    "Español": "Autores"
}
about_title_dict = {
    "English": "About",
    "Español": "Acerca de"
}
about_dict = {
    "English": "PySchool is a school that teaches Python programming language to students.",
    "Español": "PySchool es una escuela que enseña el lenguaje de programación Python a estudiantes."
}
references_title_dict = {
    "English": "References",
    "Español": "Referencias"
}

# Define the authors modal
@st.dialog(authors_dict[language_sel], width="large")
def authors():
    col1, col2 = st.columns(2)
    col1.page_link(page="https://www.linkedin.com/in/sebastiandres/", label="Sebastian Flores", icon=None, use_container_width=True)
    col2.page_link(page="https://www.linkedin.com/in/faam/", label="Francisco Alfaro", icon=None, use_container_width=True)

# Define the about modal
@st.dialog(about_title_dict[language_sel], width="large")
def about():
    st.write(about_dict[language_sel])

# Define the references modal
@st.dialog(references_title_dict[language_sel], width="large")
def references():
    mkd = """
    * Repo: https://github.com/python-chile/pyschool2024/ 
    * Website: https://pyschool.cl/ 
    * https://www.linkedin.com/posts/pythonchiledev_pyschool-python-educaci%C3%B3n-activity-7234401423780696064-W-vt/?originalSubdomain=es 
    * https://www.instagram.com/admisionduocuc_vregion/p/C_lLWF8JS9J/?img_index=1 
    * https://pythonchile.cl/pyschool-en-valparaiso-inspirando-a-la-proxima-generacion-de-programadores-python.html 
    """
    st.write(mkd)

# Lorem Ipsum
@st.dialog("Lorem Ipsum", width="large")
def loremipsum():
    st.write("Lorem Ipsum")

#-----------------------------------------------------------------------------#
title, subtitle = title_dict[language_sel]
st.title(title)
st.caption(subtitle)
if st.button(authors_dict[language_sel], use_container_width=True):
    authors()
if st.button("Acknowledgement", use_container_width=True):
    loremipsum()
if st.button(about_title_dict[language_sel], use_container_width=True):
    about()
if st.button("Tech Stack", use_container_width=True):
    loremipsum()
if st.button("Replicate the initiative", use_container_width=True):
    loremipsum()
if st.button(references_title_dict[language_sel], use_container_width=True):
    references()
st.image("images/pyschool.png")
