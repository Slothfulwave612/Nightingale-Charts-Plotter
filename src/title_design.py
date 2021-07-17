import streamlit as st

def edit_title_design(default_dict, template):

    # Title and Subtitle
    with st.beta_expander("Title & Subtitle Layout", expanded=False):
        # title
        title = st.text_input(
            label="Enter The Title", value=default_dict["title"],
            help="Type the title for the visual.",
            key=f"title_{st.session_state.run}"
        )

        default_dict["title"] = title

        # fontsize for title
        title_size = st.number_input(
            label="Title Fontsize", format="%.3f",
            min_value=0.0, value=default_dict["title_size"],
            help="Choose fontsize for the title.",
            key=f"title_size_{st.session_state.run}"
        )

        default_dict["title_size"] = title_size

        # title color
        title_color = st.color_picker(
            label=f"Title Fontcolor", value=default_dict["title_color"],
            help=f"Choose fontcolor for the title.",
            key=f"title_color_{st.session_state.run}"
        )

        default_dict["title_color"] = title_color

        # adjust title (x-coordinate)
        adjust_title_x = st.number_input(
            label="Adjust Title (x-coord)", value=default_dict["adjust_title_x"],
            format="%.3f", key=f"adjust_title_x_{st.session_state.run}",
            help="Adjust x-coordinate for the title."
        )

        default_dict["adjust_title_x"] = adjust_title_x

        # adjust title (y-coordinate)
        adjust_title_y = st.number_input(
            label="Adjust Title (y-coord)", value=default_dict["adjust_title_y"],
            format="%.3f", key=f"adjust_title_y_{st.session_state.run}",
            help="Adjust y-coordinate for the title."
        )

        default_dict["adjust_title_y"] = adjust_title_y

        # title-alignment
        title_alignment = st.radio(
            label="Title Horizontal Alignment", options=["center", "right", "left"],
            index=0, help="Choose horizontal alingnment for title text",
            key=f"title_alignment_{st.session_state.run}"
        )

        default_dict["title_alignment"] = title_alignment

        # sub-title
        sub_title = st.text_input(
            label="Enter The Sub-Title", value=default_dict["sub_title"],
            help="Type the sub-title for the visual.",
            key=f"sub_title_{st.session_state.run}"
        )

        default_dict["sub_title"] = sub_title

        # fontsize for title
        sub_title_size = st.number_input(
            label="Sub-Title Fontsize", format="%.3f",
            min_value=0.0, value=default_dict["sub_title_size"],
            help="Choose fontsize for the sub-title.",
            key=f"sub_title_size_{st.session_state.run}"
        )

        default_dict["sub_title_size"] = sub_title_size

        # title color
        sub_title_color = st.color_picker(
            label=f"Sub-Title Fontcolor", value=default_dict["sub_title_color"],
            help=f"Choose fontcolor for the sub-title.",
            key=f"sub_title_color_{st.session_state.run}"
        )

        default_dict["sub_title_color"] = sub_title_color

        # adjust title (x-coordinate)
        adjust_sub_title_x = st.number_input(
            label="Adjust Sub-Title (x-coord)",
            value=default_dict["adjust_sub_title_x"], format="%.3f",
            help="Adjust x-coordinate for the sub-title.",
            key=f"adjust_sub_title_x_{st.session_state.run}"
        )

        default_dict["adjust_sub_title_x"] = adjust_sub_title_x

        # adjust title (y-coordinate)
        adjust_sub_title_y = st.number_input(
            label="Adjust Sub-Title (y-coord)", format="%.3f",
            value=default_dict["adjust_sub_title_y"],
            help="Adjust y-coordinate for the sub-title.",
            key=f"adjust_sub_title_y_{st.session_state.run}"
        )

        default_dict["adjust_sub_title_y"] = adjust_sub_title_y

        # sub-title-alignment
        sub_title_alignment = st.radio(
            label="Sub-Title Horizontal Alignment", options=["center", "right", "left"],
            index=0, help="Choose horizontal alingnment for sub-title text",
            key=f"sub_title_alignment_{st.session_state.run}"
        )

        default_dict["sub_title_alignment"] = sub_title_alignment

        if template in ["Colorful Pizza (Light)", "Colorful Pizza (Dark)"]:
            # legend-text
            legend_texts = st.text_input(
                label=f"Enter Legend Text Seperated By Space", value=default_dict["legend_texts"],
                help="Type the legends for the visual.", key=f"legend_texts_{st.session_state.run}"
            )

            legend_space = st.number_input(
                label=f"Space Between Legend", min_value=0,
                value=default_dict["legend_space"], key=f"legend_space_{st.session_state.run}",
                help="How many spaces do you want between your legend texts?"
            )

            # fontsize for legend
            legend_size = st.number_input(
                label="Legend Fontsize", format="%.3f",
                min_value=0.0, value=default_dict["legend_size"],
                help="Choose fontsize for the legend.",
                key=f"legend_size_{st.session_state.run}"
            )

            # adjust legend (x-coordinate)
            adjust_legend_x = st.number_input(
                label="Adjust Legend (x-coord)",
                value=default_dict["adjust_legend_x"], format="%.3f",
                help="Adjust x-coordinate for the legend.",
                key=f"adjust_legend_x_{st.session_state.run}"
            )

            # adjust title (y-coordinate)
            adjust_legend_y = st.number_input(
                label="Adjust Legend (y-coord)", format="%.3f",
                value=default_dict["adjust_legend_y"],
                help="Adjust y-coordinate for the legend.",
                key=f"adjust_legend_y_{st.session_state.run}"
            )

            # legend-alignment
            legend_alignment = st.radio(
                label="Legend Horizontal Alignment", options=["center", "right", "left"],
                index=0, help="Choose horizontal alingnment for legend text",
                key=f"legend_alignment_{st.session_state.run}"
            )

            default_dict["legend_texts"] = legend_texts
            default_dict["legend_space"] = legend_space
            default_dict["legend_size"] = legend_size
            default_dict["adjust_legend_x"] = adjust_legend_x
            default_dict["adjust_legend_y"] = adjust_legend_y
            default_dict["legend_alignment"] = legend_alignment
    
    return default_dict
