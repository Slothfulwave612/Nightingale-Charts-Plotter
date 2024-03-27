import streamlit as st

def pick_params_values(num_params, default_dict):

    # init list that will contain parameter name and values
    params, values = [], []

    for i in range(int(num_params)):
        # get default values
        if i > default_dict["num_params"] - 1:
            param_name = f"Parameter {i+1}"
            value = 77.0
        else:
            param_name = default_dict["params"][i]
            value = default_dict["values"][i]


        with st.beta_expander(f"Parameter {i+1}", expanded=False):
            # user-input parameter-name
            param = st.text_input(
                label="Enter Parameter Name", value=param_name,
                help="Type the parameter name.", key=f"Parameter_{i+1}_{st.session_state.run}",
            )

            # user-input parameter-value
            label = param.replace("\\n", ' ').replace("\\t", ' ') + " (value)"
            param_value = st.number_input(
                label=label, value=value, key=f"Value_{i+1}_{st.session_state.run}",
                help=f"Type value for {label[:-8]}"
            )
            
            # add to list
            params.append(param)
            values.append(param_value)
    
    default_dict["params"] = params
    default_dict["values"] = values
    
    return default_dict
