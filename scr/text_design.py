import streamlit as st

def edit_text_design(default_dict):
    # TEXT DESIGN LAYOUT
    with st.beta_expander("Text Design Layout", expanded=False):
        
        # param-text colors
        param_text_colors = st.color_picker(
            label="Parameter Text Color", value=default_dict["param_text_colors"],
            help="Choose color for all the parameter texts",
            key=f"param_text_colors_{st.session_state.run}"
        )

        default_dict["param_text_colors"] = param_text_colors
        
        # fontsize for param-text
        param_text_size = st.number_input(
            label="Parameter Texts Fontsize", format="%.3f",
            min_value=0.0, value=default_dict["param_text_size"],
            help="Choose fontsize for parameter texts",
            key=f"param_text_size_{st.session_state.run}"
        )

        default_dict["param_text_size"] = param_text_size

        # location for param-text
        param_location = st.number_input(
            label="Parameter Location", format="%.3f",
            min_value=0.0, value=default_dict["param_location"],
            help="Choose location for parameter texts",
            key=f"param_location"
        )

        default_dict["param_location"] = param_location

        # value text color
        value_text_color = st.color_picker(
            label="Choose Value Text Color", value=default_dict["value_text_color"],
            help="Choose color for all the slices", key=f"value_text_color_{st.session_state.run}"
        )
     
        default_dict["value_text_color"] = value_text_color
            
        # fontsize for value-text
        value_text_size = st.number_input(
            label="Value Texts Fontsize", format="%.3f",
            min_value=0.0, value=default_dict["value_text_size"],
            help="Choose fontsize for value texts", key=f"value_text_size_{st.session_state.run}"
        )
        
        default_dict["value_text_size"] = value_text_size

        # get boxstyle for value-text
        value_boxstyle = st.selectbox(
            label="Boxstyle For Value Text", options=["none", "circle", "round", "round4", "roundtooth", "sawtooth", "square"],
            index=default_dict["value_boxstyle"], key=f"value_boxstyle",
            help="Choose a boxstyle for the value-text."
        )

        default_dict["value_boxstyle"] = value_boxstyle

        # padding value
        box_pad = st.number_input(
            label="Padding Value For Box", format="%.3f",
            min_value=0.0, value=default_dict["box_pad"],
            help="Choose padding-value for box.", key=f"box_pad_{st.session_state.run}"
        )

        default_dict["box_pad"] = box_pad

        # edgecolor for box
        box_ec = st.color_picker(
            label="Edgecolor For Box", value=default_dict["box_ec"],
            help="Choose edgecolor for box.", key=f"box_ec_{st.session_state.run}"
        )

        default_dict["box_ec"] = box_ec

        # linewidth for box
        box_lw = st.number_input(
            label="Linewidth For Box", format="%.3f",
            min_value=0.0, value=default_dict["box_lw"],
            help="Choose linewidth for box.", key=f"box_lw_{st.session_state.run}"
        )

        default_dict["box_lw"] = box_lw

        # box facecolor
        if default_dict["box_fc"] != "same":
            box_fc = st.color_picker(
                label="Choose Facecolor For All Boxes", value=default_dict["box_fc"],
                help="Choose facecolor for all the boxes", key=f"box_fc_{st.session_state.run}"
            )

            default_dict["box_fc"] = box_fc
            
    return default_dict
