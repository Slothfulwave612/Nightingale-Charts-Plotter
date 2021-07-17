import streamlit as st

def edit_slice_design(default_dict, template, num_params):

    # DESIGN LAYOUT
    with st.beta_expander("Slice Design Layout", expanded=False):
        # get background color
        background_color = st.color_picker(
            label="Background Color", value=default_dict["background_color"],
            help="Background Color For The Whole Plot.", key=f"background_color_{st.session_state.run}"
        )

        default_dict["background_color"] = background_color

        # get straight line color
        straight_line_color = st.color_picker(
            label="Straight Line Color", value=default_dict["straight_line_color"],
            help="Lines That Divides The Slices.", key=f"straight_line_color_{st.session_state.run}"
        )

        default_dict["straight_line_color"] = straight_line_color

        # get straight line linewidth
        straight_line_lw = st.number_input(
            label="Straight Line Linewidth", min_value=0.0,
            value=default_dict["straight_line_lw"], format="%.3f",
            help="Lines That Divides The Slices.", key=f"straight_line_lw_{st.session_state.run}"
        )

        default_dict["straight_line_lw"] = straight_line_lw

        # get straight-line linestyle
        straight_line_ls = st.selectbox(
            label="Straight-Line Linestyle", options=["None", "solid", "dashed", "dashdot", "dotted"],
            index=default_dict["straight_line_ls"], key=f"straight_line_ls_{st.session_state.run}",
            help="Lines That Divides The Slices.."
        )

        default_dict["straight_line_ls"] = straight_line_ls

        # get last circle color
        last_circle_color = st.color_picker(
            label="Circle Boundary Color", value=default_dict["last_circle_color"],
            help="Circle Boundary.", key=f"last_circle_color_{st.session_state.run}"
        )

        default_dict["last_circle_color"] = last_circle_color

        # get last circle linewidth
        last_circle_lw = st.number_input(
            label="Circle Boundary Linewidth", min_value=0.0, format="%.3f",
            value=default_dict["last_circle_lw"], key=f"last_circle_lw_{st.session_state.run}",
            help="Circle Boundary."
        )

        default_dict["last_circle_lw"] = last_circle_lw

        # get last circle linestyle
        last_circle_ls = st.selectbox(
            label="Circle Boundary Linestyle", options=["None", "solid", "dashed", "dashdot", "dotted"],
            index=default_dict["last_circle_ls"], key=f"last_circle_ls_{st.session_state.run}",
            help="Circle Boundary."
        )

        default_dict["last_circle_ls"] = last_circle_ls

        # get other circles color
        other_circle_color = st.color_picker(
            label="Other Circles Color", value=default_dict["other_circle_color"],
            help="Choose a color for all the other circles in the plot.",
            key=f"other_circle_color_{st.session_state.run}"
        )

        default_dict["other_circle_color"] = other_circle_color

        # get other circles linewidth
        other_circle_lw = st.number_input(
            label="Other Circles Linewidth", min_value=0.0,
            value=default_dict["other_circle_lw"], format="%.3f",
            help="Enter linewidth for the other circles.", 
            key=f"other_circle_lw_{st.session_state.run}"
        )

        default_dict["other_circle_lw"] = other_circle_lw

        # get other circles linestyle
        other_circle_ls = st.selectbox(
            label="Other Circles Linestyle",
            options=["None", "solid", "dashed", "dashdot", "dotted"],
            index=default_dict["other_circle_ls"],
            help="Choose a linestyle for the other circles.", 
            key=f"other_circle_ls_{st.session_state.run}"
        )

        default_dict["other_circle_ls"] = other_circle_ls

        # get inner circles size
        inner_circle_size = st.number_input(
            label="Center Circle Size", key=f"inner_circle_size_{st.session_state.run}",
            value=default_dict["inner_circle_size"], format="%.3f",
            help="Enter size for the center circle. (To change circle size - the value for Center Circle Size and Straight Line Lower Limit should be close to each other)"
        )

        default_dict["inner_circle_size"] = inner_circle_size

        # get inner circles size
        inner_circle_limit = st.number_input(
            label="Straight Line Lower Limit", key=f"inner_circle_limit_{st.session_state.run}",
            value=default_dict["inner_circle_limit"], format="%.3f",
            help="Straight Line Lower Limit (To change circle size - the value for Center Circle Size and Straight Line Lower Limit should be close to each other)"
        )

        default_dict["inner_circle_limit"] = inner_circle_limit

        if template in ["Light Theme Pizza", "Dark Theme Pizza"]:
            if type(default_dict["slice_colors"]) is list:
                default_dict["slice_colors"] = default_dict["slice_colors"][0]
                
            slice_colors = st.color_picker(
                label="Choose Slice Face Color", value=default_dict["slice_colors"],
                help="Choose color for all the slices", key=f"slice_colors_{st.session_state.run}"
            )
        else:
            slice_colors = []

            if type(default_dict["slice_colors"]) is str:
                default_dict["slice_colors"] = [default_dict["slice_colors"]] * len(default_dict["params"])

            for index, param in enumerate(default_dict["params"]):
                if index > default_dict["num_params"] - 1 and index > num_params - 1:
                    param_name = f"Parameter {index+1}"
                    value = default_dict["slice_colors"][-1]
                else:
                    param_name = default_dict["params"][index]

                    try:
                        value = default_dict["slice_colors"][index]
                    except Exception:
                        value = default_dict["slice_colors"][-1]

                param = param_name.replace("\\n", ' ').replace("\\t", ' ')
                temp_color = st.color_picker(
                    label=f"Color For {param_name} Slice", value=value,
                    help=f"Choose color for {param_name} Slice",
                    key=f"temp_color_slice_{index}_{st.session_state.run}"
                )
                slice_colors.append(temp_color)
        
        default_dict["slice_colors"] = slice_colors

        # slice linewidth
        slice_lw = st.number_input(
            label="Slice Linewidth", 
            min_value=0.0, value=default_dict["slice_lw"],
            format="%.3f", key=f"slice_lw_{st.session_state.run}",
            help="Choose slice linewidth"
        )

        default_dict["slice_lw"] = slice_lw
        
        # slice-edge-color
        slice_ec= st.color_picker(
            label=f"Choose Slice Egde Color", value=default_dict["slice_ec"],
            help="Choose color for all the slice edges", key=f"slice_ec_{st.session_state.run}"
        )

        default_dict["slice_ec"] = slice_ec

        # slice blank colors
        if default_dict["slice_blank_colors"] != "same":
            slice_blank_colors = st.color_picker(
                label=f"Color For Blank Space", value=default_dict["slice_blank_colors"],
                help=f"Choose color for blank space for all slices",
                key=f"slice_blank_colors_{st.session_state.run}"
            )
            
            default_dict["slice_blank_colors"] = slice_blank_colors
        
        # transparency-level for blank-spaces
        transparency_blank_space = st.number_input(
            label="Transparency Level For Blank Space Colors",
            min_value=0.0, max_value=1.0, key=f"transparency_blank_space_{st.session_state.run}",
            format="%.3f", value=default_dict["transparency_blank_space"],
            help="0 means fully-transparent, 1 means not-transparent"
        )

        default_dict["transparency_blank_space"] = transparency_blank_space

        # bottom-value for slice
        bottom = st.number_input(
            label="Start Value For The Slice", 
            value=default_dict["bottom"], format="%.3f",
            help="Enter start value for the slice", key=f"bottom_{st.session_state.run}"
        )

        default_dict["bottom"] = bottom

        # end-value for slice
        straight_line_limit = st.number_input(
            label="End Value For The Slice", value=default_dict["straight_line_limit"],
            help="Enter end value for the slice", format="%.3f", key=f"straight_line_limit_{st.session_state.run}"
        )

        default_dict["straight_line_limit"] = straight_line_limit

    return default_dict
