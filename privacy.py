import streamlit as st

st.set_page_config(page_title="Privacy Policy", page_icon="🔐")

st.title("Privacy Policy")

st.write(
    """
    This Privacy Policy explains how BoardFlow accesses and uses
    user-authorized information in compliance with applicable
    developer platform policies.
    """
)

st.subheader("Information Accessed")
st.markdown(
    """
    - Account information authorized by the user
    - Board and content data required for application features
    """
)

st.subheader("How Information Is Used")
st.markdown(
    """
    - To authenticate users when they choose to connect an external service
    - To perform actions explicitly requested by the user
    """
)

st.subheader("Data Storage")
st.write(
    """
    This application does not permanently store personal user data.
    """
)

st.subheader("Data Sharing")
st.write(
    """
    No user data is sold, shared, or transferred to third parties.
    """
)

st.subheader("Contact")
st.write(
    """
    📧 your@email.com
    """
)
