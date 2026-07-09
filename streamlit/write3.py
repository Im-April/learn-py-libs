import streamlit as st
import pandas as pd
import altair as alt
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((200,3)), columns=['a','b','c'])
chart = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.write(chart)