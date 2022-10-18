import streamlit as st
import pandas as pd

def main():
    st.header("header")
    st.title("Output examples")
    st.caption("caption")
    st.code("code")
    st.text("text")
    st.json({"key": "value"})
    st.markdown("markdown")

    st.dataframe(pd.DataFrame())
    st.table(pd.DataFrame())
    st.bar_chart(pd.DataFrame())
    st.map(pd.DataFrame())

main()
