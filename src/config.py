import streamlit as st

def init_page():
    """Initialize Streamlit page configuration"""
    st.set_page_config(
        page_title="Blockchain Research AI",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.title("🔗 Blockchain Research AI")