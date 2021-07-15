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
                "Non-Penalty Goals", "npxG", "npxG per Shot", "xA", "Open Play\\nSCA",
                "Penalty Area\\nEntries", "Progressive\\nPasses", "Progressive\\nCarries",
                "Successful\\nDribbles", "Touches\\nper Turnover", "pAdj\\nPress Regains", "Aerials Won"
            ],
            "values": [99.0, 99.0, 87.0, 51.0, 62.0, 58.0, 45.0, 40.0, 27.0, 74.0, 77.0, 73.0],

            # SLICE DESIGN LAYOUT
            "background_color": "#EBECE5",
            "straight_line_color": "#EBECE5",
            "straight_line_lw": 1.0,
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
            "inner_circle_limit": 4.6,
            "choose_slice_colors": 0,
            "slice_colors": "#65ADFF",
            "slice_lw": 1.0,
            "slice_ec": "#EBECE5",
            "choose_slice_blank_colors": 1,
            "slice_blank_colors": "#6495ED",
            "transparency_blank_space": 0.2,

            # TEXT DESIGN LAYOUT
            "param_text_colors": "#222222",
            "param_text_size": 8.0,
            "param_location": 107.0,
            "value_text_color": "#101010",
            "value_text_size": 8.0,
            "value_boxstyle": 1,
            "box_pad": 0.35,
            "box_ec": "#101010",
            "box_lw": 1.0,
            "choose_box_fc": 0,
            "box_fc": "#65ADFF",

            # TITLE AND SUBTITLE
            "title": "Robert Lewandowski - FC Bayern Munich",
            "title_size": 14.0,
            "title_color": "#222222",
            "adjust_title_x": 0.5,
            "adjust_title_y": 0.810,
            "title_alignment": "center",
            "sub_title": "Percentile Rank vs Top-Five League Forwards | Season 2020-21\\nMinutes Played: 2458 | Age: 32 years",
            "sub_title_size": 10.5,
            "sub_title_color": "#222222",
            "adjust_sub_title_x": 0.5,
            "adjust_sub_title_y": 0.780,
            "sub_title_alignment": "center",
            "num_legends": 0,
            "legend_texts": "",
            "legend_space": 2,
            "legend_size": 14.0,
            "adjust_legend_x": 0.5,
            "adjust_legend_y": 0.787,
            "legend_alignment": "center",

            # CREDITS
            "right_credit": "All metrics are normalized per90\\nSource: Statsbomb via FBRef.com",
            "adjust_right_credit_x": 0.770,
            "adjust_right_credit_y": 0.215,
            "adjust_default_credit_x": 0.22,
            "adjust_default_credit_y": 0.215,
            "credit_size": 6.0,
            "credit_color": "#222222"
            
        }
    
    elif template_type == "Dark Theme Pizza":
        default_dict = {
            
            # TOTAL PARAMETERS
            "num_params": 12,

            # PARAMETER & VALUES
            "params": [
                "Non-Penalty Goals", "npxG", "npxG per Shot", "xA", "Open Play\\nSCA",
                "Penalty Area\\nEntries", "Progressive\\nPasses", "Progressive\\nCarries",
                "Successful\\nDribbles", "Touches\\nper Turnover", "pAdj\\nPress Regains", "Aerials Won"
            ],
            "values": [99.0, 99.0, 87.0, 51.0, 62.0, 58.0, 45.0, 40.0, 27.0, 74.0, 77.0, 73.0],

            # SLICE DESIGN LAYOUT
            "background_color": "#222222",
            "straight_line_color": "#222222",
            "straight_line_lw": 1.0,
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
            "inner_circle_limit": 4.6,
            "choose_slice_colors": 0,
            "slice_colors": "#4169E1",
            "slice_lw": 1.0,
            "slice_ec": "#222222",
            "choose_slice_blank_colors": 0,
            "slice_blank_colors": "#6495ED",
            "transparency_blank_space": 0.4,

            # TEXT DESIGN LAYOUT
            "param_text_colors": "#F9F9F9",
            "param_text_size": 8.0,
            "param_location": 107.0,
            "value_text_color": "#121212",
            "value_text_size": 8.0,
            "value_boxstyle": 1,
            "box_pad": 0.35,
            "box_ec": "#222222",
            "box_lw": 1.0,
            "choose_box_fc": 0,
            "box_fc": "#4169E1",

            # TITLE AND SUBTITLE
            "title": "Robert Lewandowski - FC Bayern Munich",
            "title_size": 14.0,
            "title_color": "#F9F9F9",
            "adjust_title_x": 0.5,
            "adjust_title_y": 0.810,
            "title_alignment": "center",
            "sub_title": "Percentile Rank vs Top-Five League Forwards | Season 2020-21\\nMinutes Played: 2458 | Age: 24 years",
            "sub_title_size": 10.5,
            "sub_title_color": "#F9F9F9",
            "adjust_sub_title_x": 0.5,
            "adjust_sub_title_y": 0.780,
            "sub_title_alignment": "center",
            "num_legends": 0,
            "legend_texts": "",
            "legend_space": 2,
            "legend_size": 14.0,
            "adjust_legend_x": 0.5,
            "adjust_legend_y": 0.787,
            "legend_alignment": "center",

            # CREDITS
            "right_credit": "All metrics are normalized per90\\nSource: Statsbomb via FBRef.com",
            "adjust_right_credit_x": 0.770,
            "adjust_right_credit_y": 0.215,
            "adjust_default_credit_x": 0.22,
            "adjust_default_credit_y": 0.215,
            "credit_size": 6.0,
            "credit_color": "#F9F9F9"
            
        }
    
    elif template_type == "Colorful Pizza (Light)":
        default_dict = {
            
            # TOTAL PARAMETERS
            "num_params": 15,

            # PARAMETER & VALUES
            "params": [
                "Non-Penalty Goals", "npxG", "xA", "Open Play\\nSCA", "Penalty Area\\nEntries",
                "Touches\\nper Turnover", "Progressive\\nPasses", "Progressive\\nCarries",
                "Final Third\\nPasses", "Final Third\\nCarries", "pAdj\\nPressure Regains",
                "pAdj\\nTackles Made", "pAdj\\nInterceptions", "Recoveries", "Aerial Win %"
            ],
            "values": [70.0, 77.0, 74.0, 68.0, 60.0, 96.0, 89.0, 97.0, 92.0, 94.0, 16.0, 19.0, 56.0, 53.0, 94.0],

            # SLICE DESIGN LAYOUT
            "background_color": "#EBEBE5",
            "straight_line_color": "#EBEBE5",
            "straight_line_lw": 1.0,
            "straight_line_limit": 100.0,
            "bottom": 0.0,
            "straight_line_ls": 1,
            "last_circle_color": "#EBEBE5",
            "last_circle_lw": 0.0,
            "last_circle_ls": 1,
            "other_circle_color": "#222222",
            "other_circle_lw": 0.0,
            "other_circle_ls": 1,
            "inner_circle_size": 5.0,
            "inner_circle_limit": 4.6,
            "choose_slice_colors": 1,
            "slice_colors": ["#008080"] * 5 + ["#D65DB1"] * 5 + ["#1A78CF"] * 5,
            "slice_lw": 1.0,
            "slice_ec": "#F2F2F2",
            "choose_slice_blank_colors": 0,
            "slice_blank_colors": "same",
            "transparency_blank_space": 0.4,

            # TEXT DESIGN LAYOUT
            "param_text_colors": "#222222",
            "param_text_size": 8.0,
            "param_location": 107.0,
            "value_text_color": "#F9F9F9",
            "value_text_size": 8.0,
            "value_boxstyle": 1,
            "box_pad": 0.35,
            "box_ec": "#EBECE5",
            "box_lw": 1.0,
            "choose_box_fc": 0,
            "box_fc": "same",

            # TITLE AND SUBTITLE
            "title": "Frenkie de Jong - FC Barcelona",
            "title_size": 14.0,
            "title_color": "#222222",
            "adjust_title_x": 0.5,
            "adjust_title_y": 0.84,
            "title_alignment": "center",
            "sub_title": "Percentile Rank vs Top-Five League Midfielders | Season 2020-21\\nMinutes Played: 3154 | Age: 32 years",
            "sub_title_size": 10.5,
            "sub_title_color": "#222222",
            "adjust_sub_title_x": 0.5,
            "adjust_sub_title_y": 0.81,
            "sub_title_alignment": "center",
            "num_legends": 3,
            "legend_texts": "Attacking Possession Defending",
            "legend_space": 2,
            "legend_size": 14.0,
            "adjust_legend_x": 0.5,
            "adjust_legend_y": 0.795,
            "legend_alignment": "center",

            # CREDITS
            "right_credit": "All metrics are normalized per90\\nSource: Statsbomb via FBRef.com",
            "adjust_right_credit_x": 0.775,
            "adjust_right_credit_y": 0.215,
            "adjust_default_credit_x": 0.22,
            "adjust_default_credit_y": 0.215,
            "credit_size": 6.0,
            "credit_color": "#222222"
            
        }
    
    elif template_type == "Colorful Pizza (Dark)":
        default_dict = {
            
            # TOTAL PARAMETERS
            "num_params": 15,

            # PARAMETER & VALUES
            "params": [
                "Non-Penalty Goals", "npxG", "xA", "Open Play\\nSCA", "Penalty Area\\nEntries",
                "Touches\\nper Turnover", "Progressive\\nPasses", "Progressive\\nCarries",
                "Final Third\\nPasses", "Final Third\\nCarries", "pAdj\\nPressure Regains",
                "pAdj\\nTackles Made", "pAdj\\nInterceptions", "Recoveries", "Aerial Win %"
            ],
            "values": [70.0, 77.0, 74.0, 68.0, 60.0, 96.0, 89.0, 97.0, 92.0, 94.0, 16.0, 19.0, 56.0, 53.0, 94.0],

            # SLICE DESIGN LAYOUT
            "background_color": "#222222",
            "straight_line_color": "#222222",
            "straight_line_lw": 1.0,
            "straight_line_limit": 100.0,
            "bottom": 0.0,
            "straight_line_ls": 1,
            "last_circle_color": "#222222",
            "last_circle_lw": 0.0,
            "last_circle_ls": 1,
            "other_circle_color": "#F9F9F9",
            "other_circle_lw": 0.0,
            "other_circle_ls": 1,
            "inner_circle_size": 5.0,
            "inner_circle_limit": 4.6,
            "choose_slice_colors": 1,
            "slice_colors": ["#008080"] * 5 + ["#D65DB1"] * 5 + ["#1A78CF"] * 5,
            "slice_lw": 1.0,
            "slice_ec": "#222222",
            "choose_slice_blank_colors": 0,
            "slice_blank_colors": "same",
            "transparency_blank_space": 0.4,

            # TEXT DESIGN LAYOUT
            "param_text_colors": "#F9F9F9",
            "param_text_size": 8.0,
            "param_location": 107.0,
            "value_text_color": "#F9F9F9",
            "value_text_size": 8.0,
            "value_boxstyle": 1,
            "box_pad": 0.35,
            "box_ec": "#222222",
            "box_lw": 1.0,
            "choose_box_fc": 0,
            "box_fc": "same",

            # TITLE AND SUBTITLE
            "title": "Frenkie de Jong - FC Barcelona",
            "title_size": 14.0,
            "title_color": "#F9F9F9",
            "adjust_title_x": 0.5,
            "adjust_title_y": 0.84,
            "title_alignment": "center",
            "sub_title": "Percentile Rank vs Top-Five League Midfielders | Season 2020-21\\nMinutes Played: 3154 | Age: 32 years",
            "sub_title_size": 10.5,
            "sub_title_color": "#F9F9F9",
            "adjust_sub_title_x": 0.5,
            "adjust_sub_title_y": 0.81,
            "sub_title_alignment": "center",
            "num_legends": 3,
            "legend_texts": "Attacking Possession Defending",
            "legend_space": 2,
            "legend_size": 14.0,
            "adjust_legend_x": 0.5,
            "adjust_legend_y": 0.795,
            "legend_alignment": "center",

            # CREDITS
            "right_credit": "All metrics are normalized per90\\nSource: Statsbomb via FBRef.com",
            "adjust_right_credit_x": 0.775,
            "adjust_right_credit_y": 0.215,
            "adjust_default_credit_x": 0.22,
            "adjust_default_credit_y": 0.215,
            "credit_size": 6.0,
            "credit_color": "#F9F9F9"
            
        }

    return default_dict
