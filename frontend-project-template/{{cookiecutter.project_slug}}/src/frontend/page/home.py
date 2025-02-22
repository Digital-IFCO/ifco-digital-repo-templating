import streamlit as st

from backend.sum import sum_values
from frontend.models.sidebar import SideBarModel

def validate_model(first_number, second_number):
    model = SideBarModel(
        first_number=first_number,
        second_number=second_number
    )

    return model

def home():
    st.write("# Welcome to Hello World App! 👋")
    st.markdown(
        """
        This is an amazing template for streamlit 🚀
        """,
        unsafe_allow_html=False,
    )

    sidebar = st.sidebar
    first_number = sidebar.number_input("Enter a number")
    second_number = sidebar.number_input("Enter another number")

    if st.button("Calculate sum"):
        model = validate_model(first_number, second_number)
        sum_result = sum_values(model)
        st.write(f"Sum of values: {sum_result}")