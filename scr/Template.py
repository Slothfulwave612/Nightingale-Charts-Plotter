import streamlit as st

def choose_template(session):
    with st.sidebar.form(key='template_form'):
        template = st.selectbox(
            "Select Template",
            options=["Light Theme Pizza", "Dark Theme Pizza", "Colorful Pizza (Light)", "Colorful Pizza (Dark)"],
            index=2, help="Select Template"
        )

        # generate template
        submit_button = st.form_submit_button(label='Generate Template')

        # download
        if submit_button:
            session.run_id += 1

    return template, session


def pick_params(default_dict, session):
    # sidebar - user input for params
    num_params = st.sidebar.number_input(
        label="Total Number of Parameters", min_value=1,
        value=default_dict["num_params"],
        key=session.run_id, help="How many parameters do you have?"
    )

    return num_params, session
