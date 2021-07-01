import streamlit as st
import session_state as SessionState

session = SessionState.get(run_id=0)

if st.button("Reset"):
    session.run_id += 1

options = ["a", "b"]
option_selected = st.radio("Label", options, key=session.run_id)
index_selected = options.index(option_selected)

st.write(option_selected)
st.write(index_selected)

option_selected_ = st.radio("Label", ["b", "d"], key=session.run_id)
st.write(option_selected_)