import streamlit as st

def choose_template():
    with st.sidebar.form(key='template_form'):
        template = st.selectbox(
            "Select Template",
            options=["Light Theme Pizza", "Dark Theme Pizza", "Colorful Pizza (Light)", "Colorful Pizza (Dark)"],
            index=2, help="Select Template"
        )

        # generate template
        submit_button = st.form_submit_button(label='Generate Template')

        if submit_button:
            gen_temp = True
            st.session_state.run += 1
        else:
            gen_temp = False

            if st.session_state.get("run") is None:
                st.session_state.run = 0

    return template, gen_temp


def pick_params(default_dict):
    # sidebar - user input for params
    num_params = st.sidebar.number_input(
        label="Total Number of Parameters", min_value=1,
        value=default_dict["num_params"], key=f"num_params_{st.session_state.run}",
        help="How many parameters do you have?"
    )

    return num_params
