"""
Python module to plot Nightingale-Charts / Pizza-Charts.

Author: Anmol Durgapal / @slothfulwave612
"""

import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from mplsoccer import PyPizza

class PizzaPlotter:
    """A class for plotting pizza charts using mplsoccer.

    Parameters
    ----------
    default_dict : dict
        All the default values we need to plot the pizza.
    """

    def __init__(self, default_dict):

        # TOTAL PARAMETERS
        self.num_params = default_dict["num_params"]
        
        # PARAMETER & VALUES
        self.params = default_dict["params"]
        self.values = default_dict["values"]

        # SLICE DESIGN LAYOUT
        self.background_color = default_dict["background_color"]
        self.straight_line_color = default_dict["straight_line_color"]
        self.straight_line_lw = default_dict["straight_line_lw"]
        self.straight_line_limit = default_dict["straight_line_limit"]
        self.bottom = default_dict["bottom"]
        self.straight_line_ls = default_dict["straight_line_ls"]
        self.last_circle_color = default_dict["last_circle_color"]
        self.last_circle_lw = default_dict["last_circle_lw"]
        self.last_circle_ls = default_dict["last_circle_ls"]
        self.other_circle_color = default_dict["other_circle_color"]
        self.other_circle_lw = default_dict["other_circle_lw"]
        self.other_circle_ls = default_dict["other_circle_ls"]
        self.inner_circle_size = default_dict["inner_circle_size"]
        self.choose_slice_colors = default_dict["choose_slice_colors"]
        self.slice_colors = default_dict["slice_colors"]
        self.slice_lw = default_dict["slice_lw"]
        self.slice_ec = default_dict["slice_ec"]
        self.choose_slice_blank_colors = default_dict["choose_slice_blank_colors"]
        self.slice_blank_colors = default_dict["slice_blank_colors"]
        self.transparency_blank_space = default_dict["transparency_blank_space"]

        # TEXT DESIGN LAYOUT
        self.param_text_colors = default_dict["param_text_colors"]
        self.param_text_size = default_dict["param_text_size"]
        self.param_location = default_dict["param_location"]
        self.choose_text_colors = default_dict["choose_text_colors"]
        self.value_text_color = default_dict["value_text_color"]
        self.value_text_size = default_dict["value_text_size"]
        self.value_boxstyle = default_dict["value_boxstyle"]
        self.box_pad = default_dict["box_pad"]
        self.box_ec = default_dict["box_ec"]
        self.box_lw = default_dict["box_lw"]
        self.choose_box_fc = default_dict["choose_box_fc"]
        self.box_fc = default_dict["box_fc"]

        # TITLE AND SUBTITLE
        self.title = default_dict["title"]
        self.title_size = default_dict["title_size"]
        self.title_color = default_dict["title_color"]
        self.adjust_title_x = default_dict["adjust_title_x"]
        self.adjust_title_y = default_dict["adjust_title_y"]
        self.title_alignment = default_dict["title_alignment"]
        self.sub_title = default_dict["sub_title"]
        self.sub_title_size = default_dict["sub_title_size"]
        self.sub_title_color = default_dict["sub_title_color"]
        self.adjust_sub_title_x = default_dict["adjust_sub_title_x"]
        self.adjust_sub_title_y = default_dict["adjust_sub_title_y"]
        self.sub_title_alignment = default_dict["sub_title_alignment"]

        # CREDITS
        self.right_credit = default_dict["right_credit"]
        self.adjust_right_credit_x = default_dict["adjust_right_credit_x"]
        self.adjust_right_credit_y = default_dict["adjust_right_credit_y"]
        self.adjust_default_credit_x = default_dict["adjust_default_credit_x"]
        self.adjust_default_credit_y = default_dict["adjust_default_credit_y"]
        self.credit_size = default_dict["credit_size"]
        self.credit_color = default_dict["credit_color"]


    def load_fonts(self):
        # load the required fonts
        font_bold = fm.FontProperties(fname="../fonts/BasierCircle-Bold.ttf")
        font_medium = fm.FontProperties(fname="../fonts/BasierCircle-Medium.ttf")
        font_normal = fm.FontProperties(fname="../fonts/BasierCircle-Regular.ttf")

        return font_bold, font_medium, font_normal


    def plot_pizza(self):
        # fetch fonts
        font_bold, font_medium, font_normal = self.load_fonts()

        # instantiate PyPizza class
        baker = PyPizza(
            params=self.params,
            background_color=self.background_color,
            inner_circle_size=self.inner_circle_size,
            straight_line_limit=self.straight_line_limit,
            straight_line_color=self.straight_line_color,
            straight_line_lw=self.straight_line_lw,
            straight_line_ls=self.straight_line_ls,
            last_circle_color=self.last_circle_color,
            last_circle_lw=self.last_circle_lw,
            last_circle_ls=self.last_circle_ls,
            other_circle_color=self.other_circle_color,
            other_circle_lw=self.other_circle_lw,
            other_circle_ls=self.other_circle_ls
        )

        # plot pizza
        fig, ax = baker.make_pizza(
            values=self.values,
            bottom=self.bottom,
            figsize=(12, 12),
            param_location=self.param_location,
            slice_colors=None,
            value_colors=None,
            value_bck_colors=None,
            color_blank_space=[self.slice_blank_colors] * len(self.params),
            blank_alpha=self.transparency_blank_space,

            kwargs_slices=dict(
                facecolor=self.slice_colors,
                edgecolor=self.slice_ec,
                linewidth=self.slice_lw,
                zorder=2,
            ),

            kwargs_params=dict(
                color=self.param_text_colors,
                fontsize=self.param_text_size,
            ),

            kwargs_values=dict(
                color=self.value_text_color,
                fontsize=self.value_text_size,
                bbox=dict(
                    edgecolor=self.box_ec, facecolor=self.box_fc,
                    boxstyle=f"{self.value_boxstyle},pad={self.box_pad}",
                    lw=self.box_lw
                )
            ),
        )

        # add title
        fig.text(
            self.adjust_title_x, self.adjust_title_y, self.title, size=self.title_size,
            ha=self.title_alignment, fontproperties=font_bold, color=self.title_color
        )

        # add subtitle
        fig.text(
            self.adjust_sub_title_x, self.adjust_sub_title_y, self.sub_title,
            size=self.sub_title_size, ha=self.sub_title_alignment,
            fontproperties=font_normal, color=self.sub_title_color
        )

        # add credits
        CREDIT_1 = self.right_credit
        CREDIT_2 = "Made Using: mplsoccer\nInspired By: @Worville, @FootballSlices, @somazerofc & @Soumyaj15209314"

        fig.text(
            self.adjust_right_credit_x, self.adjust_right_credit_y, CREDIT_1,
            size=self.credit_size, fontproperties=font_medium,
            color=self.credit_color, ha="right"
        )

        fig.text(
            self.adjust_default_credit_x, self.adjust_default_credit_y, CREDIT_2,
            size=self.credit_size, fontproperties=font_medium,
            color=self.credit_color, ha="left"
        )

        return fig, ax