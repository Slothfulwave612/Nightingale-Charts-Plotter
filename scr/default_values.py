"""
Python module for default values.

Author: Anmol Durgapal / @slothfulwave612
"""

def get_default_values(template_type):
    """
    Function to get default value dict.

    Arguments:
        template_type: string.
        Type of template.
    
    Returns:
        dict containing default values.
    """
    if template_type == "Light Theme Pizza":
        default_dict = {
            
            # TOTAL PARAMETERS
            "num_params": 12,

            # PARAMETER & VALUES
            "params": [
                "Non-Penalty Goals", "npxG", "npxG per Shot", "\\nxA", "Open Play\\nSCA",
                "\\nPenalty Area\nEntries", "Progressive\\nPasses", "Progressive\nCarries",
                "Successful\nDribbles", "\\nTouches\\nper Turnover", "pAdj\\nPress Regains", "Aerials Won"
            ],
            "values": [99.0, 99.0, 87.0, 51.0, 62.0, 58.0, 45.0, 40.0, 27.0, 74.0, 77.0, 73.0],

            # SLICE DESIGN LAYOUT
            "background_color": "#EBECE5",
            "straight_line_color": "#EBECE5",
            "straight_line_lw": 2.0,
            "straight_line_limit": 100.0,
            "bottom": 0.0,
            "straight_line_ls": 1,
            "last_circle_color": "#222222",
            "last_circle_lw": 0.0,
            "last_circle_ls": 1,
            "other_circle_color": "#222222",
            "other_circle_lw": 0.0,
            "other_circle_ls": 1,
            "inner_circle_size": 5.0,
            "choose_slice_colors": 0,
            "slice_colors": "#65ADFF",
            "slice_lw": 2.0,
            "slice_ec": "#EBECE5",
            "choose_slice_blank_colors": 1,
            "slice_blank_colors": "#6495ED",
            "transparency_blank_space": 0.2,

            # TEXT DESIGN LAYOUT
            "param_text_colors": "#222222",
            "param_text_size": 12.0,
            "param_location": 107.0,
            "choose_text_colors": 0,
            "value_text_color": "#101010",
            "value_text_size": 12.0,
            "value_boxstyle": 1,
            "box_pad": 0.3,
            "box_ec": "#101010",
            "box_lw": 1.0,
            "choose_box_fc": 0,
            "box_fc": "#65ADFF",

            # TITLE AND SUBTITLE
            "title": "Robert Lewandowski - FC Bayern Munich",
            "title_size": 20.0,
            "title_color": "#222222",
            "adjust_title_x": 0.515,
            "adjust_title_y": 0.99,
            "title_alignment": "center",
            "sub_title": "Percentile Rank vs Top-Five League Forwards | Season 2020-21\\nMinutes Played: 2,458 | Age: 32 years",
            "sub_title_size": 15.0,
            "sub_title_color": "#222222",
            "adjust_sub_title_x": 0.515,
            "adjust_sub_title_y": 0.947,
            "sub_title_alignment": "center",

            # CREDITS
            "right_credit": "Source: Statsbomb via FBRef.com",
            "adjust_right_credit_x": 0.925,
            "adjust_right_credit_y": 0.05,
            "adjust_default_credit_x": 0.0925,
            "adjust_default_credit_y": 0.05,
            "credit_size": 9.0,
            "credit_color": "#222222"
            
        }
    
    else:
        default_dict = {}

    return default_dict
