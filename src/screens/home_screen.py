import streamlit as st
import base64
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import base_layout_home , style_base_layout


def home_screen():

    header_home()
    style_base_layout()
    base_layout_home()

    col1 , col2 = st.columns(2, gap="large")

    with col1:
        st.header("I'm Student")
        st.image("src/images/Student.png", width=250)
        if st.button("Student Portal" , type="primary", icon=":material/arrow_outward:", icon_position="right" ):
            st.session_state["login_type"] = "student"
            st.rerun()

    with col2:
        st.header("I'm Teacher")
        st.image("src/images/Teacher.png", width=162)
        if st.button("Teacher Portal", type="primary", icon=":material/arrow_outward:", icon_position="right"):
            st.session_state["login_type"] = "teacher"
            st.rerun()

    footer_home()