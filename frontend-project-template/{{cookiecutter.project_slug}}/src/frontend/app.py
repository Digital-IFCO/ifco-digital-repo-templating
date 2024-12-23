from backend.sum import sum_values
import streamlit as st
from common.logger import setup_logger
from frontend.components.sidebar import SideBar
from frontend.misc.page_config import set_page_config


logger = setup_logger()
set_page_config()
st.title("FrontEnd frontend_app template: Work in progress...")

side_bar = SideBar()
side_bar.render()

if st.button("Calculate sum"):
    side_bar.validate_model()
    sum_result = sum_values(side_bar.model)
    st.write(f"Sum of values: {sum_result}")
