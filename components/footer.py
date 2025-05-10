import streamlit as st

def show_footer():
    footer_style = """
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #121212;
    color: #FAFAFA;
    text-align: center;
    padding: 10px;
    """
    st.markdown(
        """
        <footer style='{}'>
            © 2025, Persevera Team
        </footer>
        """.format(footer_style),
        unsafe_allow_html=True
    )
