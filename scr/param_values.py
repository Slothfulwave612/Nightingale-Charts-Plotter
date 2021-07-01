import streamlit as st

def pick_params_values(num_params, default_dict, session):

    # init list that will contain parameter name and values
    params, values = [], []

    for i in range(num_params):
        # get default values
        if i > default_dict["num_params"] - 1:
            param_name = f"Parameter {i+1}"
            value = 69.0
        else:
            param_name = default_dict["params"][i]
            value = default_dict["values"][i]


        with st.sidebar.beta_expander(f"Parameter {i+1}", expanded=False):
            # user-input parameter-name
            param = st.text_input(
                label="Enter Parameter Name", value=param_name,
                key=session.run_id, help="Type the parameter name."
            )

            # user-input parameter-value
            label = param.replace("\\n", ' ').replace("\\t", ' ') + " (value)"
            param_value = st.number_input(
                label=label, value=value,
                key=session.run_id, help=f"Type value for {label[:-8]}"
            )
            
            # add to list
            params.append(param)
            values.append(param_value)
        
    default_dict["params"] = params
    default_dict["values"] = values
    
    return default_dict, session
