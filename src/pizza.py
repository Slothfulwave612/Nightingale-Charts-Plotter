"""
Python module to plot Nightingale-Charts / Pizza-Charts.

Author: Anmol Durgapal / @slothfulwave612
"""

import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from mplsoccer import PyPizza
from highlight_text import fig_text
import streamlit as st

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
        self.inner_circle_limit = default_dict["inner_circle_limit"]
        self.slice_colors = default_dict["slice_colors"]
        self.slice_lw = default_dict["slice_lw"]
        self.slice_ec = default_dict["slice_ec"]
        self.slice_blank_colors = default_dict["slice_blank_colors"]
        self.transparency_blank_space = default_dict["transparency_blank_space"]

        # TEXT DESIGN LAYOUT
        self.param_text_colors = default_dict["param_text_colors"]
        self.param_text_size = default_dict["param_text_size"]
        self.param_location = default_dict["param_location"]
        self.value_text_color = default_dict["value_text_color"]
        self.value_text_size = default_dict["value_text_size"]
        self.value_boxstyle = default_dict["value_boxstyle"]
        self.box_pad = default_dict["box_pad"]
        self.box_ec = default_dict["box_ec"]
        self.box_lw = default_dict["box_lw"]
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
        self.num_legends = default_dict["num_legends"]
        self.legend_texts = default_dict["legend_texts"].strip()
        self.legend_space = int(default_dict["legend_space"])
        self.legend_size = default_dict["legend_size"]
        self.adjust_legend_x = default_dict["adjust_legend_x"]
        self.adjust_legend_y = default_dict["adjust_legend_y"]
        self.legend_alingment = default_dict["legend_alignment"]

        # CREDITS
        self.right_credit = default_dict["right_credit"]
        self.adjust_right_credit_x = default_dict["adjust_right_credit_x"]
        self.adjust_right_credit_y = default_dict["adjust_right_credit_y"]
        self.adjust_default_credit_x = default_dict["adjust_default_credit_x"]
        self.adjust_default_credit_y = default_dict["adjust_default_credit_y"]
        self.credit_size = default_dict["credit_size"]
        self.credit_color = default_dict["credit_color"]

        # manage newline
        self.params = [x.replace("\\n", "\n") for x in self.params]
        self.title = self.title.replace("\\n", "\n")
        self.sub_title = self.sub_title.replace("\\n", "\n")
        self.right_credit = self.right_credit.replace("\\n", "\n")

        # manage float-integer value
        self.values = [int(x) if x.is_integer() else x for x in self.values]

        # blank colors
        if self.slice_blank_colors != "same":
            self.slice_blank_colors = [self.slice_blank_colors] * len(self.params)

    @st.cache(ttl=3600*24, show_spinner=False)
    def load_fonts(self):
        # load the required fonts
        font_bold = fm.FontProperties(fname="fonts/BasierCircle-Bold.ttf")
        font_medium = fm.FontProperties(fname="fonts/BasierCircle-Medium.ttf")
        font_normal = fm.FontProperties(fname="fonts/BasierCircle-Regular.ttf")

        return font_bold, font_medium, font_normal

    
    def adjustFigAspect(self, fig, aspect=1):
        '''
        Adjust the subplot parameters so that the figure has the correct
        aspect ratio.
        '''
        xsize,ysize = fig.get_size_inches()
        minsize = min(xsize,ysize)
        xlim = .4*minsize/xsize
        ylim = .4*minsize/ysize
        if aspect < 1:
            xlim *= aspect
        else:
            ylim /= aspect
        fig.subplots_adjust(left=.5-xlim,
                            right=.5+xlim,
                            bottom=.5-ylim,
                            top=.5+ylim)


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

        if type(self.slice_colors) is list:
            slice_cols = self.slice_colors
            slice_fc = None
        else:
            slice_cols = None
            slice_fc = self.slice_colors


        if self.box_fc == "same":
            if type(slice_cols) is list:
                value_bck_colors = slice_cols
                self.box_fc = None
            else:
                value_bck_colors = None
                self.box_fc = slice_fc
        else:
            value_bck_colors = None


        if self.value_boxstyle == "none":
            bbox = dict(
                color=self.value_text_color,
                fontsize=self.value_text_size,
                zorder=3, va="center"
            )
        else:
            bbox = dict(
                color=self.value_text_color,
                fontsize=self.value_text_size,
                bbox=dict(
                    edgecolor=self.box_ec, facecolor=self.box_fc,
                    boxstyle=f"{self.value_boxstyle},pad={self.box_pad}",
                    lw=self.box_lw
                ),
                zorder=3, va="center"
            )


        # plot pizza
        fig, ax = baker.make_pizza(
            values=self.values,
            bottom=self.bottom,
            figsize=(12, 12),
            param_location=self.param_location,
            slice_colors=slice_cols,
            value_colors=None,
            value_bck_colors=value_bck_colors,
            color_blank_space=self.slice_blank_colors,
            blank_alpha=self.transparency_blank_space,

            kwargs_slices=dict(
                facecolor=slice_fc,
                edgecolor=self.slice_ec,
                linewidth=self.slice_lw,
                zorder=2,
            ),

            kwargs_params=dict(
                color=self.param_text_colors,
                fontsize=self.param_text_size,
                va="center",
            ),

            kwargs_values=bbox
        )

        baker.make_pizza(
            values=[self.inner_circle_limit]*len(self.params),
            bottom=-self.inner_circle_size,
            ax=ax,
            kwargs_slices=dict(
                facecolor=self.background_color,
                edgecolor=self.background_color,
                linewidth=1,
                zorder=3,
            ),

            kwargs_params=dict(alpha=0),
            kwargs_values=dict(alpha=0),
        )

        self.adjustFigAspect(fig, 0.6)

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

        # add legend
        if len(self.legend_texts) > 0:
            # fetch colors
            colors = dict()

            for color in self.slice_colors:
                if colors.get(color.lower()) is None:
                    colors[color.lower()] = True

            colors = list(colors.keys())

            # fetch texts
            legend_texts = self.legend_texts.split(' ')
            legend_texts = [x.replace('~', ' ') for x in legend_texts]

            colors = colors + [colors[-1]] * (len(legend_texts) - len(colors))
            temp_text = (' ' * self.legend_space).join(['<' + x + '>' for x in legend_texts])
            high_colors = [{"color": x} for x in colors[:len(legend_texts)]]

            fig_text(
                self.adjust_legend_x, self.adjust_legend_y, s=temp_text,
                fontsize=self.legend_size, fontproperties=font_bold,
                highlight_textprops=high_colors,
                ha=self.legend_alingment, fig=fig,
            )


        # add credits
        CREDIT_1 = self.right_credit
        CREDIT_2 = "Made Using: mplsoccer / Nightingale Chart Plotter\nInspired By: @Worville, @FootballSlices, @somazerofc & @Soumyaj15209314"

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
