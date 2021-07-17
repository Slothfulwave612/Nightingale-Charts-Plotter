import streamlit as st

def edit_credit_design(default_dict):
    # Credits Layout
    with st.beta_expander("Credits Layout", expanded=False):
        
        # right-credit
        right_credit = st.text_input(
            label="Enter The Credits", value=default_dict["right_credit"],
            help="Type the credits for the visual.",
            key=f"right_credit_{st.session_state.run}"
        )

        default_dict["right_credit"] = right_credit

        # adjust credit (x-coordinate)
        adjust_right_credit_x = st.number_input(
            label="Adjust Your Credit (x-coord)", format="%.3f",
            min_value=0.0, value=default_dict["adjust_right_credit_x"],
            help="Adjust x-coordinate for the credit text.",
            key=f"adjust_right_credit_x_{st.session_state.run}"
        )

        default_dict["adjust_right_credit_x"] = adjust_right_credit_x

        # adjust credit (y-coordinate)
        adjust_right_credit_y = st.number_input(
            label="Adjust Your Credit (y-coord)", format="%.3f",
            min_value=0.0, value=default_dict["adjust_right_credit_y"],
            help="Adjust y-coordinate for the credit text.",
            key=f"adjust_right_credit_y_{st.session_state.run}"
        )

        default_dict["adjust_right_credit_y"] = adjust_right_credit_y

        # adjust credit (x-coordinate)
        adjust_default_credit_x = st.number_input(
            label="Adjust Default Credit (x-coord)", format="%.3f",
            min_value=0.0, value=default_dict["adjust_default_credit_x"],
            help="Adjust x-coordinate for the default-credit text.",
            key=f"adjust_default_credit_x_{st.session_state.run}"
        )

        default_dict["adjust_default_credit_x"] = adjust_default_credit_x

        # adjust credit (y-coordinate)
        adjust_default_credit_y = st.number_input(
            label="Adjust Default Credit (y-coord)", format="%.3f",
            min_value=0.0, value=default_dict["adjust_default_credit_y"],
            help="Adjust y-coordinate for the default-credit text.",
            key=f"adjust_default_credit_y_{st.session_state.run}"
        )

        default_dict["adjust_default_credit_y"] = adjust_default_credit_y

        # fontsize for credit
        credit_size = st.number_input(
            label="Credit Fontsize", format="%.3f",
            min_value=0.0, value=default_dict["credit_size"],
            help="Choose fontsize for the credit.",
            key=f"credit_size_{st.session_state.run}"
        )

        default_dict["credit_size"] = credit_size

        # title color
        credit_color = st.color_picker(
            label=f"Credit Fontcolor", value=default_dict["credit_color"],
            help=f"Choose fontcolor for the credit.",
            key=f"credit_color_{st.session_state.run}"
        )

        default_dict["credit_color"] = credit_color
    
    return default_dict
