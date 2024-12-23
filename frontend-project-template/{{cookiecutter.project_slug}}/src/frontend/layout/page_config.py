import os

import streamlit as st
from PIL import Image


def set_page_config():
    logo_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "assets", "green_rpc.png")
    )
    logo = Image.open(logo_path)
    st.set_page_config(page_title="App title", page_icon=logo, layout="wide")

