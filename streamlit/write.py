import streamlit as st
import pandas as pd

st.write('Hello, *JOJO* :sunglasses:')
st.write(1,2,3,4,5,6)

st.write(
    pd.DataFrame(
        {
            "First column" : ['1부','2부','3부','4부','5부','6부','7부'],
            'second column': ['죠나단','죠셉','죠타로','죠스케','죠르노','죠린','죠니']
        }
    )
)
