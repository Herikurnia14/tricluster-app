import streamlit as st
from time import sleep
from navigation import make_sidebar
import pandas as pd
import os
#---------Page Config-----------
st.set_page_config(page_title="Triclustering App", page_icon="pictures/ui.png")
st.image("pictures/lg.gif")
c30, c31, c32 = st.columns([0.2, 0.1, 3])
with c30:
    st.caption("")
    st.image("pictures/ui.png", width=60)
with c32:
    st.title("Triclustering App")
    st.subheader("Dive into 3D Gene Expression Patterns!")
    st.write("Powered by Departement of Mathematic - Universitas Indonesia")
# Fungsi untuk autentikasi
def authenticate(username, password):
    return username == "tricluster" and password == "123"
username = st.text_input("Username")
password = st.text_input("Password", type="password")
if st.button("Log in", type="primary"):
    if authenticate(username, password):
        st.session_state.logged_in = True
        st.session_state.username = username  # Simpan username di session_state
        st.success("Logged in successfully!")
        sleep(0.5)
        st.switch_page("pages/OPTricluster.py")
    else:
        st.error("Incorrect username or password")
