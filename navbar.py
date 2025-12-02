import streamlit as st
from streamlit_option_menu import option_menu
# from streamlit_extras.switch_page_button import switch_page

def navbar():

    pages = ["Home", "page1", "page2"]

    # หาว่า page ปัจจุบันอยู่ index ไหน
    current_index = pages.index(st.session_state["page"])

    with st.container():
        selected = option_menu(
            menu_title=None,
            options=pages,
            icons=['house', 'cloud-upload', "graph-up-arrow", 'gear'],
            menu_icon="cast",
            orientation="horizontal",
            default_index=current_index,   # <<<<< ให้ highlight หน้าเดิม
            styles={
                "nav-link": {
                    "text-align": "left",
                    "--hover-color": "#eee",
                }
            }
        )

        # เปลี่ยนหน้า + อัพเดท state
        if selected != st.session_state["page"]:
            st.session_state["page"] = selected
            if selected == "Home":
                st.switch_page("app.py")
            if selected == "page1":
                st.switch_page("pages/1_page1.py")
            if selected == "page2":
                st.switch_page("pages/2_page2.py")