import streamlit as st

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

        # transparency
        transparency = st.radio(
            label="Transparent", options=["Yes", "No"],
            index=1, key="Transparent", help="Downloaded plot will not have background. (file-format should be png)"
        )

        # pad-inches
        pad_inches = st.number_input(
            label="Pad Inches", value=0.03,
            key="Pad Inches", help="Amount of padding around the plot."
        )

        submit_button = st.form_submit_button(label='Download')

        # download
        if submit_button:
            if transparency == "Yes":
                transparency = True
            else:
                transparency = False

            # save figure
            fig.savefig(
                fname=filename, format=file_format, dpi=dpi,
                bbox_inches="tight",
                transparent=transparency, pad_inches=pad_inches
            )
