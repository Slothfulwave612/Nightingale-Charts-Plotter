import streamlit as st
from tempfile import NamedTemporaryFile
import base64

def get_your_plot(fig):
    with st.sidebar.form(key='my_form'):
        # filename
        filename = st.text_input(
            label="Enter The Filename", value="my_file",
            key=f"Enter The Filename", help="Type the filename (without file-format)"
        )

        # file-format
        file_format = st.radio(
            label="File Format", options=["png", "jpg", "jpeg", "pdf", "raw", "svg", "svgz", "tif", "tiff"],
            index=0, key="File Format", help="Choose the required file-format."
        )

        # dpi
        dpi = st.number_input(
            label="Dots-per-Inch Value", 
            min_value=50, value=500,
            key="Dots-per-Inch Value", help="Higher The Value Better The Resolution."
        )

        # pad-inches
        pad_inches = st.number_input(
            label="Pad Inches", value=0.03, format="%.3f",
            key="Pad Inches", help="Amount of padding around the plot."
        )

        submit_button = st.form_submit_button(label='Download')

        # download
        if submit_button:
            pass
    