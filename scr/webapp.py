"""
Python module for the webapp.

Author: Anmol Durgapal / @slothfulwave612
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import is_color_like
from matplotlib.backends.backend_agg import RendererAgg
from PIL import Image
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

# use renderer
matplotlib.use("agg")
_lock = RendererAgg.lock

# set page-config
st.set_page_config(page_title="Nightingale", page_icon=None, layout="centered", initial_sidebar_state='expanded')

# page-setup and title
background_and_title()

# <---------------- INITIAL SETUP ----------------> #

# fetch template
template, gen_temp = choose_template()

# get default-dict
default_dict = get_default_values(template_type=template)

# fetch number of parameters
num_params = pick_params(default_dict)

with st.sidebar.form(key="main_form"):
    # Second Options
    st.subheader("Edit Parameters & Values")
    st.write(
        """
        To make the required changes click the `Generate Plot` button below.
        """
    )

    # fetch parameter and corresponding values
    default_dict = pick_params_values(num_params, default_dict)

    # <---------------- EDIT DESIGN ----------------> #

    # Design
    st.subheader("Edit Design")

    # fetch slice design edits
    default_dict = edit_slice_design(default_dict, template, num_params)

    # fetch text design edits
    default_dict = edit_text_design(default_dict)

    # fetch title design edits
    default_dict= edit_title_design(default_dict, template)

    # fetch credit design edits
    default_dict = edit_credit_design(default_dict)

    # <---------------- EDIT DESIGN ----------------> #
    if (st.form_submit_button("Generate Plot") or num_params != default_dict["num_params"]) and not gen_temp:
        plot_fig = True
    else:
        plot_fig = False

if plot_fig:
    try:
        # instantiate PizzaPlotter class
        obj = PizzaPlotter(default_dict)

        # plot the chart
        fig, ax = obj.plot_pizza()

        # display chart
        st.pyplot(fig, bbox_inches="tight", pad_inches=0.035, dpi=300, format="jpg")

    except Exception as e:
        st.error(e)

else:
    st.image(Image.open(f"plots/{template}.png"))
