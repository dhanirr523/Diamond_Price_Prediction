import streamlit as st
import page.prediksi as prediksi
import page.home as home
import components.sidebar as sd
import components.footer as ft

st.set_page_config(
    page_title="Diamond Price Prediction",
    page_icon="logo/logo_diamond.png",
    menu_items=None
)

def main():
    with st.sidebar:
        selected = sd.show_sidebar()

    if selected == "Home":
        home.show_home()
    elif selected == "Prediksi":
        prediksi.run_ml_app()

    ft.show_footer()


if __name__ == "__main__":
    main()