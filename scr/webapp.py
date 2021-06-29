"""
Python module for the webapp.

Author: Anmol Durgapal / @slothfulwave612
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import is_color_like
import streamlit as st

import default_values as dv
from pizza import PizzaPlotter

# set page-config
st.set_page_config(page_title="Nightingale", page_icon=None, layout="wide", initial_sidebar_state='expanded')

# set style
st.markdown(
    """
    <style>
    .reportview-container {
        background: #EBECE5
    }

    a:link{ color:#325FE5; } 
    a:visited{ color:#325FE5; } 
    a:hover{ color:#325FE5; } 
    a:active{ color:#325FE5}
    </style>
    """,
    unsafe_allow_html=True
)

# title and sub-title
st.markdown(
    """
    <center>
        <h1>Nightingale Chart Plotter</h1>
    </center>
    <center>
        <i>Make Percentile Nightingale-Charts / Pizza-Charts with a few clicks. This webapp uses <a href="https://mplsoccer.readthedocs.io/" target="_blank">mplsoocer</a> 
        to make the nightingale-charts.</i>
    </center>
    """,
    unsafe_allow_html=True
)

# template
template = st.sidebar.radio(
    label="Generate Template", options=["Light Theme Pizza", "Dark Theme Pizza", "Colorful Pizza (Light)", "Colorful Pizza (Dark)"],
    index=0, key="Generate Template", help="Choose the required template."
)

# get default-dict
default_dict = dv.get_default_values(template_type=template)


# sidebar - user input for params
num_params = st.sidebar.number_input(
    label="Total Number of Parameters", min_value=1,
    value=default_dict["num_params"],
    key="Total Number of Parameters", help="How many parameters do you have?"
)


# Second Options
st.sidebar.subheader("Edit Parameters & Values")

# expand section
expand = st.sidebar.radio(
    label="Expand All Parameter Widgets", options=["Yes", "No"],
    index=0, key="Expand All Parameter Widgets", help="Do you want to expand parameter widgets or not?"
)

if expand == "Yes": expand = True
else: expand = False

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


    with st.sidebar.beta_expander(f"Parameter {i+1}", expanded=expand):
        # user-input parameter-name
        param = st.text_input(
            label="Enter Parameter Name", value=param_name,
            key=f"Enter Parameter Name:", help="Type the parameter name."
        )

        # user-input parameter-value
        label = param.replace("\\n", ' ').replace("\\t", ' ') + " (value)"
        param_value = st.number_input(
            label=label, value=value,
            key=label, help=f"Type value for {label[:-8]}"
        )
        
        # add to list
        params.append(param)
        values.append(param_value)


# Design
st.sidebar.subheader("Edit Design")

# DESIGN LAYOUT
with st.sidebar.beta_expander("Slice Design Layout", expanded=False):
    # get background color
    background_color = st.color_picker(
        label="Background Color", value=default_dict["background_color"],
        key="Background Color", help="Choose a color for your plot's background."
    )

    # get straight line color
    straight_line_color = st.color_picker(
        label="Straight Line Color", value=default_dict["straight_line_color"],
        key="Straight Line Color", help="Choose a color for the straight lines in the plot."
    )

    # get straight line linewidth
    straight_line_lw = st.number_input(
        label="Straight Line Linewidth", min_value=0.0,
        value=default_dict["straight_line_lw"],
        key="Straight Line Linewidth", help="Enter linewidth for the straight lines."
    )

    # get straight-line linestyle
    straight_line_ls = st.selectbox(
        label="Straight-Line Linestyle", options=["None", "solid", "dashed", "dashdot", "dotted"],
        index=default_dict["straight_line_ls"], key="Straight-Line Linestyle",
        help="Choose a linestyle for the straight lines."
    )

    # get last circle color
    last_circle_color = st.color_picker(
        label="Last Circle Color", value=default_dict["last_circle_color"],
        key="Last Circle Color", help="Choose a color for the last circle in the plot."
    )

    # get last circle linewidth
    last_circle_lw = st.number_input(
        label="Last Circle Linewidth", min_value=0.0, value=default_dict["last_circle_lw"],
        key="Last Circle Linewidth", help="Enter linewidth for the last circle."
    )

    # get last circle linestyle
    last_circle_ls = st.selectbox(
        label="Last Circle Linestyle", options=["None", "solid", "dashed", "dashdot", "dotted"],
        index=default_dict["last_circle_ls"], key="Last Circle Linestyle",
        help="Choose a linestyle for the last circle."
    )

    # get other circles color
    other_circle_color = st.color_picker(
        label="Other Circles Color", value=default_dict["other_circle_color"],
        key="Other Circles Color", help="Choose a color for all the other circles in the plot."
    )

    # get other circles linewidth
    other_circle_lw = st.number_input(
        label="Other Circles Linewidth", min_value=0.0, value=default_dict["other_circle_lw"],
        key="Other Circles Linewidth", help="Enter linewidth for the other circles."
    )

    # get other circles linestyle
    other_circle_ls = st.selectbox(
        label="Other Circles Linestyle", options=["None", "solid", "dashed", "dashdot", "dotted"],
        index=default_dict["other_circle_ls"], key="Other Circles Linestyle",
        help="Choose a linestyle for the other circles."
    )

    # get inner circles size
    inner_circle_size = st.number_input(
        label="Inner Circle Size", min_value=0.0, value=default_dict["inner_circle_size"],
        key="Inner Circle Size", help="Enter size for the inner circle."
    )

    # slice colors
    choose_slice_colors = st.radio(
        label="Slice Colors", options=["Same Color", "Different Colors"],
        index=default_dict["choose_slice_colors"], key="Slice Colors",
        help="Do you want same color for all the slices or different colors?"
    )

    if choose_slice_colors == "Same Color":
        slice_colors = st.color_picker(
            label="Choose Slice Face Color", value=default_dict["slice_colors"],
            key="Choose Slice Face Color", help="Choose color for all the slices"
        )
    else:
        slice_colors = []

        for param in params:
            param = param.replace("\\n", ' ').replace("\\t", ' ')
            temp_color = st.color_picker(
                label=f"Color For {param} Slice", value=default_dict["slice_colors"],
                key=f"Color For {param} Slice", help=f"Choose color for {param} Slice"
            )
            slice_colors.append(param)

    # slice linewidth
    slice_lw = st.number_input(
        label="Slice Linewidth", 
        min_value=0.0, value=default_dict["slice_lw"],
        key="Slice Linewidth", help="Choose slice linewidth"
    )
    
    # slice-edge-color
    slice_ec= st.color_picker(
        label=f"Choose Slice Egde Color", value=default_dict["slice_ec"],
        key=f"Choose Slice Egde Color", help=f"Choose color for all the slice edges"
    )

    # slice-blank-space colors
    choose_slice_blank_colors = st.radio(
        label="Slice (Blank Space) Colors", options=["Same Color As The Slices", "Same Color (User Input)", "Different Colors"],
        index=default_dict["choose_slice_blank_colors"], key="Slice (Blank Space) Colors",
        help="Do you want same color for all the blank-slice-area or different colors?"
    )

    if choose_slice_blank_colors == "Same Color As The Slices":
        slice_blank_colors = "same"
    elif choose_slice_blank_colors == "Same Color (User Input)":
        slice_blank_colors = st.color_picker(
            label=f"Color For Blank Space", value=default_dict["slice_blank_colors"],
            key=f"Color For Blank Space", help=f"Choose color for blank space for all slices"
        )
    else:
        slice_blank_colors = []

        for i, param in enumerate(params):
            param = param.replace("\\n", ' ').replace("\\t", ' ')
            temp_color = st.color_picker(
                label=f"Color For Blank Space In Parameter {i+1}", value=default_dict["slice_blank_colors"],
                key=f"Color For Blank Space In Parameter {i+1}", help=f"Choose color for blank space in {param} slice"
            )
            slice_blank_colors.append(param)
    
    # transparency-level for blank-spaces
    transparency_blank_space = st.number_input(
        label="Transparency Level For Blank Space Colors", 
        min_value=0.0, max_value=1.0, value=default_dict["transparency_blank_space"],
        key="Transparency Level For Blank Space Colors", help="0 means fully-transparent, 1 means not-transparent"
    )

    # bottom-value for slice
    straight_line_limit = st.number_input(
        label="Start Value For The Slice", 
        value=default_dict["bottom"],
        key="Start Value For The Slice", help="Enter start value for the slice"
    )

    # end-value for slice
    bottom = st.number_input(
        label="End Value For The Slice", value=default_dict["straight_line_limit"],
        key="End Value For The Slice", help="Enter end value for the slice"
    )


# TEXT DESIGN LAYOUT
with st.sidebar.beta_expander("Text Design Layout", expanded=False):
    
    # param-text colors
    param_text_colors = st.color_picker(
        label="Parameter Text Color", value=default_dict["param_text_colors"],
        key="Parameter Text Color", help="Choose color for all the parameter texts"
    )
    
    # fontsize for param-text
    param_text_size = st.number_input(
        label="Parameter Texts Fontsize", 
        min_value=0.0, value=default_dict["param_text_size"],
        key="Parameter Texts Fontsize", help="Choose fontsize for parameter texts"
    )

    # location for param-text
    param_location = st.number_input(
        label="Parameter Location", 
        min_value=0.0, value=default_dict["param_location"],
        key="Parameter Location", help="Choose location for parameter texts"
    )

    # value colors
    choose_text_colors = st.radio(
        label="Value-Text Colors", options=["Same Color", "Different Colors"],
        index=default_dict["choose_text_colors"], key="Value Colors",
        help="Do you want same color for all the value-texts or different colors?"
    )

    if choose_text_colors == "Same Color":
        value_text_color = st.color_picker(
            label="Choose Value Text Color", value=default_dict["value_text_color"],
            key="Choose Value Text Color", help="Choose color for all the slices"
        )
    else:
        value_text_color = []

        for param in params:
            param = param.replace("\\n", ' ').replace("\\t", ' ')
            temp_color = st.color_picker(
                label=f"Color For ({param}) Value Text", value=default_dict["value_text_color"],
                key=f"Color For ({param}) Value Text", help=f"Choose color for {param} Value Text"
            )
            value_text_color.append(param)
        
    # fontsize for value-text
    value_text_size = st.number_input(
        label="Value Texts Fontsize", 
        min_value=0.0, value=default_dict["value_text_size"],
        key="Value Texts Fontsize", help="Choose fontsize for value texts"
    )
    
    # get boxstyle for value-text
    value_boxstyle = st.selectbox(
        label="Boxstyle For Value Text", options=["none", "circle", "round", "round4", "roundtooth", "sawtooth", "square"],
        index=default_dict["value_boxstyle"], key="Boxstyle For Value Text",
        help="Choose a boxstyle for the value-text."
    )

    # padding value
    box_pad = st.number_input(
        label="Padding Value For Box", 
        min_value=0.0, value=default_dict["box_pad"],
        key="Padding Value For Boxstyle", help="Choose padding-value for box."
    )

    # edgecolor for box
    box_ec = st.color_picker(
        label="Edgecolor For Box", value=default_dict["box_ec"],
        key="Edgecolor For Box", help="Choose edgecolor for box."
    )

    # linewidth for box
    box_lw = st.number_input(
        label="Linewidth For Box", 
        min_value=0.0, value=default_dict["box_lw"],
        key="Linewidth For Boxstyle", help="Choose linewidth for box."
    )

    # box facecolor
    choose_box_fc = st.radio(
        label="Facecolor For Box", options=["Same Color", "Different Colors"],
        index=default_dict["choose_box_fc"], key="Facecolor For Box",
        help="Do you want same color for all the box or different colors?"
    )

    if choose_box_fc == "Same Color":
        box_fc = st.color_picker(
            label="Choose Facecolor For All Boxes", value=default_dict["box_fc"],
            key="Choose Facecolor For All Boxes", help="Choose facecolor for all the boxes"
        )
    else:
        box_fc = []

        for param in params:
            param = param.replace("\\n", ' ').replace("\\t", ' ')
            temp_color = st.color_picker(
                label=f"Facecolor For ({param}) Value Box", value=default_dict["box_fc"],
                key=f"Facecolor For ({param}) Value Box", help=f"Choose facecolor for {param} Value Box"
            )
            box_fc.append(param)


# Title and Subtitle
with st.sidebar.beta_expander("Title & Subtitle Layout", expanded=False):
    # title
    title = st.text_input(
        label="Enter The Title", value=default_dict["title"],
        key=f"Enter The Title", help="Type the title for the visual."
    )

    # fontsize for title
    title_size = st.number_input(
        label="Title Fontsize", 
        min_value=0.0, value=default_dict["title_size"],
        key="Title Fontsize", help="Choose fontsize for the title."
    )

    # title color
    title_color = st.color_picker(
        label=f"Title Fontcolor", value=default_dict["title_color"],
        key=f"Title Fontcolor", help=f"Choose fontcolor for the title."
    )

    # adjust title (x-coordinate)
    adjust_title_x = st.number_input(
        label="Adjust Title (x-coord)", value=default_dict["adjust_title_x"],
        key="Adjust Title (x-coord)", help="Adjust x-coordinate for the title."
    )

    # adjust title (y-coordinate)
    adjust_title_y = st.number_input(
        label="Adjust Title (y-coord)", value=default_dict["adjust_title_y"],
        key="Adjust Title (y-coord)", help="Adjust y-coordinate for the title."
    )

    # title-alignment
    title_alignment = st.radio(
        label="Title Horizontal Alignment", options=["center", "right", "left"],
        index=0, key="Title Horizontal Alignment", help="Choose horizontal alingnment for title text"
    )

    # sub-title
    sub_title = st.text_input(
        label="Enter The Sub-Title", value=default_dict["sub_title"],
        key=f"Enter The Sub-Title", help="Type the sub-title for the visual."
    )

    # fontsize for title
    sub_title_size = st.number_input(
        label="Sub-Title Fontsize", 
        min_value=0.0, value=default_dict["sub_title_size"],
        key="Sub-Title Fontsize", help="Choose fontsize for the sub-title."
    )

    # title color
    sub_title_color = st.color_picker(
        label=f"Sub-Title Fontcolor", value=default_dict["sub_title_color"],
        key=f"Sub-Title Fontcolor", help=f"Choose fontcolor for the sub-title."
    )

    # adjust title (x-coordinate)
    adjust_sub_title_x = st.number_input(
        label="Adjust Sub-Title (x-coord)", value=default_dict["adjust_sub_title_x"],
        key="Adjust Sub-Title (x-coord)", help="Adjust x-coordinate for the sub-title."
    )

    # adjust title (y-coordinate)
    adjust_sub_title_y = st.number_input(
        label="Adjust Sub-Title (y-coord)", value=default_dict["adjust_sub_title_y"],
        key="Adjust Sub-Title (y-coord)", help="Adjust y-coordinate for the sub-title."
    )

    # sub-title-alignment
    sub_title_alignment = st.radio(
        label="Sub-Title Horizontal Alignment", options=["center", "right", "left"],
        index=0, key="Sub-Title Horizontal Alignment", help="Choose horizontal alingnment for sub-title text"
    )


# Credits Layout
with st.sidebar.beta_expander("Credits Layout", expanded=False):
    
    # right-credit
    right_credit = st.text_input(
        label="Enter The Credits", value=default_dict["right_credit"],
        key=f"Enter The Credits", help="Type the credits for the visual."
    )

    # adjust credit (x-coordinate)
    adjust_right_credit_x = st.number_input(
        label="Adjust Your Credit (x-coord)", 
        min_value=0.0, value=default_dict["adjust_right_credit_x"],
        key="Adjust Your Credit (x-coord)", help="Adjust x-coordinate for the credit text."
    )

    # adjust credit (y-coordinate)
    adjust_right_credit_y = st.number_input(
        label="Adjust Your Credit (y-coord)", 
        min_value=0.0, value=default_dict["adjust_right_credit_y"],
        key="Adjust Your Credit (y-coord)", help="Adjust y-coordinate for the credit text."
    )

    # adjust credit (x-coordinate)
    adjust_default_credit_x = st.number_input(
        label="Adjust Default Credit (x-coord)", 
        min_value=0.0, value=default_dict["adjust_default_credit_x"],
        key="Adjust Default Credit (x-coord)", help="Adjust x-coordinate for the default-credit text."
    )

    # adjust credit (y-coordinate)
    adjust_default_credit_y = st.number_input(
        label="Adjust Default Credit (y-coord)", 
        min_value=0.0, value=default_dict["adjust_default_credit_y"],
        key="Adjust Default Credit (x-coord)", help="Adjust y-coordinate for the default-credit text."
    )

    # fontsize for credit
    credit_size = st.number_input(
        label="Credit Fontsize", 
        min_value=0.0, value=default_dict["credit_size"],
        key="Credit Fontsize", help="Choose fontsize for the credit."
    )

    # title color
    credit_color = st.color_picker(
        label=f"Credit Fontcolor", value=default_dict["credit_color"],
        key=f"Credit Fontcolor", help=f"Choose fontcolor for the credit."
    )

# Generate & Save
st.sidebar.subheader("Generate & Save")

if st.sidebar.button("Make Pizza Chart"):
    default_dict = {
            
        # TOTAL PARAMETERS
        "num_params": num_params,

        # PARAMETER & VALUES
        "params": params,
        "values": values,

        # SLICE DESIGN LAYOUT
        "background_color": background_color,
        "straight_line_color": straight_line_color,
        "straight_line_lw": straight_line_lw,
        "straight_line_limit": straight_line_limit,
        "bottom": bottom,
        "straight_line_ls": straight_line_ls,
        "last_circle_color": last_circle_color,
        "last_circle_lw": last_circle_lw,
        "last_circle_ls": last_circle_ls,
        "other_circle_color": other_circle_color,
        "other_circle_lw": other_circle_lw,
        "other_circle_ls": other_circle_ls,
        "inner_circle_size": inner_circle_size,
        "choose_slice_colors": choose_slice_colors,
        "slice_colors": slice_colors,
        "slice_lw": slice_lw,
        "slice_ec": slice_ec,
        "choose_slice_blank_colors": choose_slice_blank_colors,
        "slice_blank_colors": slice_blank_colors,
        "transparency_blank_space": transparency_blank_space,

        # TEXT DESIGN LAYOUT
        "param_text_colors": param_text_colors,
        "param_text_size": param_text_size,
        "param_location": param_location,
        "choose_text_colors": choose_text_colors,
        "value_text_color": value_text_color,
        "value_text_size": value_text_size,
        "value_boxstyle": value_boxstyle,
        "box_pad": box_pad,
        "box_ec": box_ec,
        "box_lw": box_lw,
        "choose_box_fc": choose_box_fc,
        "box_fc": box_fc,

        # TITLE AND SUBTITLE
        "title": title,
        "title_size": title_size,
        "title_color": title_color,
        "adjust_title_x": adjust_title_x,
        "adjust_title_y": adjust_title_y,
        "title_alignment": title_alignment,
        "sub_title": sub_title,
        "sub_title_size": sub_title_size,
        "sub_title_color": sub_title_color,
        "adjust_sub_title_x": adjust_sub_title_x,
        "adjust_sub_title_y": adjust_sub_title_y,
        "sub_title_alignment": sub_title_alignment,

        # CREDITS
        "right_credit": right_credit,
        "adjust_right_credit_x": adjust_right_credit_x,
        "adjust_right_credit_y": adjust_right_credit_y,
        "adjust_default_credit_x": adjust_default_credit_x,
        "adjust_default_credit_y": adjust_default_credit_y,
        "credit_size": credit_size,
        "credit_color": credit_color,
        
    }

    # instantiate PizzaPlotter class
    obj = PizzaPlotter(default_dict)
    
    # # plot the chart
    fig, ax = obj.plot_pizza()

    # display chart
    st.pyplot(fig)

# Credits Layout
with st.sidebar.beta_expander("Download The Plot", expanded=False):

    # filename
    filename = st.text_input(
        label="Enter The Filename", value="my_file",
        key=f"Enter The Filename", help="Type the filename (without file-format)"
    )

    # file-format
    file_format = st.radio(
        label="File Format", options=["png", "jpg", "jpeg", "pdf", "raw", "svg", "svgz", "tif", "tiff"],
        index=0, key="File Format", help="Choose the required file-format."
    )

    # dpi
    dpi = st.number_input(
        label="Dots-per-Inch Value", 
        min_value=50, value=500,
        key="Dots-per-Inch Value", help="Higher The Value Better The Resolution."
    )

    # transparency
    transparency = st.radio(
        label="Transparent", options=["Yes", "No"],
        index=1, key="Transparent", help="Downloaded plot will not have background. (file-format should be png)"
    )

    # pad-inches
    pad_inches = st.number_input(
        label="Pad Inches", value=0.03,
        key="Pad Inches", help="Amount of padding around the plot."
    )

    # download button
    if st.button("Download Your Chart"):
        pass
