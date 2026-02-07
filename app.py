import streamlit as st

st.set_page_config(
    page_title="BoardFlow Platform",
    page_icon="📌",
    layout="centered"
)

st.markdown(
    """
    <h1 style="text-align:center;">BoardFlow Platform</h1>
    <p style="text-align:center; color:gray;">
        Secure • Compliant • Streamlit-powered
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

st.subheader("About")
st.write(
    """
    BoardFlow is a web application that allows users to manage
    visual boards and content through a clean web interface.

    The platform is designed with user privacy, transparency,
    and developer policy compliance in mind.
    """
)

st.subheader("Features")
st.markdown(
    """
    - Secure account connection (OAuth-ready)
    - Visual board and content management
    - Automation-ready structure
    - No user data stored without consent
    """
)

st.divider()

st.subheader("Status")
st.success("Application is live and running.")

st.divider()
st.markdown(
    """
    <p style="text-align:center; font-size:13px; color:gray;">
        <a href="/privacy" target="_self">Privacy Policy</a> • Contact: your@email.com
    </p>
    """,
    unsafe_allow_html=True
)
