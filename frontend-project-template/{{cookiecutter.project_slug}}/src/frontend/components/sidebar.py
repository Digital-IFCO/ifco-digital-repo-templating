import os
import streamlit as st

from frontend.page.home import home


class SideBar:
    def render(self):
        logo_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "assets", "ifco-logo.svg")
        )
        cliq_logo_sidebar = logo_path
        st.logo(cliq_logo_sidebar)
        home_ = st.Page(
            home, title="Home", icon=":material/home:", default=True
        )

        page_2 = st.Page(
            home, title="Page 2", icon=":material/home:", url_path="page_2"
        )

        pg = st.navigation(
            [
                home_,
                page_2
            ],
            expanded=True,
        )
        pg.run()
