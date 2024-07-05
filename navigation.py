import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages


def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")

    return pages[ctx.page_script_hash]["page_name"]


def make_sidebar():
    with st.sidebar:
        st.title("🧬 Triclustering App")
        st.write("")
        st.write("")

        if st.session_state.get("logged_in", False):
            st.page_link("pages/THD-Tricluster.py", label="THD-Tricluster", icon="📑")
            st.page_link("pages/OPTricluster.py", label="OPTricluster", icon="📊")
            st.page_link("pages/delta-trimax.py", label="δ-Trimax", icon="📈")

            st.write("")
            st.write("")

            if st.button("Log out"):
                logout()

        elif get_current_page_name() != "Tricluster":
            # If anyone tries to access a secret page without being logged in,
            # redirect them to the login page
            st.switch_page("deploy.py")

        # Add Footer
            st.write("")
            st.markdown("---")
            st.markdown("Powered by Magister of Mathematics", unsafe_allow_html=True)



def logout():
    st.session_state.logged_in = False
    st.info("Logged out successfully!")
    sleep(0.5)
    st.switch_page("deploy.py")
    