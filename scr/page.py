import streamlit as st

def background_and_title():
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
            <i>Make Percentile Nightingale-Charts / Pizza-Charts with a few clicks.<br>This webapp uses <a href="https://mplsoccer.readthedocs.io/" target="_blank">mplsoccer</a> 
            to make the nightingale-charts.</i>
            <br>
            <hr>
            <br>
        </center>
        """,
        unsafe_allow_html=True
    )