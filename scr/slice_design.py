import streamlit as st

def edit_slice_design(default_dict, session):

    # DESIGN LAYOUT
    with st.sidebar.beta_expander("Slice Design Layout", expanded=False):
        # get background color
        background_color = st.color_picker(
            label="Background Color", value=default_dict["background_color"],
            key=session.run_id, help="Choose a color for your plot's background."
        )

        default_dict["background_color"] = background_color

        # get straight line color
        straight_line_color = st.color_picker(
            label="Straight Line Color", value=default_dict["straight_line_color"],
            key=session.run_id, help="Choose a color for the straight lines in the plot."
        )

        default_dict["straight_line_color"] = straight_line_color

        # get straight line linewidth
        straight_line_lw = st.number_input(
            label="Straight Line Linewidth", min_value=0.0,
            value=default_dict["straight_line_lw"], format="%.3f",
            key=session.run_id, help="Enter linewidth for the straight lines."
        )

        default_dict["straight_line_lw"] = straight_line_lw

        # get straight-line linestyle
        straight_line_ls = st.selectbox(
            label="Straight-Line Linestyle", options=["None", "solid", "dashed", "dashdot", "dotted"],
            index=default_dict["straight_line_ls"], key=session.run_id,
            help="Choose a linestyle for the straight lines."
        )

        default_dict["straight_line_ls"] = straight_line_ls

        # get last circle color
        last_circle_color = st.color_picker(
            label="Last Circle Color", value=default_dict["last_circle_color"],
            key=session.run_id, help="Choose a color for the last circle in the plot."
        )

        default_dict["last_circle_color"] = last_circle_color

        # get last circle linewidth
        last_circle_lw = st.number_input(
            label="Last Circle Linewidth", min_value=0.0, format="%.3f",
            value=default_dict["last_circle_lw"],
            key=session.run_id, help="Enter linewidth for the last circle."
        )

        default_dict["last_circle_lw"] = last_circle_lw

        # get last circle linestyle
        last_circle_ls = st.selectbox(
            label="Last Circle Linestyle", options=["None", "solid", "dashed", "dashdot", "dotted"],
            index=default_dict["last_circle_ls"], key=session.run_id,
            help="Choose a linestyle for the last circle."
        )

        default_dict["last_circle_ls"] = last_circle_ls

        # get other circles color
        other_circle_color = st.color_picker(
            label="Other Circles Color", value=default_dict["other_circle_color"],
            key=session.run_id, help="Choose a color for all the other circles in the plot."
        )

        default_dict["other_circle_color"] = other_circle_color

        # get other circles linewidth
        other_circle_lw = st.number_input(
            label="Other Circles Linewidth", min_value=0.0,
            value=default_dict["other_circle_lw"], format="%.3f",
            key=session.run_id, help="Enter linewidth for the other circles."
        )

        default_dict["other_circle_lw"] = other_circle_lw

        # get other circles linestyle
        other_circle_ls = st.selectbox(
            label="Other Circles Linestyle",
            options=["None", "solid", "dashed", "dashdot", "dotted"],
            index=default_dict["other_circle_ls"], key=session.run_id,
            help="Choose a linestyle for the other circles."
        )

        default_dict["other_circle_ls"] = other_circle_ls

        # get inner circles size
        inner_circle_size = st.number_input(
            label="Center Circle Size",
            value=default_dict["inner_circle_size"], format="%.3f",
            key=session.run_id, help="Enter size for the center circle. (To change circle size - the value for Center Circle Size and Straight Line Lower Limit should be close to each other)"
        )

        default_dict["inner_circle_size"] = inner_circle_size

        # get inner circles size
        inner_circle_limit = st.number_input(
            label="Straight Line Lower Limit",
            value=default_dict["inner_circle_limit"], format="%.3f",
            key=session.run_id, help="Straight Line Lower Limit (To change circle size - the value for Center Circle Size and Straight Line Lower Limit should be close to each other)"
        )

        default_dict["inner_circle_limit"] = inner_circle_limit

        # slice colors
        choose_slice_colors = st.radio(
            label="Slice Colors", options=["Same Color", "Different Colors"],
            index=default_dict["choose_slice_colors"], key=session.run_id,
            help="Do you want same color for all the slices or different colors?"
        )

        default_dict["choose_slice_colors"] = choose_slice_colors

        if choose_slice_colors == "Same Color":
            if type(default_dict["slice_colors"]) is list:
                default_dict["slice_colors"] = default_dict["slice_colors"][0]
                
            slice_colors = st.color_picker(
                label="Choose Slice Face Color", value=default_dict["slice_colors"],
                key=session.run_id, help="Choose color for all the slices"
            )
        else:
            slice_colors = []

            if type(default_dict["slice_colors"]) is str:
                default_dict["slice_colors"] = [default_dict["slice_colors"]] * len(default_dict["params"])

            for index, param in enumerate(default_dict["params"]):
                if index > default_dict["num_params"] - 1:
                    param_name = f"Parameter {index+1}"
                    value = default_dict["slice_colors"][-1]
                else:
                    param_name = default_dict["params"][index]
                    value = default_dict["slice_colors"][index]

                param = param_name.replace("\\n", ' ').replace("\\t", ' ')
                temp_color = st.color_picker(
                    label=f"Color For {param_name} Slice", value=value,
                    key=session.run_id, help=f"Choose color for {param_name} Slice"
                )
                slice_colors.append(temp_color)
        
        default_dict["slice_colors"] = slice_colors

        # slice linewidth
        slice_lw = st.number_input(
            label="Slice Linewidth", 
            min_value=0.0, value=default_dict["slice_lw"],
            format="%.3f",
            key=session.run_id, help="Choose slice linewidth"
        )

        default_dict["slice_lw"] = slice_lw
        
        # slice-edge-color
        slice_ec= st.color_picker(
            label=f"Choose Slice Egde Color", value=default_dict["slice_ec"],
            key=session.run_id, help="Choose color for all the slice edges"
        )

        default_dict["slice_ec"] = slice_ec

        # slice-blank-space colors
        choose_slice_blank_colors = st.radio(
            label="Slice (Blank Space) Colors", options=["Same Color As The Slices", "Different Color"],
            index=default_dict["choose_slice_blank_colors"], key=session.run_id,
            help="Do you want same color for all the blank-slice-area or different colors?"
        )

        default_dict["choose_slice_blank_colors"] = choose_slice_blank_colors

        if choose_slice_blank_colors == "Same Color As The Slices":
            slice_blank_colors = "same"
            
        elif choose_slice_blank_colors == "Different Color":
            if default_dict["slice_blank_colors"] == "same": default_dict["slice_blank_colors"] = "#4169e1"
            
            slice_blank_colors = st.color_picker(
                label=f"Color For Blank Space", value=default_dict["slice_blank_colors"],
                key=session.run_id, help=f"Choose color for blank space for all slices"
            )
        
        default_dict["slice_blank_colors"] = slice_blank_colors
        
        # transparency-level for blank-spaces
        transparency_blank_space = st.number_input(
            label="Transparency Level For Blank Space Colors",
            min_value=0.0, max_value=1.0,
            format="%.3f", value=default_dict["transparency_blank_space"],
            key=session.run_id, help="0 means fully-transparent, 1 means not-transparent"
        )

        default_dict["transparency_blank_space"] = transparency_blank_space

        # bottom-value for slice
        bottom = st.number_input(
            label="Start Value For The Slice", 
            value=default_dict["bottom"], format="%.3f",
            key=session.run_id, help="Enter start value for the slice"
        )

        default_dict["bottom"] = bottom

        # end-value for slice
        straight_line_limit = st.number_input(
            label="End Value For The Slice", value=default_dict["straight_line_limit"],
            key=session.run_id, help="Enter end value for the slice", format="%.3f",
        )

        default_dict["straight_line_limit"] = straight_line_limit

    return default_dict, session
