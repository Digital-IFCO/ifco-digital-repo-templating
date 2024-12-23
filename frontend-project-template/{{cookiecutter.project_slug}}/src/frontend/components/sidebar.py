from frontend.models.sidebar import SideBarModel
import streamlit as st


class SideBar:
    def render(self):
        self.sidebar = st.sidebar
        self.first_number = self.sidebar.number_input("Introduce un numero")
        self.second_number = self.sidebar.number_input("Introduce otro numero")

    def validate_model(self):
        self.model = SideBarModel(
            first_number=self.first_number,
            second_number=self.second_number
        )