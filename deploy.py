import streamlit as st
from time import sleep

# Konfigurasi halaman
st.set_page_config(page_title="Triclustering App", page_icon="🧬")

# Fungsi untuk autentikasi
def authenticate(username, password):
    return username == "tricluster" and password == "123"

# Inisialisasi session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

st.title("Triclustering App")
st.subheader("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Log in", type="primary"):
    if authenticate(username, password):
        st.session_state.logged_in = True
        st.success("Logged in successfully!")
        sleep(1)
        st.switch_page("pages/THD-Tricluster.py")
    else:
        st.error("Incorrect username or password")
