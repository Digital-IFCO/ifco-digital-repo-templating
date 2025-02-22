import os
import streamlit as st

from frontend.models.sidebar import SideBarModel
from frontend.page.home import home


class SideBar:
    def render(self):
        logo_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "assets", "green_rpc.png")
        )
        cliq_logo_sidebar = logo_path
        st.logo(cliq_logo_sidebar)
        home_ = st.Page(
            home, title="Home", icon=":material/home:", default=True
        )

        pg = st.navigation(
            [
                home_,
            ],
            expanded=True,
        )
        pg.run()

        self.sidebar = st.sidebar
        self.first_number = self.sidebar.number_input("Enter a number")
        self.second_number = self.sidebar.number_input("Enter another number")

    def validate_model(self):
        self.model = SideBarModel(
            first_number=self.first_number,
            second_number=self.second_number
        )
