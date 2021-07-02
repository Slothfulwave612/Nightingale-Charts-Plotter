"""
Python module for the webapp.

Author: Anmol Durgapal / @slothfulwave612
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import is_color_like
from matplotlib.backends.backend_agg import RendererAgg
import streamlit as st

from default_values import get_default_values
from pizza import PizzaPlotter

from page import background_and_title
from Template import choose_template, pick_params
from param_values import pick_params_values
from slice_design import edit_slice_design
from text_design import edit_text_design
from title_design import edit_title_design
from credit_design import edit_credit_design
from download import get_your_plot
import SessionState

# use renderer
matplotlib.use("agg")
_lock = RendererAgg.lock

# get session-state id
session = SessionState.get(run_id=0)

# set page-config
st.set_page_config(page_title="Nightingale", page_icon=None, layout="centered", initial_sidebar_state='expanded')

# page-setup and title
background_and_title()


# <---------------- INITIAL SETUP ----------------> #

# fetch template
template, session = choose_template(session)

# get default-dict
default_dict = get_default_values(template_type=template)

# fetch number of parameters
num_params, session = pick_params(default_dict, session)

# Second Options
st.sidebar.subheader("Edit Parameters & Values")

# fetch parameter and corresponding values
default_dict, session = pick_params_values(num_params, default_dict, session)

# <---------------- INITIAL SETUP ----------------> #



# <---------------- EDIT DESIGN ----------------> #

# Design
st.sidebar.subheader("Edit Design")

# fetch slice design edits
default_dict, session = edit_slice_design(default_dict, session)

# fetch text design edits
default_dict, session = edit_text_design(default_dict, session)

# fetch title design edits
default_dict, session = edit_title_design(default_dict, session)

# fetch credit design edits
default_dict, session = edit_credit_design(default_dict, session)

# <---------------- EDIT DESIGN ----------------> #



# <---------------- PLOT PIZZA ----------------> #



try:
    # instantiate PizzaPlotter class
    obj = PizzaPlotter(default_dict)

    # plot the chart
    fig, ax = obj.plot_pizza()

    # display chart
    st.pyplot(fig, bbox_inches="tight", pad_inches=0.035)
except Exception as e:
    st.error(e)
else:
    # Generate & Save
    st.sidebar.subheader("Save The Plot")
    get_your_plot(fig)