import streamlit as st

def edit_credit_design(default_dict, session):
    # Credits Layout
    with st.sidebar.beta_expander("Credits Layout", expanded=False):
        
        # right-credit
        right_credit = st.text_input(
            label="Enter The Credits", value=default_dict["right_credit"],
            key=session.run_id, help="Type the credits for the visual."
        )

        default_dict["right_credit"] = right_credit

        # adjust credit (x-coordinate)
        adjust_right_credit_x = st.number_input(
            label="Adjust Your Credit (x-coord)", format="%.3f",
            min_value=0.0, value=default_dict["adjust_right_credit_x"],
            key=session.run_id, help="Adjust x-coordinate for the credit text."
        )

        default_dict["adjust_right_credit_x"] = adjust_right_credit_x

        # adjust credit (y-coordinate)
        adjust_right_credit_y = st.number_input(
            label="Adjust Your Credit (y-coord)", format="%.3f",
            min_value=0.0, value=default_dict["adjust_right_credit_y"],
            key=session.run_id, help="Adjust y-coordinate for the credit text."
        )

        default_dict["adjust_right_credit_y"] = adjust_right_credit_y

        # adjust credit (x-coordinate)
        adjust_default_credit_x = st.number_input(
            label="Adjust Default Credit (x-coord)", format="%.3f",
            min_value=0.0, value=default_dict["adjust_default_credit_x"],
            key=session.run_id, help="Adjust x-coordinate for the default-credit text."
        )

        default_dict["adjust_default_credit_x"] = adjust_default_credit_x

        # adjust credit (y-coordinate)
        adjust_default_credit_y = st.number_input(
            label="Adjust Default Credit (y-coord)", format="%.3f",
            min_value=0.0, value=default_dict["adjust_default_credit_y"],
            key=session.run_id, help="Adjust y-coordinate for the default-credit text."
        )

        default_dict["adjust_default_credit_y"] = adjust_default_credit_y

        # fontsize for credit
        credit_size = st.number_input(
            label="Credit Fontsize", format="%.3f",
            min_value=0.0, value=default_dict["credit_size"],
            key=session.run_id, help="Choose fontsize for the credit."
        )

        default_dict["credit_size"] = credit_size

        # title color
        credit_color = st.color_picker(
            label=f"Credit Fontcolor", value=default_dict["credit_color"],
            key=session.run_id, help=f"Choose fontcolor for the credit."
        )

        default_dict["credit_color"] = credit_color
    
    return default_dict, session
