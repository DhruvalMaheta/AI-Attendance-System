import streamlit as st
import base64


def header_home():
    # for image showing in HTML first read in bytes and after that using base64 encode & decode it

    with open("src/images/logo.png", "rb") as image_file:
        img_bytes = base64.b64encode(image_file.read()).decode()

    st.markdown(f"""
        <div style = "display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px;">
            <img src="data:image/png;base64,{img_bytes}" style= "height:100px;"  alt='snapClass logo' />
            <h1 style = "text-align:center; color:#E0E3FF">SNAP<br>CLASS</h1>
        </div>


                """ , unsafe_allow_html=True)


def header_dashboard():
    # for image showing in HTML first read in bytes and after that using base64 encode & decode it

    with open("src/images/logo.png", "rb") as image_file:
        img_bytes = base64.b64encode(image_file.read()).decode()

    st.markdown(f"""
        <div style = "display:flex; align-items:center; justify-content:center; gap:10px;">
            <img src="data:image/png;base64,{img_bytes}" style= "height:85px;"  alt='snapClass logo'/>
            <h2 style = "text-align:left; color:#5865F2;">SNAP<br>CLASS</h2>
        </div>


                """ , unsafe_allow_html=True)