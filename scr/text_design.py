import streamlit as st

def edit_text_design(default_dict, session):
    # TEXT DESIGN LAYOUT
    with st.sidebar.beta_expander("Text Design Layout", expanded=False):
        
        # param-text colors
        param_text_colors = st.color_picker(
            label="Parameter Text Color", value=default_dict["param_text_colors"],
            key=session.run_id, help="Choose color for all the parameter texts"
        )

        default_dict["param_text_colors"] = param_text_colors
        
        # fontsize for param-text
        param_text_size = st.number_input(
            label="Parameter Texts Fontsize", format="%.3f",
            min_value=0.0, value=default_dict["param_text_size"],
            key=session.run_id, help="Choose fontsize for parameter texts"
        )

        default_dict["param_text_size"] = param_text_size

        # location for param-text
        param_location = st.number_input(
            label="Parameter Location", format="%.3f",
            min_value=0.0, value=default_dict["param_location"],
            key=session.run_id, help="Choose location for parameter texts"
        )

        default_dict["param_location"] = param_location

        # value text color
        value_text_color = st.color_picker(
            label="Choose Value Text Color", value=default_dict["value_text_color"],
            key=session.run_id, help="Choose color for all the slices"
        )
     
        default_dict["value_text_color"] = value_text_color
            
        # fontsize for value-text
        value_text_size = st.number_input(
            label="Value Texts Fontsize", format="%.3f",
            min_value=0.0, value=default_dict["value_text_size"],
            key=session.run_id, help="Choose fontsize for value texts"
        )
        
        default_dict["value_text_size"] = value_text_size

        # get boxstyle for value-text
        value_boxstyle = st.selectbox(
            label="Boxstyle For Value Text", options=["none", "circle", "round", "round4", "roundtooth", "sawtooth", "square"],
            index=default_dict["value_boxstyle"], key=session.run_id,
            help="Choose a boxstyle for the value-text."
        )

        default_dict["value_boxstyle"] = value_boxstyle

        # padding value
        box_pad = st.number_input(
            label="Padding Value For Box", format="%.3f",
            min_value=0.0, value=default_dict["box_pad"],
            key=session.run_id, help="Choose padding-value for box."
        )

        default_dict["box_pad"] = box_pad

        # edgecolor for box
        box_ec = st.color_picker(
            label="Edgecolor For Box", value=default_dict["box_ec"],
            key=session.run_id, help="Choose edgecolor for box."
        )

        default_dict["box_ec"] = box_ec

        # linewidth for box
        box_lw = st.number_input(
            label="Linewidth For Box", format="%.3f",
            min_value=0.0, value=default_dict["box_lw"],
            key=session.run_id, help="Choose linewidth for box."
        )

        default_dict["box_lw"] = box_lw

        # choose option for box facecolor
        choose_box_fc = st.radio(
            label="Choose Box Facecolor", options=["Same Color As The Slice", "Different Color"],
            index=default_dict["choose_box_fc"], key=session.run_id, help="Choose the required box facecolor."
        )

        if choose_box_fc == "Different Color":
            if default_dict["box_fc"] == "same": default_dict["box_fc"] = "#222222"
            # box facecolor
            box_fc = st.color_picker(
                    label="Choose Facecolor For All Boxes", value=default_dict["box_fc"],
                    key=session.run_id, help="Choose facecolor for all the boxes"
                )
        else:
            box_fc = "same"

        default_dict["box_fc"] = box_fc
            
    return default_dict, session
