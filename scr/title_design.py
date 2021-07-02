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

        # Legend
        num_legends = st.number_input(
            label="Number of Legend Text You Want To Add", min_value=0,
            value=default_dict["num_legends"], key=session.run_id,
            help="Number of Legend Text You Want To Add"
        )

        default_dict["num_legends"] = num_legends

        if num_legends > 0:
            legend_texts, legend_colors = [], []

            for index in range(num_legends):
                if len(default_dict["legend_texts"]) == 0 or index > len(default_dict["legend_texts"]) - 1:
                    text_val = f"Legend Text {index+1}"
                    color_val = "#4169e1" 
                else:
                    text_val = default_dict["legend_texts"][index]
                    color_val = default_dict["legend_colors"][index]

                temp_text = st.text_input(
                    label=f"Enter Text For Legend {index+1}", value=text_val,
                    key=session.run_id, help="Type the title for the visual."
                )

                temp_color = st.color_picker(
                    label=f"Color For {temp_text}", value=color_val,
                    key=session.run_id, help=f"Choose color for {temp_text} (Legend)"
                )
                
                legend_texts.append(temp_text)
                legend_colors.append(temp_color)

            legend_space = st.number_input(
                label=f"Space Between Legend", min_value=0,
                value=default_dict["legend_space"],
                key=session.run_id, help="How many spaces do you want between your legend texts?"
            )

            # fontsize for legend
            legend_size = st.number_input(
                label="Legend Fontsize", format="%.3f",
                min_value=0.0, value=default_dict["legend_size"],
                key=session.run_id, help="Choose fontsize for the legend."
            )

            # adjust legend (x-coordinate)
            adjust_legend_x = st.number_input(
                label="Adjust Legend (x-coord)",
                value=default_dict["adjust_legend_x"], format="%.3f",
                key=session.run_id, help="Adjust x-coordinate for the legend."
            )

            # adjust title (y-coordinate)
            adjust_legend_y = st.number_input(
                label="Adjust Legend (y-coord)", format="%.3f",
                value=default_dict["adjust_legend_y"],
                key=session.run_id, help="Adjust y-coordinate for the legend."
            )

            # legend-alignment
            legend_alignment = st.radio(
                label="Legend Horizontal Alignment", options=["center", "right", "left"],
                index=0, key=session.run_id, help="Choose horizontal alingnment for legend text"
            )

            default_dict["legend_texts"] = legend_texts
            default_dict["legend_colors"] = legend_colors
            default_dict["legend_space"] = legend_space
            default_dict["legend_size"] = legend_size
            default_dict["adjust_legend_x"] = adjust_legend_x
            default_dict["adjust_legend_y"] = adjust_legend_y
            default_dict["legend_alignment"] = legend_alignment
    
    return default_dict, session
