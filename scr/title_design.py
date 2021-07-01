import streamlit as st

def edit_title_design(default_dict, session):

    # Title and Subtitle
    with st.sidebar.beta_expander("Title & Subtitle Layout", expanded=False):
        # title
        title = st.text_input(
            label="Enter The Title", value=default_dict["title"],
            key=session.run_id, help="Type the title for the visual."
        )

        default_dict["title"] = title

        # fontsize for title
        title_size = st.number_input(
            label="Title Fontsize", format="%.3f",
            min_value=0.0, value=default_dict["title_size"],
            key=session.run_id, help="Choose fontsize for the title."
        )

        default_dict["title_size"] = title_size

        # title color
        title_color = st.color_picker(
            label=f"Title Fontcolor", value=default_dict["title_color"],
            key=session.run_id, help=f"Choose fontcolor for the title."
        )

        default_dict["title_color"] = title_color

        # adjust title (x-coordinate)
        adjust_title_x = st.number_input(
            label="Adjust Title (x-coord)", value=default_dict["adjust_title_x"],
            format="%.3f",
            key=session.run_id, help="Adjust x-coordinate for the title."
        )

        default_dict["adjust_title_x"] = adjust_title_x

        # adjust title (y-coordinate)
        adjust_title_y = st.number_input(
            label="Adjust Title (y-coord)", value=default_dict["adjust_title_y"],
            format="%.3f",
            key=session.run_id, help="Adjust y-coordinate for the title."
        )

        default_dict["adjust_title_y"] = adjust_title_y

        # title-alignment
        title_alignment = st.radio(
            label="Title Horizontal Alignment", options=["center", "right", "left"],
            index=0, key=session.run_id, help="Choose horizontal alingnment for title text"
        )

        default_dict["title_alignment"] = title_alignment

        # sub-title
        sub_title = st.text_input(
            label="Enter The Sub-Title", value=default_dict["sub_title"],
            key=session.run_id, help="Type the sub-title for the visual."
        )

        default_dict["sub_title"] = sub_title

        # fontsize for title
        sub_title_size = st.number_input(
            label="Sub-Title Fontsize", format="%.3f",
            min_value=0.0, value=default_dict["sub_title_size"],
            key=session.run_id, help="Choose fontsize for the sub-title."
        )

        default_dict["sub_title_size"] = sub_title_size

        # title color
        sub_title_color = st.color_picker(
            label=f"Sub-Title Fontcolor", value=default_dict["sub_title_color"],
            key=session.run_id, help=f"Choose fontcolor for the sub-title."
        )

        default_dict["sub_title_color"] = sub_title_color

        # adjust title (x-coordinate)
        adjust_sub_title_x = st.number_input(
            label="Adjust Sub-Title (x-coord)",
            value=default_dict["adjust_sub_title_x"], format="%.3f",
            key=session.run_id, help="Adjust x-coordinate for the sub-title."
        )

        default_dict["adjust_sub_title_x"] = adjust_sub_title_x

        # adjust title (y-coordinate)
        adjust_sub_title_y = st.number_input(
            label="Adjust Sub-Title (y-coord)", format="%.3f",
            value=default_dict["adjust_sub_title_y"],
            key=session.run_id, help="Adjust y-coordinate for the sub-title."
        )

        default_dict["adjust_sub_title_y"] = adjust_sub_title_y

        # sub-title-alignment
        sub_title_alignment = st.radio(
            label="Sub-Title Horizontal Alignment", options=["center", "right", "left"],
            index=0, key=session.run_id, help="Choose horizontal alingnment for sub-title text"
        )

        default_dict["sub_title_alignment"] = sub_title_alignment
    
    return default_dict, session
