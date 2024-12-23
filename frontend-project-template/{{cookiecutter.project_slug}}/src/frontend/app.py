import streamlit as st
from common.logger import setup_logger
from frontend.components.side_bar import my_func
from frontend.layout.page_config import set_page_config


logger = setup_logger()
set_page_config()
st.title("FrontEnd frontend_app template: Work in progress...")

side_bar = st.sidebar
first_number = side_bar.number_input("Introduce un numero")
second_number = side_bar.number_input("Introduce otro numero")

if st.button("Calculate sum"):
    sum_result = my_func(first_number, second_number)
    st.write(f"Sum of values: {sum_result}")
