from streamlit_option_menu import option_menu

def show_sidebar():
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Prediksi"],
        icons=["house", "diamond"],
        menu_icon="list",
        default_index=0,
        styles={"container": {"background-color": "#1E1E1E"}}
    )
    return selected